import customtkinter
import suggest_fr
import load_data
from difflib import get_close_matches
import time
import trie
import pickle
with open("set.pkl","rb") as pic:
    data = pickle.load(pic)
customtkinter.set_appearance_mode(data["theme"])
customtkinter.set_default_color_theme(data["color"])

class Search_entr:
    def __init__(self,lang):
        self.lang = lang
    
        self.root = customtkinter.CTk()
        
        self.root.geometry("400x500")
        self.root.resizable(False,False)
        self.root.attributes("-topmost",True)
        
        self.word = []
        self.meaning = []
        self.Trie_per = trie.Trie()
        self.Trie_eng =trie.Trie()
        
        if data["color"] == "blue" and data["theme"] == "dark":
            self.fg_set = "#333536"
        elif data["color"] == "green" and data["theme"] == 'light':
            self.fg_set = "#bfbfbf"
        elif data["color"] == "green" and data["theme"] == 'dark':
            self.fg_set = "#333536"
        elif data["color"] == "blue" and data["theme"] == 'light':
            self.fg_set = "#bfbfbf"
        self.root.rowconfigure((0,1),weight=0)
        self.root.columnconfigure((0),weight=1)

        self.search_entry = customtkinter.CTkEntry(self.root,height=40,font=("Arial",20),placeholder_text="🔍  Search")
        self.search_entry.grid(row=0,column=0,sticky="ew",padx=12,pady=12)

        self.fr_sc = customtkinter.CTkScrollableFrame(self.root,height=400)
        self.fr_sc.grid(row=1,column=0,sticky="ewn",pady=12,padx=12)
        self.fr_sc.rowconfigure((0,1),weight=1)
        self.fr_sc.columnconfigure((0),weight=1)

        self.search_entry.bind('<KeyRelease>',self.suggest)

        self.root.bind("<FocusIn>",self.focus_in)
        self.root.mainloop()
    
    def focus_in(self,e):
        with open("set.pkl","rb") as pic:
            data = pickle.load(pic)
        customtkinter.set_appearance_mode(data["theme"])
        customtkinter.set_default_color_theme(data["color"])
        
        self.root.update_idletasks()
    def suggest(self,e):
            
        word_l = self.search_entry.get()
        
            
        
            
        if self.lang =="eng":
            if len(word_l) == 1:
                self.word,self.meaning = load_data.load(word_l,"eng")
            for w in self.word:
                self.Trie_eng.insert(w)
        else:
            if len(word_l) == 1:        
                self.meaning, self.word_dl  = load_data.english_english_persian_json("Persian-Persian\index.json")
                    
                for x in self.word_dl:
                    for u in x:
                        self.word.append(u)
                        self.Trie_per.insert(u)
            
        if len(word_l) == 0:
            for x in self.fr_sc.winfo_children():
                x.grid_forget()
        found = []
            
        found= self.Trie_per.search_prefix(word_l)
            
        if self.lang == "eng":
            result = self.Trie_eng.search_prefix(word_l)
            if len(result) > 20:
                    found = result[:20]
            else:
                found = result
                # found = get_close_matches(word_l,word,n=7,cutoff=0.01)
        else:
            result = self.Trie_per.search_prefix(word_l)
            if len(result) > 20:
                found= result[:20]
            else:
                found =result
        for u in found:
            
            suggest_fr.suggest_frame(word=u,master=self.fr_sc,lang=self.lang,fg_color=self.fg_set).placing(found.index(u))
                



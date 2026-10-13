import customtkinter
import load_data
import tkinter
from tkinter import *
import pickle
with open("set.pkl","rb") as pic:
    data = pickle.load(pic)
customtkinter.set_appearance_mode(data["theme"])
customtkinter.set_default_color_theme(data["color"])

class suggest_frame(customtkinter.CTkFrame):
    def __init__(self, word, lang,master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = "gray20", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.master = master
        self.word= word
        
        self.lang = lang
        self.lbl = customtkinter.CTkLabel(self,text=word)
        self.btn  = customtkinter.CTkButton(self,text="More",font=("Arial",10),width=30,command=self.info)

        self.lbl.grid(row=0,column=0,sticky="w",columnspan=5,pady=12,padx=12)
        self.btn.grid(row=0,column=5,sticky="ew",pady=12,padx=12)
    def placing(self,row):
        self.grid(row=row,column=0,columnspan=2,sticky="ew",pady=12,padx=12)
        self.rowconfigure((0),weight=1)
        self.columnconfigure((0,1,2,3,4,5),weight=1)


    def meaning(self):
        word = self.word
        
        return_list = []
        return_list_per = []
        #==========================================================================
        if self.lang == "eng":
            words,meaning = load_data.load(word[0],lan="eng")
            words_per,meaning_per = load_data.load(word[0],lan="per")
            for w in words:
                if w ==word:
                    if meaning[words.index(w)] not in return_list:
                        return_list.append(meaning[words.index(w)])
            for wp in words_per:
                if wp == word:
                    if meaning_per[words_per.index(wp)] not in return_list_per:
                        return_list_per.append(meaning_per[words_per.index(wp)])
        #==========================================================================
        else:
            meaning, word_dl  = load_data.english_english_persian_json("Persian-Persian\index.json")
            for x in word_dl:
                for u in x:
                    if u == self.word:
                        return_list.append(meaning[word_dl.index(x)])
        #==========================================================================
        return return_list,return_list_per
        
        
    def info(self):
        for x in self.master.winfo_children():
            if x.widgetName == "toplevel":
                x.destroy()
        self.toplevel  = customtkinter.CTkToplevel(master = self.master)
        self.toplevel.attributes("-topmost",True)
        self.toplevel.title(self.word)
        self.toplevel.resizable(False,False)
        self.toplevel.geometry("400x300")
        self.toplevel.rowconfigure((0,1,2),weight=0)
        self.toplevel.columnconfigure((0),weight=1)
        self.word_lbl = customtkinter.CTkLabel(self.toplevel,text=self.word,font=("Arial",30))
        self.word_lbl.grid(row=0,column=0,sticky="w",pady=12,padx=12)
         
        
#Englist --> English
#English --> Perisna
#=============================================================================================================
        if self.lang == "eng":
            per_list,eng_list= self.meaning()

            self.meaning_lbl_eng  = customtkinter.CTkTextbox(self.toplevel,width=500,state='normal',height=50,)
            self.meaning_lbl_eng.grid(row=1,column=0,sticky="ew",pady=12,padx=12)
            for u in eng_list:
                u = u.rstrip("']")
                u = u.lstrip("['")
                u = u.split("', '")
                for ele in u:
                    if u.index(ele) != 0:
                        self.meaning_lbl_eng.insert('end',", ")
                    for x in ele.split(" ")[::-1]:
                        self.meaning_lbl_eng.insert('end',x+" ")
                    
            self.meaning_lbl_per  = customtkinter.CTkTextbox(self.toplevel,width=500,state='normal',height=150)
            self.meaning_lbl_per.grid(row=2,column=0,sticky="ew",pady=0,padx=12)

            meaing_no_per = 1
            for u in per_list:
                u = u.rstrip("']")
                u = u.lstrip("['")
                u = u.split("', '")
                for ele in u:
                    self.meaning_lbl_per.insert('end',str(meaing_no_per)+" -  "+"   "+ele+"\n\n")
                    meaing_no_per+=1
            self.meaning_lbl_eng.configure(state="disabled")
            self.meaning_lbl_per.configure(state="disabled")
#================================================================================================================
#Persian --> English
#Persian --> Perisna
#================================================================================================================#=======
        else:
            eng,per= self.meaning()
            self.meaning_lbl_eng  = customtkinter.CTkTextbox(self.toplevel,width=500,state='normal')
            self.meaning_lbl_eng.grid(row=1,column=0,rowspan=3,sticky="ew",pady=12,padx=12)
            number = 1
            for x in eng:
                self.meaning_lbl_eng.insert('end',str(number) + " - " + x + "\n")
                number+=1
#========================================================================================================================
        self.toplevel.anchor("w")
        
        

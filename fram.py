import customtkinter
import PIL
import sys
import english_search
import win32api
import win32gui
import win32con
import pickle
import settings


with open("set.pkl","rb") as pic:
    data = pickle.load(pic)
customtkinter.set_appearance_mode(data["theme"])
customtkinter.set_default_color_theme("green")


class frame(customtkinter.CTkFrame):
    def __init__(self, img,text, row,column,master, width = 200, span =1,height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.row = row
        self.text = text
        self.span =span
        self.column = column
        self.master = master
        self.img = img 
        
        self.bind('<Enter>',self.enter_chg)
        self.bind('<Leave>',self.leave_chg)
        self.bind('<Button-1>',self.show_info)
    def change_lang(self,code):
        hwnd = win32gui.GetForegroundWindow()
        win32api.SendMessage(
            hwnd,win32con.WM_INPUTLANGCHANGEREQUEST,0,code
        )
    def enter_chg(self,ar):
        if data["color"] == "blue" and data["theme"] == "dark":
            self.configure(fg_color="#1F6AA5")
        elif data["color"] == "green" and data["theme"] == "light":
            self.configure(fg_color="#2FA572")
        elif data["color"] == "green" and data["theme"] == "dark":
            self.configure(fg_color="#2FA572")
        elif data["color"] == "blue" and data["theme"] == "light":
            self.configure(fg_color="#1F6AA5")
    def leave_chg(self,ar):

        if data["color"] == "blue" and data["theme"] == "dark":

            self.configure(fg_color="gray17")
        elif data["color"] == "green" and data["theme"] == "light":
            self.configure(fg_color = "white")
        elif data['color'] == "green" and data["theme"] == "dark":
            self.configure(fg_color="gray17")
        elif data['color'] == "blue" and data["theme"] == "light":
            self.configure(fg_color = "white")
    def placing(self):
        self.grid(row=self.row,column=self.column,sticky="ew",pady=12,padx=12,columnspan = self.span)
        self.rowconfigure((0,1),weight=1)
        self.columnconfigure((0,1),weight=1)

    def lbl_placing(self):
        self.lbl  = customtkinter.CTkLabel(self,image=self.img,text="")
        self.txt  = customtkinter.CTkLabel(self,text=self.text,font=("Arial",15))
        
        self.lbl.grid(row=0,column =0,columnspan = 2,sticky="ew",pady=12,padx=12)
        self.txt.grid(row=1,column =0,columnspan = 2,sticky="ew",pady=(0,12))
        self.lbl.bind('<Enter>',self.enter_chg)
        self.txt.bind('<Enter>',self.enter_chg)
        self.lbl.bind('<Button-1>',self.show_info)
    
    
    def show_info(self,e):
        if self.txt.cget("text") == "English":
            self.change_lang(0x4090409)
            english_search.Search_entr("eng")
        elif self.txt.cget("text") == "Dari":
            self.change_lang(0x4290429)
            english_search.Search_entr("per")
        elif self.txt.cget('text') == "Settings":
           
            settings.SettingsWindow().mainloop()
            
        else:
            sys.exit()
    
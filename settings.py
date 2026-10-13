import customtkinter as ctk
from tkinter import font
import pickle


with open("set.pkl","rb") as pic:
    data = pickle.load(pic)
ctk.set_appearance_mode(data["theme"])
ctk.set_default_color_theme(data["color"])


class SettingsWindow(ctk.CTk):
   
    def __init__(self):
        super().__init__()
        
        self.title("Settings")
        self.geometry("300x330")
        self.resizable(False,False)
       
        
        
        
        ctk.CTkLabel(self, text="Theme:").pack()
        self.theme_dropdown = ctk.CTkComboBox(self,  values=["Light", "Dark"])
        self.theme_dropdown.set(data["theme"])
        self.theme_dropdown.pack(pady=(1,12))

        
    
        
        ctk.CTkLabel(self, text="Color:").pack()
        self.color_dropdown = ctk.CTkComboBox(self,values=["Green", "Blue"])
        self.color_dropdown.set(data["color"])
        self.color_dropdown.pack(pady=(1,12))

        
        

        ctk.CTkButton(self, text="Apply", command=self.get_settings).pack()

    def get_settings(self):
        
        settings = {
            "theme": self.theme_dropdown.get().lower(),
            "color": self.color_dropdown.get().lower(),
            
        }
        
        with open("set.pkl","wb") as pic:
            pickle.dump(settings,pic)

        print(settings)



if __name__ == "__main__":
    app = SettingsWindow()
    app.mainloop()
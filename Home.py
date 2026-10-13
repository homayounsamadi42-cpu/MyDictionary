import PIL.Image
import customtkinter
import PIL
import fram
import pickle

with open("set.pkl","rb") as pic:
    data = pickle.load(pic)
customtkinter.set_appearance_mode(data["theme"])
customtkinter.set_default_color_theme(data["color"])
root = customtkinter.CTk()


eng_photo = customtkinter.CTkImage(light_image=PIL.Image.open("icons/eng.png"),size=(250,170))
dari_photo = customtkinter.CTkImage(light_image=PIL.Image.open("icons/dari.png"),size=(250,170))
settin_photo = customtkinter.CTkImage(light_image=PIL.Image.open("icons/settings.png"),size=(80,80))

exit_photo = customtkinter.CTkImage(light_image=PIL.Image.open("icons/exit.png"),size=(80,80))


root.rowconfigure((0,1,2),weight=1)
root.columnconfigure((0,1,2),weight=1)

frame_eng =fram.frame(master= root,img=eng_photo,row=0,column=0,text="English")
frame_eng.placing()
frame_eng.lbl_placing()

frame_dari =fram.frame(master= root,img=dari_photo,row=0,column=1,text="Dari")
frame_dari.placing()
frame_dari.lbl_placing()

frame_settings = fram.frame(master=root,img =settin_photo,row=1,column=0,text="Settings")
frame_settings.placing()
frame_settings.lbl_placing()



frame_exit = fram.frame(master=root,row=1,column=1,img=exit_photo,text="Exit",span=2)
frame_exit.placing()
frame_exit.lbl_placing()

def focus_in(e):
    with open("set.pkl","rb") as pic:
        data = pickle.load(pic)
    customtkinter.set_appearance_mode(data["theme"])
    customtkinter.set_default_color_theme(data["color"])
    
    root.update_idletasks()
root.bind("<FocusIn>",focus_in)
root.mainloop()

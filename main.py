from PIL import ImageTk,Image
from tkinter import Tk,Label,Button,CENTER
import os
import shutil
from tkinter import messagebox

def delete_temp_files_cmd():
    appdata_dir =os.getenv("LOCALAPPDATA")
    temp_dir =appdata_dir +"\\Temp"
    if os.path.exists(temp_dir):
        print("Deleting Temp Files")
        for root, dirs, files in os.walk(temp_dir):
            for f in files:
                try:
                    os.unlink(os.path.join(root, f))
                except:
                    pass                
            for d in dirs:
                try:
                    shutil.rmtree(os.path.join(root, d))
                except:
                    pass
        messagebox.showinfo("Success","Successfully Deleted All Temp Files")

root = Tk(className=" Temp File Deleter")
root.iconbitmap("assets\\icon.ico")
root.geometry("400x300")
background_image=ImageTk.PhotoImage(Image.open("assets\\background.png"))
image_panel=Label(root,image=background_image)
image_panel.pack(fill="both",expand="yes")
redbutton = Button(image_panel, text = 'Delete Temp Files', fg ='red',command=delete_temp_files_cmd)
redbutton.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
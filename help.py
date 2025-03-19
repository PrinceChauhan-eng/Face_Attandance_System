from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text=" HELP  DESK ",font=("new times roman",30,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1024,height=40)

        img_top=Image.open(r'College_Image\help.jpg')
        img_top=img_top.resize((1024,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=42,width=1024,height=700)

        dev_label=Label(f_lbl,text="Email:pc6174544@gmail.com ",font=("times new roman,",20,"bold"),bg="black",fg="red")
        dev_label.place(x=200,y=300)




        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()    
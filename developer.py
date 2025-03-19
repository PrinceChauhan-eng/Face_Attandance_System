from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x768+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text=" DEVELOPER ",font=("new times roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1024,height=40)

        img_top=Image.open(r'College_Image\facialrecognition.jpg')
        img_top=img_top.resize((1024,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=42,width=1024,height=700)

# =============Frame=========================
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=600,y=0,width=400,height=400)

        img_bottom=Image.open(r'College_Image\prince.jpg')
        img_bottom=img_bottom.resize((190,200))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
    
        f_lbl=Label(main_frame,image=self.photoimg_bottom)
        f_lbl.place(x=200,y=0,width=190,height=200)

        #Developer
        dev_label=Label(main_frame,text="Hello my name , Prince",font=("times new roman,",12,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am Python Developer",font=("times new roman,",12,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img1=Image.open(r'College_Image\f.jpg')
        img1=img1.resize((395,195))
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=0,y=200,width=395,height=195)



        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()    
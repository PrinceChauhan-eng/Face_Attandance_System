from datetime import datetime
from tkinter import*
from tkinter import ttk
import tkinter  
from PIL import Image,ImageTk
import os 
from time import strftime
from student import Student
from train import Train
from face_recgonition import Face_recognition
from attendence import Attendence
from developer import Developer
from help import Help

 

class face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x768+0+0")
        self.root.title("Face Recognition System")
        
        
        #First Image
        img=Image.open(r'College_Image\e.jpg')
        img=img.resize((350,150))
        self.photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=150)
        
        #Second Image
        img1=Image.open(r'College_Image\f.jpg')
        img1=img1.resize((350,150))
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=350,y=0,width=350,height=150)
        
        #Third Image
        img2=Image.open(r'College_Image\a.jpg')
        img2=img2.resize((350,150))
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=700,y=0,width=350,height=150)
        
    
        # Bg_img
        img3=Image.open(r'College_Image\g.jpg')
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
    
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1024,height=688)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE ",font=("new times roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1024,height=40)

        # ====================Time==================================
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text= string)
            lbl.after(1000,time)
        
        lbl= Label(title_lbl,font=("times new roman",12,"bold"),background="white",fg="blue")
        lbl.place(x=0,y=0,width=100,height=45)
        time()
        
        
        # Student Button
        img4=Image.open(r'College_Image\p.jpg')
        img4=img4.resize((150,150))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_detail,cursor="hand2")
        b1.place(x=150,y=70,width=150,height=150)
        
        b1=Button(bg_img,text="Student Details",command=self.student_detail,cursor="hand2",font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=150,y=210,width=150,height=30)
        
        
        # Detector button
        img5=Image.open(r'College_Image\Face_detector.jpg')
        img5=img5.resize((150,150))
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=350,y=70,width=150,height=150)
        
        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=350,y=210,width=150,height=30)
        

        # Attendence Face button
        img6=Image.open(r'College_Image\T.jpg')
        img6=img6.resize((150,150))
        self.photoimg6=ImageTk.PhotoImage(img6)
    
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.atten_data)
        b1.place(x=550,y=70,width=150,height=150)
    
        b1=Button(bg_img,text="Attendence",cursor="hand2",command=self.atten_data,font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=550,y=210,width=150,height=30)
        
        
        # Help button
        img7=Image.open(r'College_Image\h.jpg')
        img7=img7.resize((150,150))
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=750,y=70,width=150,height=150)
        
        b1=Button(bg_img,text="Help desk",cursor="hand2",command=self.help_data,font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=750,y=210,width=150,height=30)
        
        
        #Train button
        img8=Image.open(r'College_Image\q.jpg')
        img8=img8.resize((150,150))
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=320,width=150,height=150)
        
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=150,y=450,width=150,height=30)
        
        
        #Photo face button
        img9=Image.open(r'College_Image\l.jpg')
        img9=img9.resize((150,150))
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=350,y=320,width=150,height=150)
        
        b1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=350,y=450,width=150,height=30)
        
        #Developer face button
        img10=Image.open(r'College_Image\r.jpg')
        img10=img10.resize((150,150))
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data,)
        b1.place(x=550,y=320,width=150,height=150)
        
        b1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=550,y=450,width=150,height=30)
        
        
        #Exit button
        img11=Image.open(r'College_Image\o.jpg')
        img11=img11.resize((150,150))
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=750,y=320,width=150,height=150)
        
        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("new times roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=750,y=450,width=150,height=30)



    def open_img(self):
        os.startfile("Data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else:
            return

    
    # =======================Function Button =====================
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
     
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def atten_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
        

        

    
    
     

if __name__=="__main__":
    root=Tk()
    obj=face_Recognition_System(root)
    root.mainloop()    
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
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




def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Login")
        
        
        self.bg=ImageTk.PhotoImage(file=r'College_Image\login.jpg')
        bg_lbl = Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r'College_Image\login.png')
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbl_img1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #labels
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text="Password ",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=258,width=270)

        # =====================Icon IMages======================
        img2=Image.open(r'College_Image\user.png')
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbl_img2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r'College_Image\password.png')
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbl_img3.place(x=650,y=396,width=25,height=25)

        #login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #Register Button
        registerbtn=Button(frame,text="New user Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #Forget Password
        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

# ========================Login Function===================================
    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror('Error','Please fill all the fields',parent=self.root)
        elif self.txtuser.get()=="prince" and self.txtpassword.get()=="1234":
            messagebox.showinfo("Success","Welcome to my Face Recognition attendence System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                                                                    self.txtuser.get(),
                                                                    self.txtpassword.get()
                                                                    ))
            row=my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","Invalid Username anf Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

# ========================================Reset Function==================================================
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Security Question is required")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Answer Field can not be empty")
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("UPDATE register SET password=%s WHERE email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)
                self.root2.destroy()

# ==========================================Forget function=================================================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror('Error','Enter your registered Email id',parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            qurey=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(qurey,value)
            row=my_cursor.fetchall()
            # print(row)

            if row==None:
                messagebox.showerror('Error','Email Id not found',parent=self.root2)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",12,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                security_q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_q.place(x=30,y=60)

                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
                self.combo_security_q.place(x=30,y=90,width=250)
                self.combo_security_q.current(0)

                sec_answ=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                sec_answ.place(x=30,y=130)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=30,y=160,width=250)

                newpass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                newpass.place(x=30,y=200)
                self.txt_newpassword=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpassword.place(x=30,y=230,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",12,"bold"),fg="white",bg="green")
                btn.place(x=130,y=270)

           
class Register:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Register")
        
        # ==================================variables=====================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


# ==================Bg Image================================
        self.bg=ImageTk.PhotoImage(file=r'College_Image\register.jpg')
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

# =====================Left Image===========================
        self.bg1=ImageTk.PhotoImage(file=r'College_Image\regbg.jpg')
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=170,width=470,height=380)


        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=170,width=800,height=380)

# ===========================Lables=======================================
        reg_lbl=Label(frame,text="Register Here ",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        reg_lbl.place(x=10,y=10)

# =============================Labels and Entrys=====================================

        #-----------------------------Row1
        fname=Label(frame,text="First name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=30,y=50)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=30,y=75,width=250)

        lname=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=450,y=50)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=450,y=75,width=250)

        # ----------------------------------------Rows 2
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=30,y=110)
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=30,y=135,width=250)

        phone=Label(frame,text="Phone number",font=("times new roman",15,"bold"),bg="white",fg="black")
        phone.place(x=450,y=110)
        phone_entry=ttk.Entry(frame,textvariable=self.var_phone,font=("times new roman",15,"bold"))
        phone_entry.place(x=450,y=135,width=250)
        # ---------------------------------------Row 3
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=30,y=170)
        pass_entry=ttk.Entry(frame,textvariable=self.var_pass,show='*',font=("times new roman",15,"bold"))
        pass_entry.place(x=30,y=200,width=250)
       
        cpass=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cpass.place(x=450,y=170)
        cpass_entry=ttk.Entry(frame,textvariable=self.var_confpass,show='*',font=("times new roman",15,"bold"))
        cpass_entry.place(x=450,y=200,width=250)
        # --------------------------------------------Row 4
        security_q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_q.place(x=30,y=230)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_q.place(x=30,y=260,width=250)
        self.combo_security_q.current(0)

        sec_answ=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        sec_answ.place(x=450,y=230)
        ans_sec_entry=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
        ans_sec_entry.place(x=450,y=260,width=250)

        # -------------------------------------------Buttons============================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0,background="white")
        checkbtn.place(x=30,y=298)

        # ====================Buttons================================
        img=Image.open(r'College_Image\register button.jpg')
        img=img.resize((80,80))
        self.photoimage=ImageTk.PhotoImage(img)
        registerbutton = Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        registerbutton.place(x=30, y=325,width=260,height=60)


        img1=Image.open(r'College_Image\login_button.jpg')
        img1=img1.resize((80,80))
        self.photoimage1=ImageTk.PhotoImage(img1)
        registerbutton = Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
        registerbutton.place(x=420, y=325,width=260,height=50)

        # =========================Function Declaration==================================================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror('Error','Please Fill All The Fields!')
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror('Error','Passwords Do Not Match!')
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror('Error',"This Email Is Already Registered Please Login Or Try Another One.")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_email.get(),
                                                                                self.var_phone.get(),
                                                                                self.var_pass.get(),
                                                                                self.var_securityQ.get(),
                                                                                self.var_SecurityA.get()

                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Registration Successful')

    def return_login(self):
        self.root.destroy()

        
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
    main()
   
   
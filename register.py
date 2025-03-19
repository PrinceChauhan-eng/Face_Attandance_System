from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



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
        registerbutton = Button(frame, image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white",activebackground="white")
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




      



if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()    



















    
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x768+0+0")
        self.root.title("Face Recognition System")
      
        # ==================Variables=============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_Sem=StringVar()
        self.var_year=StringVar()
        self.var_Std_id=StringVar()
        self.var_Std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
         
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
        
        title_lbl=Label(bg_img,text=" STUDENT MANAGEMENT SYSTEM ",font=("new times roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1024,height=40)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1000,height=480)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=15,y=10,width=480,height=460)
        
        img_left=Image.open(r'College_Image\e.jpg')
        img_left=img_left.resize((460,80))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
    
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=460,height=80)
        
        #Current Course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",10,"bold"))
        current_course_frame.place(x=10,y=80,width=460,height=100)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman,",9,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman,",9,"bold"),state="readonly",width=15)
        dep_combo['value']=("Select Department","Computer Science","IT","Commerce","Mechincal")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman,",9,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman,",9,"bold"),state="readonly",width=15)
        course_combo['value']=("Select Course","FY","SY","TY")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)

        #Year
        Year_label=Label(current_course_frame,text="Year",font=("times new roman,",9,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman,",9,"bold"),state="readonly",width=15)
        Year_combo['value']=("Select Year","2019","2020","2021","2022","2023")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman,",9,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("times new roman,",9,"bold"),state="readonly",width=15)
        Semester_combo['value']=("Select Course","Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)
        
        #Class Student information
        Class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",10,"bold"))
        Class_Student_frame.place(x=10,y=180,width=460,height=250)
        
        #Student ID
        StudentID_label=Label(Class_Student_frame,text="Student ID:",font=("times new roman,",9,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=5,sticky=W)
        Student_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Std_id,font=("times new roman,",9,"bold"),width=15)
        Student_entry.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        
        #Student Name
        Student_Name_label=Label(Class_Student_frame,text="Student Name:",font=("times new roman,",9,"bold"),bg="white")
        Student_Name_label.grid(row=0,column=2,padx=5,sticky=W)
        Student_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Std_name,font=("times new roman,",9,"bold"),width=15)
        Student_entry.grid(row=0,column=3,padx=2,pady=2,sticky=W)
        
        #Class Division
        Class_Division_label=Label(Class_Student_frame,text="Class Division:",font=("times new roman,",9,"bold"),bg="white")
        Class_Division_label.grid(row=1,column=0,padx=5,sticky=W)
        Division_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman,",9,"bold"),width=13)
        Division_combo["values"]=("Select Division","A","B","C")
        Division_combo.current(0)
        Division_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)
        
        #Roll No
        Roll_No_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman,",9,"bold"),bg="white")
        Roll_No_label.grid(row=1,column=2,padx=5,sticky=W)
        Roll_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,font=("times new roman,",9,"bold"),width=15)
        Roll_entry.grid(row=1,column=3,padx=2,pady=2,sticky=W)
        
        #Gender
        Gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman,",9,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=5,sticky=W)
        Gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman,",9,"bold"),width=13)
        Gender_combo["values"]=("Select Gender","Male","Female","Others")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=2,pady=2,sticky=W)
        
        #DOB
        Dob_label=Label(Class_Student_frame,text="DOB:",font=("times new roman,",9,"bold"),bg="white")
        Dob_label.grid(row=2,column=2,padx=5,sticky=W)
        Student_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,font=("times new roman,",9,"bold"),width=15)
        Student_entry.grid(row=2,column=3,padx=2,pady=2,sticky=W)
        
        #Email
        Email_label=Label(Class_Student_frame,text="Email:",font=("times new roman,",9,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=5,sticky=W)
        Student_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,font=("times new roman,",9,"bold"),width=15)
        Student_entry.grid(row=3,column=1,padx=2,pady=2,sticky=W)
        
        #Phone
        Phone_label=Label(Class_Student_frame,text="Phone No:",font=("times new roman,",9,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=5,sticky=W)
        Student_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,font=("times new roman,",9,"bold"),width=15)
        Student_entry.grid(row=3,column=3,padx=2,pady=2,sticky=W)
        
        #Address
        Address_label=Label(Class_Student_frame,text="Address:",font=("times new roman,",9,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=5,sticky=W)
        Student_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,font=("times new roman,",9,"bold"),width=15)
        Student_entry.grid(row=4,column=1,padx=2,pady=3,sticky=W)
        
        #Teacher Name
        Teacher_Name_label=Label(Class_Student_frame,text="Teacher Name:",font=("times new roman,",9,"bold"),bg="white")
        Teacher_Name_label.grid(row=4,column=2,padx=2,sticky=W)
        Student_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,font=("times new roman,",9,"bold"),width=15)
        Student_entry.grid(row=4,column=3,padx=2,pady=2,sticky=W)
        
        #Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)
        
        #Button Frame
        butn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        butn_frame.place(x=2,y=150,width=450,height=30)
        
        save_btn=Button(butn_frame,command=self.add_data,text="Save",width=15,font=("times new roman",8,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(butn_frame,command=self.update_data,text="Update",width=15,font=("times new roman",8,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        Delete_btn=Button(butn_frame,command=self.delete_data,text="Delete",width=15,font=("times new roman",8,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)
        
        Reset_btn=Button(butn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",8,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        
        #Second Button Frame
        butn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        butn_frame1.place(x=2,y=175,width=450,height=26)
        
        Take_photo_btn=Button(butn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=31,font=("times new roman",8,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=1,column=0)
        
        Update_Photo_btn=Button(butn_frame1,text="Update Photo Sample",width=31,font=("times new roman",8,"bold"),bg="blue",fg="white")
        Update_Photo_btn.grid(row=1,column=1)
  
        
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=500,y=10,width=480,height=460)
        
        img_Right=Image.open(r'College_Image\e.jpg')
        img_Right=img_Right.resize((460,80))
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)
    
        f_lbl=Label(Right_frame,image=self.photoimg_Right)
        f_lbl.place(x=10,y=0,width=460,height=80)
        
        
        # ==============SEARCH SYSTEM========================
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,'bold'))
        search_frame.place(x=10,y=80,width=460,height=60)
        
        search_label=Label(search_frame,text="Search By :",font=("times new roman",10,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readyonly",width=10)
        search_combo['value']=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        
        search_entry=Entry(search_frame,relief=RIDGE,font=("times new roman",10,"bold"),width=12)
        search_entry.grid(row=0,column=2,padx=4)
        
        search_btn=Button(search_frame,text="Search",font=("times new roman",10,"bold"),bg="blue",fg="white",width=10)
        search_btn.grid(row=0,column=3,padx=2)
        
        show_btn=Button(search_frame,text="Show All",font=("times new roman",10,"bold"),bg="blue",fg="white",width=10)
        show_btn.grid(row=0,column=4,padx=2)
        
        # ====================Tabel Frame =============================
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 10, "bold"))
        table_frame.place(x=10, y=140, width=460, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "Sem", "Studentid", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("Studentid", text="Student Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("dep",width=80)
        self.student_table.column("course",width=80)
        self.student_table.column("year",width=80)
        self.student_table.column("Sem",width=80)
        self.student_table.column("Studentid",width=80)
        self.student_table.column("name",width=80)
        self.student_table.column("div",width=80)
        self.student_table.column("roll",width=80)
        self.student_table.column("gender",width=80)
        self.student_table.column("dob",width=80)
        self.student_table.column("email",width=80)
        self.student_table.column("phone",width=80)
        self.student_table.column("address",width=80)
        self.student_table.column("teacher",width=80)
        self.student_table.column("photo",width=80)
        

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
# =====================Function Variable==================================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_Std_id.get() == "" or self.var_Std_name.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                       
                                                                                                            
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_Sem.get(),
                                                                                                self.var_Std_id.get(),
                                                                                                self.var_Std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()

                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfuly",parent=self.root)
            except Exception as es :
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 
                
# =====================Fetch Data=============================     
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor() 
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()
            
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                    conn.commit()
            conn.close()
            
# ======================Get Cursor==========================
    def get_cursor(self,event=" "):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),  
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),      
        self.var_Sem.set(data[3]),  
        self.var_Std_id.set(data[4]),  
        self.var_Std_name.set(data[5]),  
        self.var_div.set(data[6]),  
        self.var_roll.set(data[7]),  
        self.var_gender.set(data[8]),  
        self.var_dob.set(data[9]),  
        self.var_email.set(data[10]),  
        self.var_phone.set(data[11]),  
        self.var_address.set(data[12]),  
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])  
        
# =================Update Function=================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_Std_id.get() == "" or self.var_Std_name.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details",parent=self.root)
                if Update > 0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where studentid=%s", (
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_Sem.get(),
                                        self.var_Std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_Std_id.get()
                                      ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)      
                
# ===========================Delete Function===================================
    def delete_data(self):
        if self.var_Std_id.get()=="":
            messagebox.showerror('Warning',"Please Select a Student ID",parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Student delete Page","Do you want to Delete",parent=self.root)
                if Delete > 0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="Delete from Student where Studentid=%s"
                    val=(self.var_Std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deteled Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
# ========================Reset====================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_Sem.set("Select Semester")
        self.var_Std_id.set("")
        self.var_Std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
# ==============Generate Data set or Take Photo Sample=============================
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_Std_id.get() == "" or self.var_Std_name.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id=id+1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where studentid=%s", (
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_Sem.get(),
                                        self.var_Std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        id
                                      ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #===========Load predefined data on face frontals from opnecv===========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor=1.3
                    #minimum Neighbou=5

                    for (x, y, w, h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed !!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


               
    
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()    
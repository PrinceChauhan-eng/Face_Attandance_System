from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x768+0+0")
        self.root.title("Face Recognition System")

        # ====================variables=======================
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_attendence=StringVar()


        #First Image
        img=Image.open(r'College_Image\e.jpg')
        img=img.resize((510,200))
        self.photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=200)
        
        #Second Image
        img1=Image.open(r'College_Image\f.jpg')
        img1=img1.resize((510,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=200)

          
        # Bg_img
        img3=Image.open(r'College_Image\g.jpg')
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
    
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1024,height=688)
        
        title_lbl=Label(bg_img,text=" ATTENDENCE MANAGEMENT SYSTEM ",font=("new times roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1024,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1000,height=480)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        left_frame.place(x=15,y=10,width=480,height=460)

        img_left=Image.open(r'College_Image\e.jpg')
        img_left=img_left.resize((460,80))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
    
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=460,height=80)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=85,width=460,height=300)

        #Label and Entry
        #Attendence ID
        Attendence_ID_label=Label(left_inside_frame,text="Attendence ID:",font=("times new roman,",9,"bold"),bg="white")
        Attendence_ID_label.grid(row=0,column=0,padx=5,sticky=W)

        Attendence_ID=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,font=("times new roman,",9,"bold"),width=15)
        Attendence_ID.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        # Roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman,",9,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=5,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,font=("times new roman,",9,"bold"),width=15)
        atten_roll.grid(row=0,column=3,padx=2,pady=8,sticky=W)

        # Name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman,",9,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=5,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,font=("times new roman,",9,"bold"),width=15)
        atten_name.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        # Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman,",9,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=5,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,font=("times new roman,",9,"bold"),width=15)
        atten_dep.grid(row=1,column=3,padx=2,pady=8,sticky=W)

        # Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman,",9,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=5,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,font=("times new roman,",9,"bold"),width=15)
        atten_time.grid(row=2,column=1,padx=2,pady=8,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman,",9,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=5,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,font=("times new roman,",9,"bold"),width=15)
        atten_date.grid(row=2,column=3,padx=2,pady=8,sticky=W)


        # Attendence
        attendenced_label=Label(left_inside_frame,text="Attendence Status:",font=("times new roman,",9,"bold"),bg="white")
        attendenced_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendence,font=("times new roman,",9,"bold"),width=13)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=8,sticky=W)

        #Button Frame
        butn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        butn_frame.place(x=2,y=150,width=450,height=26)
        
        imp_btn=Button(butn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",8,"bold"),bg="blue",fg="white")
        imp_btn.grid(row=0,column=0)
        
        exp_btn=Button(butn_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",8,"bold"),bg="blue",fg="white")
        exp_btn.grid(row=0,column=1)
        
        updt_btn=Button(butn_frame,text="Update",width=15,font=("times new roman",8,"bold"),bg="blue",fg="white")
        updt_btn.grid(row=0,column=2)
        
        Reset_btn=Button(butn_frame,text="Reset",width=15,command=self.reset_Data,font=("times new roman",8,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=500,y=10,width=480,height=460)

        tabel_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        tabel_frame.place(x=5,y=5,width=460,height=420)
        
# ======================Scroll bar tabel ==============================================

        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.attendenceReportTabel=ttk.Treeview(tabel_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendenceReportTabel.xview)
        scroll_y.config(command=self.attendenceReportTabel.yview)

        self.attendenceReportTabel.heading("id",text="Attendence ID")
        self.attendenceReportTabel.heading("roll", text = "Roll")
        self.attendenceReportTabel.heading("name",text=" Name")
        self.attendenceReportTabel.heading("department", text = "Department")
        self.attendenceReportTabel.heading("time",text='Time')
        self.attendenceReportTabel.heading("date", text='Date')
        self.attendenceReportTabel.heading("attendence",text="Attendence")

        self.attendenceReportTabel["show"]="headings"

        self.attendenceReportTabel.column("id",width=100)
        self.attendenceReportTabel.column('roll', width=70 )
        self.attendenceReportTabel.column('name',width=90)
        self.attendenceReportTabel.column('department', width= 100)
        self.attendenceReportTabel.column('time',width=70)
        self.attendenceReportTabel.column('date',width=70)
        self.attendenceReportTabel.column('attendence',width=70)

      

        self.attendenceReportTabel.pack(fill=BOTH,expand=1)

        self.attendenceReportTabel.bind("<ButtonRelease>",self.getCursor)

# ======================fetch data===============================
    def fetchData(self,rows):
        self.attendenceReportTabel.delete(*self.attendenceReportTabel.get_children())
        for i in rows:
            self.attendenceReportTabel.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.cvs"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export csv
    def exportCsv(self, ):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data to Export!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.cvs"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data has been successfully exported to {os.path.basename(fln)}")
        except Exception as es :
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


# ==========================Get Cursor==================================
    def getCursor(self,event=""):
        cursor_row =self.attendenceReportTabel.focus()
        content=self.attendenceReportTabel.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])

# =========================Reset Data===============================
    def reset_Data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")



        
if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()    
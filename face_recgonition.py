from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 
import os




class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x768+0+0")
        self.root.title("Face Recognition System")

        f_label=Label(self.root,text="FACE RECOGNITION",relief=RIDGE,font=("times new roman",30,"bold"),bg="red",fg="yellow")
        f_label.place(x=0,y=0,width=1024,height=70)
        # First Image

        img_top=Image.open(r'College_Image\facial_recognition.jpg')
        img_top=img_top.resize((510,640))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        s_label=Label(self.root,image=self.photoimg_top)
        s_label.place(x=0,y=70,width=510,height=640)

        #Second Image
        img_bottom=Image.open(r"College_Image\facial_recognition_system.jpg")
        img_bottom=img_bottom.resize((510,640))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        b_label=Label(self.root,image=self.photoimg_bottom)
        b_label.place(x=510,y=70,width=510,height=640)
    
        #Button
        b1_button=Button(b_label,text="Face Recognition",cursor="hand2",font=("times new roman",10,"bold"),bg="white",fg="darkgreen",command=self.face_recog)
        b1_button.place(x=164,y=325,width=174,height=30)

# =================Attendence==================================
    def mark_attendence(self,i,r,n,d):
        with open("Attendence_Record.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]


            for line in myDatalist:
                entry=line.split(",")
                name_list.append(entry[0])

            if(i not in name_list) and (r not in name_list) and (d not in name_list) and (n not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")




# =============Face Recognition===============================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeigbhour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeigbhour)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("Select name from student where studentid="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("Select Roll from student where studentid="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("Select Dep from student where studentid="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("Select studentid from student where studentid="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

            
                if confidence > 77:
                    cv2.putText(img,f"Studentid:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True: 
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


           

if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()    
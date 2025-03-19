from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2 
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text=" Train Data Set ",font=("new times roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1024,height=40)

        img_top=Image.open(r'College_Image\facialrecognition.jpg')
        img_top=img_top.resize((1024,300))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=42,width=1024,height=300)

        #Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_Classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=340,width=1024,height=60)
        
        img_bottom=Image.open(r'College_Image\Face-Recognition.jpg')
        img_bottom=img_bottom.resize((1024,280))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
    
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=400,width=1024,height=280)
        
    def train_Classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  #Gray Scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

# ===================Tain the Classifier and Save=====================================================================================
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces , ids) 
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed!", parent=self.root)
       

                

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()    
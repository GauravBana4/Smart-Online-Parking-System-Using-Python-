import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import mysql.connector

my_w = tk.Tk()
my_w.geometry("500x550")
my_w.title('Car Parking')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Parking Detection System',width=30,font=my_font1)
l1.grid(row=1,column=1,columnspan=14)
l2 = tk.Label(my_w,text='---------------------------------------------------------------------------------------',width=30,font=my_font1)
l2.grid(row=3,column=2,columnspan=4)
#---------------------------------------------------------------------------------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="carparking_python"
)

mycursor = mydb.cursor()

mycursor.execute("select * from carsloat")
records = mycursor.fetchall()


myList = []
for row in records:
    myList.append(row[1])
#------------------------------------------------------------------------------------------------------------
def parksloat():

    col=1
    row=5
   # filename = ["1.jpg", "2.jpg", "2.jpg","1.jpg", "1.jpg", "1.jpg"]
    for f in myList:
        img=Image.open(f)
        img=img.resize((50,90))
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(my_w)
        e1.grid(row=row,column=col)
        e1.image = img
        e1['image']=img
        if(col==5):
            row=row+1
            col=1
        else:
            col=col+1

parksloat()
my_w.mainloop()

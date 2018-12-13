from tkinter import *
import tkinter
import mysql.connector
from tkinter import messagebox
import frame2
import welcome_page
root=tkinter.Tk()
root.geometry("1080x720+0+0")
root['bg']='black'
data=[]
T1= Frame(root,bg="black",width=1200,bd=100)
l1=Label(T1,bg="black",fg="white",text="WELCOME TO CONTROL PANEL",font=("Times New Roman",32),bd=20)
l1.grid(row=1,column=1)
T2= Frame(root,bg="black",width=1200,height= 1000,relief=SUNKEN)
T1.pack()
l2=Label(T2,bg="black",fg="white",text="Login id:",height=2,width=6,font=("Times New Roman",20))
l2.grid(row=1,column=0)
e1=Entry(T2,bg="white",bd=8,width=25,font=('arial',15,'bold'))
e1.grid(row=1,column=1)
l3=Label(T2,bg="black",fg="white",text="Password:",font=("Times New Roman",20))
l3.grid(row=2,column=0)
e2=Entry(T2,bg="white",width=25,font=('arial',15,'bold'),bd=8,show='*')
e2.grid(row=2,column=1)
def  verify():
x=e1.get()
y=e2.get()
e2.delete(0,END)
    e1.delete(0, END)
    db2 = mysql.connector.connect(host="localhost", database="student", user="root", password="123456")
    cur = db2.cursor()
    cmd = "select * from register"
    cur.execute(cmd)
    z=cur.fetchall()
    for i in range(len(z)):
        for j in z[i]:
            data.append(j)
    db2.commit()
    cur.close()
    db2.close()
    if x in data and y in data:
        messagebox.showinfo(message="welcome "+x)
        root.destroy()
        welcome_page.welcome()
    else:
        messagebox.showinfo(message="wrong credential")
def register():
    messagebox.showinfo(message="WELCOME TO REGISTRATION PAGE")
    frame2.Registration_win()
b2=Button(T2,text="Register",font=("Times New Roman",18),command=register)
b2.grid(row=7,column=1)
b1=Button(T2,text="Login",font=("Times New Roman",18),command=verify)
b1.grid(row=6,column=1)
T2.pack()
#b1= Button(T1,text="1",height=1,width=4)
#b1.pack(side=RIGHT)
root.mainloop()


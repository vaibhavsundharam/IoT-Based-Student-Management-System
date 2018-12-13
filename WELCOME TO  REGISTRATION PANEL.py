import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
def Registration_win():

    root1=tkinter.Tk()
    root1.geometry("720x480+0+0")
    root1['bg']="powder blue"

    f11=Frame(root1,height=100,width=450,bd=15,bg="sky blue")
    L11=Label(f11,text="WELCOME TO  REGISTRATION PANEL",bg="sky blue",font=("Times New Roman",28))
    L11.pack(fill=X)
    f11.pack(side=TOP)
    f22=Frame(root1,height=500,width=800,bg="powder blue",bd=60)
    f22.pack()


    L22=Label(f22,text="User Name",font=("Times New Roman",16),bg="powder blue")
    L22.grid(row=3,column=1)
    e22=Entry(f22,bd=10,width=25)
    e22.grid(row=3,column=2)

    L33 = Label(f22, text="Password", font=("Times New Roman", 16),bg="powder blue")
    L33.grid(row=4, column=1)
    e33 = Entry(f22, bd=10, width=25,show='*')
    e33.grid(row=4, column=2)

    L44 = Label(f22, text="Contact Number", font=("Times New Roman", 16),bg="powder blue")
    L44.grid(row=5, column=1)
    e44 = Entry(f22, bd=10, width=25)
    e44.grid(row=5, column=2)

    L55 = Label(f22, text="Email ID", font=("Times New Roman", 16),bg="powder blue")
    L55.grid(row=6, column=1)
    e55 = Entry(f22, bd=10, width=25)
    e55.grid(row=6, column=2)

    def submit():
        name = e22.get()
        password = e33.get()
        contact =e44.get()
        email = e55.get()
        print(name)
        db2 = mysql.connector.connect(host="localhost", database="college", user="root", password="123456")
        cur = db2.cursor()
        cmd = "insert into register(name,password,contact,email_id) values('" + name + "','" + password + "',"+ contact +",'" + email + "')"

        cur.execute(cmd)

        db2.commit()
        cur.close()
        db2.close()

    time.sleep(2)
    root1.destroy()


b11 = Button(f22, text="Submit", font=("Times New Roman", 16), command=submit)
b11.grid(row=8, column=2)
root1.mainloop()

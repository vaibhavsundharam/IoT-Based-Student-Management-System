import tkinter
from tkinter import *
import mysql.connector
import time
root3 = tkinter.Tk()
def call_update():

    root3.geometry("1080x720+0+0")
    root3.title("Update Panel")
    root3['bg'] = "yellow"
    f11 = Frame(root3, height=100, width=400, bd=20, bg='black')
    l11 = Label(f11, text="                                      WELCOME TO UPDATE PANEL                  ",
                font=('Times New Roman', 24), bg="black", fg='white')
    l11.place(x=0, y=10)
    l11.grid(row=0, column=3)
    f11.pack(side=TOP, fill=X)

    f2 = Frame(root3, height=200, width=300, bd=40, bg='yellow')
    l111 = Label(f2, text="Update From", font=('Times New Roman', 24, 'bold'), bg="yellow", fg='black', bd=20)
    l111.grid(row=0, column=4)

    f2.place(x=250, y=100)

    f3 = Frame(root3, height=400, width=600, bg='yellow', bd=40)
    l4 = Label(f3, text='FACULTY', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l4.grid(row=3, column=1)
    e4 = Entry(f3, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e4.grid(row=3, column=3)

    l5 = Label(f3, text='TIME', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l5.grid(row=4, column=1)
    e5 = Entry(f3, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e5.grid(row=4, column=3)
    f3.place(x=50, y=300)

    f2 = Frame(root3, height=200, width=300, bd=40, bg='yellow')
    l111 = Label(f2, text="Update With", font=('Times New Roman', 24, 'bold'), bg="yellow", fg='black', bd=20)
    l111.grid(row=0, column=4)

    f2.place(x=650, y=100)

    f4 = Frame(root3, height=400, width=600, bg='yellow', bd=40)
    l6 = Label(f4, text='FACULTY', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l6.grid(row=3, column=1)
    e6 = Entry(f4, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e6.grid(row=3, column=3)

    l7 = Label(f4, text='TIME', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l7.grid(row=4, column=1)
    e7 = Entry(f4, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e7.grid(row=4, column=3)

    f4.place(x=550, y=300)


def click_update():
    x = e4.get()
    y = e5.get()
    z = e6.get()
    w = e7.get()
    db = mysql.connector.connect(host='localhost', database='student', user='root', password='123456')
    cur = db.cursor()
    cmd = "update time set faculty='" + z + "' where faculty='" + x + "'  "
    cmd1 = "update time set time='" + w + "' where time='" + y + "'  "
    cur.execute(cmd)
    cur.execute(cmd1)
db.commit()
cur.close()
time.sleep(2)
root3.destroy()
b1 = Button(root3, text="SUBMIT", font=('Times New Roman', 18, 'bold'), bg="yellow", fg='black',command=click_update)
b1.place(x=500, y=500)
root3.mainloop()



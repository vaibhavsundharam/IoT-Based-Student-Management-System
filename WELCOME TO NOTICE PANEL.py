import tkinter
from tkinter import *
import mysql.connector
import update
def welcome():
    root2 = tkinter.Tk()
    root2.title("NOTICE PAGE")
    root2.geometry("1080x720+0+0")
    root2['bg'] = 'yellow'
    f1 = Frame(root2, height=100, width=400, bd=20, bg='black')
    l1 = Label(f1, text="                                      WELCOME TO NOTICE PANEL                  ",
               font=('Times New Roman', 24), bg="black", fg='white')
    l1.place(x=0, y=10)
    l1.grid(row=0, column=3)
    f1.pack(side=TOP, fill=X)

    ########################....................#####################################################
    f2 = Frame(root2, height=400, width=600, bg='yellow', bd=40)
    l11 = Label(f2, text='NOTICE SECTION', font=('Times New Roman', 20, 'bold'), bg="yellow")
    l11.grid(row=0, column=2)

    l2 = Label(f2, text='CLASS', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l2.grid(row=1, column=0)
    e22 = Entry(f2, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e22.grid(row=1, column=2)

    l3 = Label(f2, text='NOTICE', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l3.grid(row=2, column=0)
    e33 = Entry(f2, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e33.grid(row=2, column=2)


    f2.place(x=50,y=100)
    #############-------------------------------------##################################################
    f3 = Frame(root2, height=400, width=600, bg='yellow', bd=40)
    l22 = Label(f3, text='TIME-TABLE', font=('Times New Roman', 20, 'bold'), bg="yellow")
    l22.grid(row=0, column=2)
    l2 = Label(f3, text='CLASS', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l2.grid(row=1, column=0)
    e2 = Entry(f3, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e2.grid(row=1, column=2)
    l3 = Label(f3, text='LECTURE', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l3.grid(row=2, column=0)
    e3 = Entry(f3, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e3.grid(row=2, column=2)

    l4 = Label(f3, text='FACULTY', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l4.grid(row=3, column=0)
    e4 = Entry(f3, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e4.grid(row=3, column=2)

    l5 = Label(f3, text='TIME', font=('Times New Roman', 15, 'bold'), bg="yellow", fg='black', bd=20)
    l5.grid(row=4, column=0)
    e5 = Entry(f3, bg="white", bd=8, width=25, font=('arial', 14, 'bold'))
    e5.grid(row=4, column=2)
    f3.place(x=550, y=100)

    f4 = Frame(root2, height=300, width=500, bg='yellow', bd=40)
    l44 = Label(f4, text='UPDATE TIME TABLE', font=('Times New Roman', 20, 'bold'), bg="yellow")
    l44.place(x=0, y=10)

    f4.place(x=100, y=350)

    #######################------------------------------------#######################################
    def time_table():
        cls=e2.get()
        lecture=e3.get()
        faculty=e4.get()
        time=e5.get()
        db=mysql.connector.connect(host='localhost',database='college',user='root',password='123456')
        cur=db.cursor()
        cmd="insert into time (cls,lecture,faculty,time) values('"+cls+"','"+lecture+"','"+faculty+"','"+time+"')"
        cur.execute(cmd)
        db.commit()
        cur.close()
        db.close()
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
    def notice():
        cls=e22.get()
        notice=e33.get()
        e22.delete(0, END)
        e33.delete(0, END)
        db = mysql.connector.connect(host='localhost', database='college', user='root', password='123456')
        cur = db.cursor()
        cmd="update notice set cls='"+cls+"'where id =1"
        cmd1="update notice set notice='"+notice+"'where id =1"
        cur.execute(cmd)
        cur.execute(cmd1)
        db.commit()
        cur.close()
        db.close()
    def updatee():
        update.call_update()

        def student_count():
            db = mysql.connector.connect(host='192.168.43.247', database='student', user='root', password='123456')
            cur = db.cursor()

    cmd = "select * from countt"
    cur.execute(cmd)
    dat = cur.fetchone()
    db.commit()
cur.close()
db.close()
data = dat[1]
print(data)
messagebox.showinfo(title="STUDENT COUNT", message="Total students are " + str(data))
b1 = Button(f3, text="SUBMIT", font=('arial', 14, 'bold'),command=time_table)
b1.grid(row=5, column=2)
b2 = Button(f2, text="SUBMIT", font=('arial', 14, 'bold'),command=notice)
b2.grid(row=4, column=2)
b4 = Button(f4, text="Click to UPDATE", font=('arial', 14, 'bold'),command=updatee)
b4.place(x=50, y=75)
b5 = Button(f4, text="STUDENT COUNT", font=('arial', 14, 'bold'),command=student_count)
b5.place(x=50, y=150)
root2.mainloop()
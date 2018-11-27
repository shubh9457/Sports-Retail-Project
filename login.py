from tkinter import *
from tkinter import messagebox
import sqlite3
from sport_retaill import *

con = sqlite3.connect("test.db")

class login_app:
    def __init__(self):
        self.root = Tk()
        self.root.title("SPORTS CLOTHING RETAIL SHOP")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.state('zoomed')

        Tops = Frame(self.root,bg="powder blue",width = 1200,height=50,relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self.root,width = 900,height=700,relief=SUNKEN)
        f1.pack(side=TOP)

        lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="SPORTS CLOTHING RETAIL SHOP",fg="steel blue",bd=10,anchor=CENTER)
        lblinfo.grid(row=0,column=0)

        self.usrname = StringVar()
        self.pwd = StringVar()

        l1=Label(f1, font=( 'aria' ,16, 'bold' ),text="",fg="steel blue",bd=10,anchor='n')
        l1.grid(row=0,column=0)

        l2= Label(f1, font=( 'aria' ,16, 'bold' ),text="",fg="steel blue",bd=10,anchor='n')
        l2.grid(row=3,column=0)

        l3 = Label(f1, font=( 'aria' ,16, 'bold' ),text="",fg="steel blue",bd=10,anchor='n')
        l3.grid(row=6,column=0)

        lbluser = Label(f1, font=( 'aria' ,16, 'bold' ),text="USERNAME",fg="steel blue",bd=10,anchor='n')
        lbluser.grid(row=9,column=0,padx=10, pady=10)
        txtuser = Entry(f1,font=('ariel' ,16,'bold'), textvariable=self.usrname , bd=6,insertwidth=4,bg="powder blue" ,justify=CENTER)
        txtuser.grid(row=9,column=1,padx=10, pady=10)



        lblpass = Label(f1, font=( 'aria' ,16, 'bold' ),text="PASSWORD",fg="steel blue",bd=10,anchor='n')
        lblpass.grid(row=12,column=0,padx=20, pady=20)
        txtpass = Entry(f1,font=('ariel' ,16,'bold'),show="*", textvariable=self.pwd , bd=6,insertwidth=4,bg="powder blue" ,justify=CENTER)
        txtpass.grid(row=12,column=1,padx=20, pady=20)


        login=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="LOGIN", bg="powder blue",command = self.verify)
        login.grid(row=15, column=0 ,padx=20, pady=20)

        exitw=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue" ,command = self.root.destroy)
        exitw.grid(row=15, column=1 ,padx=20, pady=20)

        self.root.mainloop()

    def verify(self):
        flag = 0

        c= con.cursor()

        for row in c.execute("select username ,password from login"):
            if self.usrname.get() == row[0] and self.pwd.get() == row[1]:
                flag =1
                con.close()
                sports_shop()
        if flag == 0:
            messagebox.showinfo("Incorrect username/password", "Please enter Correct Username and Password")




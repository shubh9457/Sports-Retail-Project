from tkinter import *
from tkinter import messagebox
import sqlite3
from login import *

con = sqlite3.connect("test.db")
cd= con.cursor()
cd.execute("create table if not exists login(username varchar2(40),password varchar(20));")

root = Tk()
root.title("Signup")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.state('zoomed')

Tops = Frame(root,bg="powder blue",width = 1200,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=TOP)

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="SPORTS CLOTHING RETAIL SHOP",fg="steel blue",bd=10,anchor=CENTER)
lblinfo.grid(row=0,column=0)

usrname = StringVar()
pwd = StringVar()

l1=Label(f1, font=( 'aria' ,16, 'bold' ),text="",fg="steel blue",bd=10,anchor='n')
l1.grid(row=0,column=0)

l2= Label(f1, font=( 'aria' ,16, 'bold' ),text="",fg="steel blue",bd=10,anchor='n')
l2.grid(row=3,column=0)

l3 = Label(f1, font=( 'aria' ,16, 'bold' ),text="",fg="steel blue",bd=10,anchor='n')
l3.grid(row=6,column=0)

lbluser = Label(f1, font=( 'aria' ,16, 'bold' ),text="Choose a username",fg="steel blue",bd=10,anchor='n')
lbluser.grid(row=9,column=0,padx=10, pady=10)
txtuser = Entry(f1,font=('ariel' ,16,'bold'), textvariable=usrname , bd=6,insertwidth=4,bg="powder blue" ,justify=CENTER)
txtuser.grid(row=9,column=1,padx=10, pady=10)

lblpass = Label(f1, font=( 'aria' ,16, 'bold' ),text="Choose a password",fg="steel blue",bd=10,anchor='n')
lblpass.grid(row=12,column=0,padx=20, pady=20)
txtpass = Entry(f1,font=('ariel' ,16,'bold'),show="*", textvariable=pwd , bd=6,insertwidth=4,bg="powder blue" ,justify=CENTER)
txtpass.grid(row=12,column=1,padx=20, pady=20)

def inserttodb():
       username = usrname.get()
       password = pwd.get()
       if len(password)>4 and (username or password is not ""):
              cd= con.cursor()
              cd.execute("insert into login (username,password) values (?,?)",[str(username),str(password)])
              con.commit()
              root.destroy()
              login_app()
       else:
              messagebox.showinfo("Error","Please fill in all the fields correctly")

signup=Button(f1,padx=16,pady=8 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Signup", bg="powder blue",command = inserttodb)
signup.grid(row=15, column=0 ,padx=20, pady=20)

exitw=Button(f1,padx=16,pady=8,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue" ,command = root.destroy)
exitw.grid(row=15, column=1 ,padx=20, pady=20)

root.mainloop()

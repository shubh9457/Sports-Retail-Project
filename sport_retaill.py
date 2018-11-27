from tkinter import *
from tkinter import messagebox
import random
import datetime
import sqlite3
from PIL import Image, ImageTk
import time

db = sqlite3.connect('test.db')

class sports_shop:
    def __init__(self):
        cursor = db.cursor()
        db.execute('''CREATE TABLE IF NOT EXISTS SPORTS
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 SHOES nvarchar(20),
                 TSHIRT nvarchar(20),
                 SHORTS nvarchar(20),
                 CAP nvarchar(20),
                 WRIST_BAND nvarchar(20),
                 SOCKS nvarchar(20),
                 COST nvarchar(20),
                 SERVICE_CHARGE nvarchar(20),
                 TAX nvarchar(20),
                 SUBTOTAL nvarchar(20),
                 TOTAL nvarchar(20)
                 );''')

        db.commit()
        
        self.root = Toplevel()
        self.root.title("SPORTS CLOTHING RETAIL SHOP")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.state('zoomed')

        ## Resizable Image

        image = Image.open('5.gif')
        global copy_of_image
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        global label
        label = Label(self.root, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', self.resize_image)

        Tops = Frame(self.root,bg="black",width = 1500,height=50,relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self.root,bg="black",width = 1200,height=700,relief=SUNKEN)
        f1.pack(side=TOP)

        self.f2 = Frame(self.root,bg="black",width = 1200,height=70,relief=SUNKEN)
        self.f2.pack(side=TOP)

        lblinfohead = Label(Tops, font=( 'aria' ,40, 'bold' ),text="SPORTS CLOTHING RETAIL SHOP",fg="steel blue",bg="black",anchor=CENTER)
        lblinfohead.grid(row=0,column=0)
        self.lblinfo = Label(Tops, font=( 'aria' ,30, 'italic'),fg="steel blue",anchor=CENTER,bg='black')
        self.lblinfo.grid(row=1,column=0)

        self.rand = StringVar()
        self.Shoes = StringVar()
        self.TShirt = StringVar()
        self.Shorts = StringVar()
        self.Cap = StringVar()
        self.Subtotal = StringVar()
        self.Total = StringVar()
        self.Service_Charge = StringVar()
        self.Socks = StringVar()
        self.Tax = StringVar()
        self.cost = StringVar()
        self.Wrist_Band = StringVar()

        lblshoes = Label(f1, font=( 'aria' ,26, 'bold' ),text="Shoes",fg="white",bg="black",bd=10,anchor='w')
        lblshoes.grid(row=1,column=0)
        self.txtshoes = Entry(f1,font=('ariel' ,26,'bold'), textvariable=self.Shoes ,insertwidth=4,justify=CENTER)
        self.txtshoes.grid(row=1,column=1)

        lbltshirt = Label(f1, font=( 'aria' ,26, 'bold' ),text="TShirt",fg="white",bg="black",bd=10,anchor='w')
        lbltshirt.grid(row=2,column=0)
        self.txttshirt = Entry(f1,font=('ariel' ,26,'bold'), textvariable=self.TShirt ,insertwidth=4 ,justify=CENTER)
        self.txttshirt.grid(row=2,column=1)

        lblshorts = Label(f1, font=( 'aria' ,26, 'bold' ),text="Shorts",fg="white",bg="black",bd=10,anchor='w')
        lblshorts.grid(row=3,column=0)
        self.txtshorts = Entry(f1,font=('ariel' ,26,'bold'), textvariable=self.Shorts,insertwidth=4 ,justify=CENTER)
        self.txtshorts.grid(row=3,column=1)

        lblcap = Label(f1, font=( 'aria' ,26, 'bold' ),text="Cap",fg="white",bg="black",anchor='w')
        lblcap.grid(row=4,column=0)
        self.txtcap = Entry(f1,font=('ariel' ,26,'bold'), textvariable=self.Cap ,insertwidth=4 ,justify=CENTER)
        self.txtcap.grid(row=4,column=1)

        lblwrist_band = Label(f1, font=( 'aria' ,26, 'bold' ),text="Wrist Band",fg="white",bg="black",bd=10,anchor='w')
        lblwrist_band.grid(row=5,column=0)
        self.txtwrist_band = Entry(f1,font=('ariel' ,26,'bold'), textvariable=self.Wrist_Band ,insertwidth=4 ,justify=CENTER)
        self.txtwrist_band.grid(row=5,column=1)

        lblsocks = Label(f1, font=( 'aria' ,26, 'bold' ),text="Socks",fg="white",bg="black",anchor='w')
        lblsocks.grid(row=0,column=0)
        self.txtsocks = Entry(f1,font=('ariel' ,26,'bold'), textvariable=self.Socks ,insertwidth=4 ,justify=CENTER)
        self.txtsocks.grid(row=0,column=1)

        space_line = Label(f1,text="---------",fg="black",bg="black")
        space_line.grid(column=2,columnspan=1)

        lblreference = Label(f1, font=( 'aria' ,26, 'bold' ),text="Order No.",fg="white",bg="black",bd=10,anchor='w')
        lblreference.grid(row=0,column=3)
        self.txtreference = Label(f1,font=('ariel' ,26,'bold'),fg="steel blue",justify=CENTER,bg="black")
        self.txtreference.grid(row=0,column=4)
        
        lblcost = Label(f1, font=( 'aria' ,26, 'bold' ),text="cost",fg="white",bg="black",anchor='w')
        lblcost.grid(row=1,column=3)
        self.txtcost = Label(f1,font=('ariel' ,26,'bold'),fg="steel blue",justify=CENTER,bg="black")
        self.txtcost.grid(row=1,column=4)

        lblService_Charge = Label(f1, font=( 'aria' ,26, 'bold' ),text="Service Charge",fg="white",bg="black",anchor='w')
        lblService_Charge.grid(row=2,column=3)
        self.txtService_Charge = Label(f1,font=('ariel' ,26,'bold'),fg="steel blue",justify=CENTER,bg="black")
        self.txtService_Charge.grid(row=2,column=4)

        lblTax = Label(f1, font=( 'aria' ,26, 'bold' ),text="Tax",fg="white",bg="black",anchor='w')
        lblTax.grid(row=3,column=3)
        self.txtTax = Label(f1,font=('ariel' ,26,'bold'),fg="steel blue",justify=CENTER,bg="black")
        self.txtTax.grid(row=3,column=4)

        lblSubtotal = Label(f1, font=( 'aria' ,26, 'bold' ),text="Subtotal",fg="white",bg="black",anchor='w')
        lblSubtotal.grid(row=4,column=3)
        self.txtSubtotal = Label(f1,font=('ariel' ,26,'bold'),fg="steel blue",justify=CENTER,bg="black")
        self.txtSubtotal.grid(row=4,column=4)

        lblTotal = Label(f1, font=( 'aria' ,26, 'bold' ),text="Total",fg="white",bg="black",anchor='w')
        lblTotal.grid(row=5,column=3)
        self.txtTotal = Label(f1,font=('ariel' ,26,'bold'),fg="steel blue",justify=CENTER,bg="black")
        self.txtTotal.grid(row=5,column=4)

        #-----------------------------------------buttons------------------------------------------
        space_line = Label(self.f2,text="-",fg="black",bg="black")
        space_line.grid(row=0,columnspan=6)

        btnprice=Button(self.f2,padx=1,pady=0, bd=10 ,fg="white",bg="black",font=('ariel' ,26,'bold'),width=10, text="PRICE",command=self.price)
        btnprice.grid(row=1, column=0)

        space_line = Label(self.f2,text="-",fg="black",bg="black")
        space_line.grid(row=1,column=1,columnspan=1) 

        btnTotal=Button(self.f2,padx=1,pady=0,fg="white",bg="black",font=('ariel' ,26,'bold'),width=10, text="TOTAL",command=self.Ref)
        btnTotal.grid(row=1, column=2)

        space_line = Label(self.f2,text="-",fg="black",bg="black")
        space_line.grid(row=1,column=3,columnspan=1)

        btnreset=Button(self.f2,padx=1,pady=0,fg="white",bg="black",font=('ariel' ,26,'bold'),width=10, text="RESET",command=self.reset)
        btnreset.grid(row=1, column=4)

        space_line = Label(self.f2,text="-",fg="black",bg="black")
        space_line.grid(row=1,column=5,columnspan=1)

        btnexit=Button(self.f2,padx=1,pady=0,fg="white",bg="black",font=('ariel' ,26,'bold'),width=10, text="EXIT",command=self.qexit)
        btnexit.grid(row=1, column=6)

        self.clock()

        self.root.mainloop()

    def resize_image(self,event):
        new_width = event.width
        new_height = event.height
        global copy_of_image
        image = copy_of_image.resize((new_width, new_height))
        global photo
        photo = ImageTk.PhotoImage(image)
        global label
        label.config(image = photo)
        label.image = photo

    def clock(self):
        time = datetime.datetime.now().strftime("Time: %D %H:%M:%S")
        self.lblinfo.config(text=time)
        self.root.after(1000, self.clock) # run itself again after 1000 ms

    def Ref(self):
        cursor = db.cursor()
        Ref = db.execute('SELECT max(ID) FROM SPORTS').fetchone()[0] + 1
        self.rand.set(Ref)

        try :
            coshoes = int(self.Shoes.get())
        except:
            coshoes = 0

        try :
            cotshirt= int(self.TShirt.get())
        except:
            cotshirt= 0

        try :
            coshorts= int(self.Shorts.get())
        except:
            coshorts= 0

        try :
            cocap= int(self.Cap.get())
        except:
            cocap= 0

        try :
            cowristband= int(self.Wrist_Band.get())
        except:
            cowristband= 0

        try :
            cosocks= int(self.Socks.get())
        except:
            cosocks= 0

        if coshoes>0 or cotshirt>0 or coshorts>0 or cocap>0 or cowristband>0 or cosocks>0:
            costofshoes = coshoes*2500
            costoftshirt = cotshirt*1500
            costofshorts = coshorts*1000
            costofcap = cocap*500
            costofwristband = cowristband*300
            costofsocks = cosocks*200

            cost_without_tax = "Rs.",str('%.2f'% (costofshoes +  costoftshirt + costofshorts + costofcap + costofwristband + costofsocks))
            PayTax=((costofshoes +  costoftshirt + costofshorts + costofcap +  costofwristband + costofsocks)*0.18)
            Ser_Charge=((costofshoes +  costoftshirt + costofshorts + costofcap + costofwristband + costofsocks)/99)
            Totalcost=(costofshoes +  costoftshirt + costofshorts + costofcap  + costofwristband + costofsocks)
            Service="Rs.",str('%.2f'% Ser_Charge)
            OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
            PaidTax="Rs.",str('%.2f'% PayTax)

            self.txtreference.config(text = Ref)
            self.txtService_Charge.config(text = Service)
            self.txtcost.config(text = cost_without_tax)
            self.txtTax.config(text = PaidTax)
            self.txtSubtotal.config(text = cost_without_tax)
            self.txtTotal.config(text = OverAllCost)

            cursor = db.cursor()
            db.execute("INSERT INTO SPORTS (SHOES,TSHIRT,SHORTS,CAP,WRIST_BAND,SOCKS,COST,SERVICE_CHARGE,TAX,SUBTOTAL,TOTAL) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",[str(costofshoes),str(costoftshirt),str(costofshorts),str(costofcap),str(costofwristband),str(costofsocks),str(cost_without_tax),str(Service),str(PaidTax),str(cost_without_tax),str(OverAllCost)])
            db.commit()
        else:
            messagebox.showinfo("No items", "Please select at least one item for billing")

    def qexit(self):
        self.root.destroy()

    def reset(self):
        self.rand.set("")
        self.Shoes.set("")
        self.TShirt.set("")
        self.Shorts.set("")
        self.Cap.set("")
        self.Subtotal.set("")
        self.Total.set("")
        self.Service_Charge.set("")
        self.Socks.set("")
        self.Tax.set("")
        self.cost.set("")
        self.Wrist_Band.set("")

    def price(self):
        roo = Tk()
        roo.geometry("300x220+550+600")
        roo.title("Price List")
        lblinfo1 = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo1.grid(row=0, column=0)
        lblinfo2 = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
        lblinfo2.grid(row=0, column=2)
        lblinfo3 = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo3.grid(row=0, column=3)
        lblinfo4 = Label(roo, font=('aria', 15, 'bold'), text="Shoes", fg="steel blue", anchor=W)
        lblinfo4.grid(row=1, column=0)
        lblinfo5 = Label(roo, font=('aria', 15, 'bold'), text="2500", fg="steel blue", anchor=W)
        lblinfo5.grid(row=1, column=3)
        lblinfo6 = Label(roo, font=('aria', 15, 'bold'), text="TShirt", fg="steel blue", anchor=W)
        lblinfo6.grid(row=2, column=0)
        lblinfo7 = Label(roo, font=('aria', 15, 'bold'), text="1500", fg="steel blue", anchor=W)
        lblinfo7.grid(row=2, column=3)
        lblinfo8 = Label(roo, font=('aria', 15, 'bold'), text="Shorts", fg="steel blue", anchor=W)
        lblinfo8.grid(row=3, column=0)
        lblinfo9 = Label(roo, font=('aria', 15, 'bold'), text="1000", fg="steel blue", anchor=W)
        lblinfo9.grid(row=3, column=3)
        lblinfo10 = Label(roo, font=('aria', 15, 'bold'), text="Cap", fg="steel blue", anchor=W)
        lblinfo10.grid(row=4, column=0)
        lblinfo11 = Label(roo, font=('aria', 15, 'bold'), text="500", fg="steel blue", anchor=W)
        lblinfo11.grid(row=4, column=3)
        lblinfo12 = Label(roo, font=('aria', 15, 'bold'), text="Wrist Band", fg="steel blue", anchor=W)
        lblinfo12.grid(row=5, column=0)
        lblinfo13 = Label(roo, font=('aria', 15, 'bold'), text="300", fg="steel blue", anchor=W)
        lblinfo13.grid(row=5, column=3)
        lblinfo14 = Label(roo, font=('aria', 15, 'bold'), text="Socks", fg="steel blue", anchor=W)
        lblinfo14.grid(row=6, column=0)
        lblinfo15 = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
        lblinfo15.grid(row=6, column=3)

        roo.mainloop()


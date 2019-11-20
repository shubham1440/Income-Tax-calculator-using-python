from tkinter import *
import sqlite3
from tkinter import messagebox
import os
def adminlog():
    ad=Tk()
    ad.title("Admin Screen")
    ad.attributes('-fullscreen',True)
    adwelcome1=Label(ad,text='Welcome to')
    adwelcome2=Label(ad,text='Income Tax Calculator')
    adwelcome1.config(font=('Sans-serif',24,'bold'))
    adwelcome2.config(font=('Script-typeface',30,'bold'))
    adwelcome1.pack()
    adwelcome2.pack()
def default():
        messagebox.showwarning("Reset","Admin and Password reset to default for more ask the developer")
        con=sqlite3.connect("CMS.db")
        c=con.cursor()
        c.execute('delete from admin where AID="%s"'%("admin"))
        c.execute('select * from admin')
        if c.fetchone() is None:
            c.execute('insert into admin(AID,Password) values("%s","%s")'%("admin","Admin@123"))
        con.commit()
        con.close()
        forgot=Button(ad,text="Reset Password",command= default)
        forgot.place(relx=.45,rely=.50,anchor=CENTER)
        submit=Button(ad,text="Login",command= onsubmit)
        submit.place(relx=.55,rely=.50,anchor=CENTER)
        ad.mainloop()

def taxamount1(income):
    totalamount=0
    tax=0
    try:
        if income<=0:
            raise NameError("Hi there")
    except NameError:
            print("bsk error ha ")
    if income <= 500000:
        tax = 0
        print("reached 2")
    elif income <= 1000000:
        tax = 12500 + (income) * 0.20
        print("reached 3")
    elif income >= 1000001:
        tax = 112500 + (income) * 0.30
    else:
        tax = 12500+100000+(income - 1000000)* 0.3
    totalamount=tax
    return totalamount
def taxamount2(income):
    totalamount=0
    tax=0
    try:
        if income<=0:
            raise NameError("Hi there")
    except NameError:
            print("bsk error ha ")
    if income <= 500000:
        tax = 0
        print("reached 2")
    elif income <= 1000000:
        tax = 10000 + (income) * 0.20
        print("reached 3")
    elif income >= 1000001:
        tax = 110000 + (income) * 0.30
    else:
        tax = 12500+100000+(income - 1000000)* 0.3
    totalamount=tax
    return totalamount
def taxamount3(income):
    totalamount=0
    tax=0
    try:
        if income<=0:
            raise NameError("Hi there")
    except NameError:
            button7 = Button(root,text="bsk error ha ",command=button3)
    if income <= 500000:
        tax = 0
        print("reached 2")
    elif income <= 1000000:
        tax =(income) * 0.20
        print("reached 3")
    elif income >= 1000001:
        tax = 100000 + (income) * 0.30
    else:
        tax = 12500+100000+(income - 1000000)* 0.3
        totalamount=tax
        return totalamount

def button1():
    income=IntVar()
    income=incomefield.get()
    amount = taxamount1(int(income))
    print(amount)
    gettax = Label(root,text="Tax")
    gettax.place(x=90,y=200,anchor=CENTER)
    entry = StringVar()
    entryField = Entry(root,textvariable=entry,background="LightYellow2",foreground="blue4",justify=CENTER)
    # entryField.grid(row=0,column=0,columnspan=2,sticky=W + E)
    entryField.place(x=200,y=200,anchor=CENTER)
    # entryField.columnconfigure(0,weight=1)
    entry.set(str(amount))
def button2():
    income=IntVar()
    income=incomefield.get()
    amount = taxamount2(int(income))
    print(amount)
    gettax = Label(root,text="Tax")
    gettax.place(x=90,y=200,anchor=CENTER)
    entry = StringVar()
    entryField = Entry(root,textvariable=entry,background="LightYellow2",foreground="blue4",justify=CENTER)
    # entryField.grid(row=0,column=0,columnspan=2,sticky=W + E)
    entryField.place(x=200,y=200,anchor=CENTER)
    # entryField.columnconfigure(0,weight=1)
    entry.set(str(amount))
def button3():
    income=IntVar()
    income=incomefield.get()
    amount = taxamount3(int(income))
    print(amount)
    gettax = Label(root,text="Tax")
    gettax.place(x=90,y=200,anchor=CENTER)
    entry = StringVar()
    entryField = Entry(root,textvariable=entry,background="LightYellow2",foreground="blue4",justify=CENTER)
    # entryField.grid(row=0,column=0,columnspan=2,sticky=W + E)
    entryField.place(x=200,y=200,anchor=CENTER)
    # entryField.columnconfigure(0,weight=1)

    entry.set(str(amount))


root=Tk()
root.geometry("400x400")
#root.configure(background="blue4")
root.title("income Tax Calculator")
#root.columnconfigure(0,weight=1)
#root.columnconfigure(1,weight=1)

#labelincome = Label(root,text="INCOME",background="black",foreground="PaleTurquoise1")
labelincome = Label(root,text="INCOME")
labelincome.config(font=('Script-typeface',30,'bold'))
labelincome.place(x=200,y=50,anchor=CENTER)
enterincome = Label(root,text="Enter Income")
enterincome.place(x=90,y=150,anchor=CENTER)
incomefield = Entry(root,background="SkyBlue2",foreground="blue4")
incomefield.place(x=200,y=150,anchor=CENTER)
button11 = Button(root,text="Young People",command=button1)
button11.place(x=70,y=175,anchor=CENTER)
button22 = Button(root,text="Senior Citizen",command=button2)
button22.place(x=200,y=175,anchor=CENTER)
button33 = Button(root,text="Very Senior Citizen",command=button3)
button33.place(x=330,y=175,anchor=CENTER)
con=sqlite3.connect("main.db")
c=con.cursor()
c.execute('create table if not exists user(firstname varchar(20),lastname varchar(20))')
root.mainloop()

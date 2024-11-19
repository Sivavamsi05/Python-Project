#banking
from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
class LogDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("banking")
        self.root.geometry("400x400")
        self.root.config(bg="pink")
        b1=Button(text="registration",bg="white",fg="red",font=("bold",20),command=self.registration)
        b1.place(x=100,y=100)
        b2=Button(text="deposit",bg="white",fg="red",font=("bold",20),command=self.deposit)
        b2.place(x=100,y=200)
        b3 = Button(text="withdraw", bg="white", fg="red", font=("bold", 20),command=self.withdraw)
        b3.place(x=100, y=300)
    def registration(self):
        self.registration=Tk()
        self.registration.title("registration")
        self.registration.geometry("400x400")
        self.registration.config(bg="green")
        title=Label(self.registration,text="registartion",bg="black",fg="pink",font=("bold",20))
        title.pack()
        username=Label(self.registration,text="username",bg="pink",fg="red",font=("bold",15))
        username.place(x=20,y=90)
        self.username_entry=Entry(self.registration,font=("bold",15))
        self.username_entry.place(x=170,y=90)
        accountno=Label(self.registration,text="accountno",bg="pink",fg="red",font=("bold",15))
        accountno.place(x=20, y=160)
        self.accountno_entry = Entry(self.registration, font=("bold", 15))
        self.accountno_entry.place(x=170, y=160)
        minimumbal=Label(self.registration,text="minimumbal",bg="pink",fg="red",font=("bold",15))
        minimumbal.place(x=20, y=220)
        self.minimumbal_entry = Entry(self.registration, font=("bold", 15))
        self.minimumbal_entry.place(x=170, y=220)
        submit=Button(self.registration,text="submit",bg="pink",fg="red",font=("bold",15),command=self.registration)
        submit.place(x=150,y=300)
        self.registration.mainloop()

    def regis(self):
        mydb = mysql.connector.connect(host="localhost", port=3306, database="sss", user="root",password="May5@1222")
        mycur = mydb.cursor()
        name = self.username_entry.get()
        accountno = int(self.accountno_entry.get())
        minimumbal=int(self.minimumbal_entry.get())
        mycur.execute("insert into aaa (name,accountno,minimumbal) values (%s, %s, %s)",(name,accountno,minimumbal))
        mydb.commit()
    def deposit(self):
        self.deposit=Tk()
        self.deposit.title("registration")
        self.deposit.geometry("400x400")
        self.deposit.config(bg="green")
        title=Label(self.deposit,text="deposit",bg="black",fg="pink",font=("bold",20))
        title.pack()
        username=Label(self.deposit,text="username",bg="pink",fg="red",font=("bold",15))
        username.place(x=20,y=90)
        self.username_entry=Entry(self.deposit,font=("bold",15))
        self.username_entry.place(x=140,y=90)
        accountno=Label(self.deposit,text="accountno",bg="pink",fg="red",font=("bold",15))
        accountno.place(x=20, y=160)
        self.accountno_entry = Entry(self.deposit, font=("bold", 15))
        self.accountno_entry.place(x=140, y=160)
        depositmoney=Label(self.deposit,text="depositmoney",bg="pink",fg="red",font=("bold",15))
        depositmoney.place(x=20, y=220)
        self.depositmoney_entry = Entry(self.deposit, font=("bold", 15))
        self.depositmoney_entry.place(x=140, y=230)
        submit=Button(self.deposit,text="submit",bg="pink",fg="red",font=("bold",15),command=self.deposit)
        submit.place(x=150,y=300)
        self.deposit.mainloop()
    def depos(self):
        mydb = mysql.connector.connect(host="localhost", port=3306, database="sss", user="root",password="May5@1222")
        mycur = mydb.cursor()
        name = self.username_entry.get()
        accountno = int(self.accountno_entry.get())
        depositmoney=int(self.depositmoney_entry.get())
        mycur.execute("update aaa set deposite=%s where name = %s",
                      (int(self.depositmoney_entry.get()), self.username_entry.get()))

        mycur.execute("update aaa set minimumbal = minimumbal+%s where name = %s AND accountnumber = %s",
                      (depositmoney, name, accountno))
        mydb.commit()
    def withdraw(self):
        self.withdraw=Tk()
        self.withdraw.title("registration")
        self.withdraw.geometry("400x400")
        self.withdraw.config(bg="green")
        title=Label(self.withdraw,text="deposit",bg="black",fg="pink",font=("bold",20))
        title.pack()
        username=Label(self.withdraw,text="username",bg="pink",fg="red",font=("bold",15))
        username.place(x=20,y=90)
        self.username_entry = Entry(self.withdraw, font=("bold", 15))
        self.username_entry.place(x=140, y=90)
        accountno=Label(self.withdraw,text="accountno",bg="pink",fg="red",font=("bold",15))
        accountno.place(x=20, y=160)
        self.accountno_entry = Entry(self.withdraw, font=("bold", 15))
        self.accountno_entry.place(x=140, y=160)
        withdraw=Label(self.withdraw,text="withdraw",bg="pink",fg="red",font=("bold",15))
        withdraw.place(x=20, y=220)
        self.withdraw_entry = Entry(self.withdraw, font=("bold", 15))
        self.withdraw_entry.place(x=140, y=230)
        submit=Button(self.withdraw,text="submit",bg="pink",fg="red",font=("bold",15),command=self.withdraw)
        submit.place(x=150,y=300)
        self.withdraw.mainloop()
    def withd(self):
        mydb = mysql.connector.connect(host="localhost", port=3306, database="sss", user="root",password="May5@1222")
        mycur = mydb.cursor()
        name = self.username_entry.get()
        accountno = int(self.accountno_entry.get())
        withdraw=int(self.withdraw_entry.get())
        mycur.execute("update aaa set withdraw=%s where name = %s",
                      (int(self.withdraw_entry.get()), self.username_entry.get()))

        mycur.execute("update aaa set minimumbal = minimumbal-%s where name = %s AND accountno = %s",
                      (withdraw, name, accountno))
        mydb.commit()
        c=0
        for i in mycur:
            c=c+1
        if c>=0:
            msg.showinfo("success","withdraw money")
        else:
            msg.showinfo("failed","no withdraw money")




root=Tk()
l=LogDetails(root)
root.mainloop()
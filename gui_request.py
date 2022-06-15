import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
#import gui_ordering


import gui_main


def warning():
    messagebox.showwarning("warning", "בקשתך לא התקבלה\nישנה בעיה בתוכן שהוזן")
def f(x):
    return {
        '1': "SELECT id\
                 FROM 'Workers' \
                 WHERE job =cleaner OR job = lifeguard\
                 EXCEPT\
                 SELECT T.id\
                 FROM (SELECT * \
                 FROM 'Cleaners'\
                  UNION\
                  SELECT * \
                  FROM 'Lifeguards') T",

        '2': "SELECT T.clientsID\
                 FROM (SELECT o.code, co.objectCode, co.clientID,o.isBroken \
                 FROM 'Object' o, 'Clients-Object' co\
                 WHERE o.code = co.objectCode AND o.isBroken = 1) T",

        '3': "SELECT T.id\
                 FROM (SELECT l.lockerNum, l.usReserved, c.lockerNum, c.id \
                 FROM 'Locker' l NATURAL JOIN 'Clients' c\
                 WHERE isReserved = 1) T",

        "4":"(SELECT Date FROM Shift WHERE workerID =10) EXCEPT (SELECT Date FROM Shift WHERE workerID =11)",
        "5" : "SELECT firstName,lastName,id FROM Clients",
        "6" : "SELECT id,name FROM Workers",

        "7" : "CREATE VIEW ObjectCostumer\
          AS  select distinct Clients.firstName AS Name\
          ,Clients.lastName AS LastName,\
          Visitors.visitDay AS Date,\
          Objects.kind AS Object \
          from ((Visitors join Clients on(Visitors.id = Clients.id))\
           join Objects) where Visitors.id = Clients.id and Visitors.objectCode = Objects.code\
            group by Clients.firstName,\
            Clients.lastName,Visitors.visitDay"
    }[x]

def sql_query(mydb,q):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def makerom(root):
    temp = ["1 Customers who ordered more than 2 unbroken items?",
            "2 Are there broken chairs?",
            "3 Did a customer order a saved locker?",
            "4 Days when employee 10 worked when employee 11 did not work",
            "5 all clients",
            "6 all workers",
            "7 create view"]

    # cmb = ttk.Combobox(root, width="10", values=("prova", "ciao", "come", "stai"))
    query_choosen = ttk.Combobox(root, width=27, values=tuple(temp))

    # Adding combobox drop down list
    # personChoosen['values']=tuple(temp)
    def checkcmbo():
        query = query_choosen.get()
        #mast.destroy()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="id18704423_resortvillagepool"
        )
        mycursor = mydb.cursor()
        sql = f(query[0])
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        datastr=""
        for x in myresult:
            #datastr+="1"
            datastr=datastr+str(list(x))+"\n"
        messagebox.showinfo('data', datastr)
       # T = Text(root, height=5, width=52)

        #T.insert(tk.END, myresult)
    query_choosen.current(0)
    query_choosen.pack()
    btn = ttk.Button(root, text="הכנס בקשה", command=checkcmbo)
    btn.pack()




def add_req():
    root = tk.Tk()
    root.geometry("600x300")
    root.resizable(False, False)
    root.title('שאילתות')
    signin = tk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)

    #root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.RIGHT, padx=5, pady=5)
    ents = makerom(root)
    # Adding combobox drop down list
    # personChoosen['values']=tuple(temp)

    root.mainloop()

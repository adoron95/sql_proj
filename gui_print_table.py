import tkinter as tk

from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
import mysql.connector
fields = []




def makeform(table):
    tree = tk.Tk()
    tree.geometry("500x500")
    tree.resizable(False, False)
    tree.title('הוספת נתונים')
    signin = tk.Frame(tree)
    signin.pack(padx=10, pady=10, fill='x', expand=False)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="id18704423_resortvillagepool"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from " + table + "")
    result = mycursor.fetchall()
    num_fields = len(mycursor.description)
    fields = [i[0] for i in mycursor.description]

    entries = []
    for field in fields:
        row = tk.Frame(tree)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    #tree.bind('<Return>', (lambda event, e=entries: fetch(e, table)))
    b1 = tk.Button(tree, text='אישור',
                    command=(lambda e=entries: fetch(e, table)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    #return entries


def fetch( table):

    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="id18704423_resortvillagepool"
        )
    mycursor = mydb.cursor()

    sql = "SELECT * FROM "+table

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    datastr = ""
    for x in myresult:
        # datastr+="1"
        datastr = datastr + str(list(x)) + "\n"
    messagebox.showinfo('data', datastr)


    print(mycursor.rowcount, "record inserted.")

def warning():
    messagebox.showwarning("warning", "בקשתך לא התקבלה\nישנה בעיה בתוכן שהוזן")


def combox(root):
    temp = ['Cleaners', 'Clients', 'Department', 'HotProducts', 'Lifeguards', 'Locker', 'Objects'
        , 'ProductReceipt', 'Products', 'Receipt', 'Shift', 'Specials', 'Visitors', 'Workers']

    update_data = ttk.Combobox(root, width=27, values=tuple(temp))

    def checkcmbo():
        table_name= update_data.get()
        #makeform(table_name)
        fetch(table_name)
    update_data.current(0)
    update_data.pack()
    btn = ttk.Button(root, text="print", command=checkcmbo)
    btn.pack()


def print_db():
    root = tk.Tk()
    root.geometry("400x200")
    root.resizable(False, False)
    root.title('print')
    signin = tk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)

    combox(root)

    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()


import tkinter as tk

from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
import mysql.connector
fields = []


class add_data:
    def __init__(self):
        self.data = {}
        self.key = " "

    def append(self, data):
        self.key = data[0]
        for field in range(data):
            self.man["fname"] = data[1]

    def write_data(self):
        a=1

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


def fetch(entries, table):

    data = []
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        data.append(text)
        print('"%s"' % (text))
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="id18704423_resortvillagepool"
        )
    mycursor = mydb.cursor()
    s="("
    for i in range(len(data)):
        if i != len(data)-1:
            s+='%s, '
        else: s+='%s)'

    mycursor.execute("select * from " + table + "")
    result = mycursor.fetchall()
    num_fields = len(mycursor.description)
    fields = [i[0] for i in mycursor.description]
    str_fields=" ("
    for i in range(len(fields)):
        if i != len(fields) - 1:
            str_fields += fields[i]+', '
        else:
            str_fields += fields[i]+')'
    tuple_data= tuple(data)
    #tuple_s= tuple(s)
    sql = "INSERT INTO "+table +str_fields+" VALUES "+s
    val = tuple(tuple_data)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def warning():
    messagebox.showwarning("warning", "בקשתך לא התקבלה\nישנה בעיה בתוכן שהוזן")


def combox(root):
    temp = ['Cleaners', 'Clients', 'Department', 'HotProducts', 'Lifeguards', 'Locker', 'Objects'
        , 'ProductReceipt', 'Products', 'Receipt', 'Shift', 'Specials', 'Visitors', 'Workers']

    update_data = ttk.Combobox(root, width=27, values=tuple(temp))
    #update_data.current(0)
    #update_data.pack()
    def checkcmbo():
        table_name= update_data.get()
        makeform(table_name)

    update_data.current(0)
    update_data.pack()
    btn = ttk.Button(root, text="הוסף נתונים", command=checkcmbo)
    btn.pack()


def add_to_db():
    root = tk.Tk()
    root.geometry("400x200")
    root.resizable(False, False)
    root.title('הוספת נתונים')
    signin = tk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)

    #ents = makerom(root)

    combox(root)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()


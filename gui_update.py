import tkinter as tk
from tkinter import ttk, messagebox

from tkinter import *

import mysql



def makeform(table):
    tree = tk.Tk()
    tree.geometry("450x300")
    tree.resizable(False, False)
    tree.title('עדכון נתונים')
    signin = tk.Frame(tree)
    signin.pack(padx=10, pady=10, fill='x', expand=False)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="id18704423_resortvillagepool"
    )

    mycursor = mydb.cursor()
    sqlStatement = "SHOW keys FROM " + table + " WHERE Key_name = 'PRIMARY'"

    mycursor.execute(sqlStatement)
    primaryKeys = mycursor.fetchall()
    if primaryKeys==[]:
        tree.destroy()
        warning()
        return
    entries=[]
    primaryKey=primaryKeys[0][4]
    fields = [primaryKey,'field','update']
    for field in fields:
        row = tk.Frame(tree)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))

    # tree.bind('<Return>', (lambda event, e=entries: fetch(e, table)))
    b1 = tk.Button(tree, text='אישור',
                   command=(lambda e=entries: fetch(e, table,primaryKey)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    # return entries


def fetch(entries, table,key):
    """

    :param entries: key,update,field
    :param table:
    :param key:
    :return:
    """
    data = []
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        data.append(text)
        print('"%s"' % (text))
    if data[2]==key:
        messagebox.showerror('error',"אי אפשר לעדכן מפתח")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="id18704423_resortvillagepool"
    )
    mycursor = mydb.cursor()

    sql = "UPDATE "+table+" SET "+data[1]+" = %s WHERE " +key+" = %s "

    update_data = (data[2], data[0])
    mycursor.execute(sql,update_data)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")


def warning():
    messagebox.showwarning("warning", "בקשתך לא התקבלה\nעדכון נתון זה מתבזעת מטבלה אחרת")


def combox(root):
    temp = ['Cleaners', 'Clients', 'Department', 'HotProducts', 'Lifeguards', 'Locker', 'Objects'
        , 'ProductReceipt', 'Products', 'Receipt', 'Shift', 'Specials', 'Visitors', 'Workers']

    table_ = ttk.Combobox(root, width=27, values=tuple(temp))

    def checkcmbo():
        table_name = table_.get()
        makeform(table_name)

    table_.current(0)
    table_.pack()
    btn = ttk.Button(root, text="עדכון נתונים", command=checkcmbo)
    btn.pack()


def update_db():
    root = tk.Tk()
    root.geometry("400x200")
    root.resizable(False, False)
    root.title('עדכון נתונים')
    signin = tk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)
    combox(root)

    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

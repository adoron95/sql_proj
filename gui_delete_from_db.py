import tkinter as tk
from tkinter import ttk, messagebox


import mysql


def makeform(table):
    tree = tk.Tk()
    tree.geometry("500x500")
    tree.resizable(False, False)
    tree.title('מחיקת נתונים')
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
    primaryKey=primaryKeys[0][4]
    row = tk.Frame(tree)
    lab = tk.Label(row, width=15, text=primaryKey, anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    entries = [primaryKey, ent]
    # tree.bind('<Return>', (lambda event, e=entries: fetch(e, table)))
    b1 = tk.Button(tree, text='אישור',
                   command=(lambda e=entries: fetch(e, table,primaryKey)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    # return entries


def fetch(entries, table,key):
    data = []

    field = entries[0]
    text = entries[1].get()
    data.append(text)
    print('"%s"' % (text))
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="id18704423_resortvillagepool"
    )
    mycursor = mydb.cursor()

    sql = "DELETE FROM " + table + " WHERE " + key + " = " + text

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")


def warning():
    messagebox.showwarning("warning", "בקשתך לא התקבלה\nמחיקת נתון זה מתבזעת מטבלה אחרת")


def combox(root):
    temp = ['Cleaners', 'Clients', 'Department', 'HotProducts', 'Lifeguards', 'Locker', 'Objects'
        , 'ProductReceipt', 'Products', 'Receipt', 'Shift', 'Specials', 'Visitors', 'Workers']

    table_ = ttk.Combobox(root, width=27, values=tuple(temp))

    def checkcmbo():
        table_name = table_.get()
        makeform(table_name)

    table_.current(0)
    table_.pack()
    btn = ttk.Button(root, text="מחק נתונים", command=checkcmbo)
    btn.pack()


def delete_from_db():
    root = tk.Tk()
    root.geometry("400x200")
    root.resizable(False, False)
    root.title('מחיקת נתונים')
    signin = tk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)
    combox(root)

    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

import mysql.connector
from tkinter import ttk
import tkinter as tk

import gui_print_table
import gui_request
import gui_add_to_db as adding_data
import gui_delete_from_db as del_element_from_table
import gui_update

def gui_main():
    root = tk.Tk()
    root.geometry("600x300")
    root.resizable(False, False)
    root.title('בסנת')
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=False)

    label = ttk.Label(signin, text="מיני פרוייקט")
    label.pack(fill='y', expand=True)

    login_button = ttk.Button(signin, text="שאילתות", command=gui_request.add_req)
    login_button.pack(fill='y', expand=True, pady=10)


    add_gard_button = ttk.Button(signin, text="הוסף נתונים", command=adding_data.add_to_db)
    add_gard_button.pack(fill='y', expand=True, pady=30)

    delete_gard_button = ttk.Button(signin, text="מחק נתונים", command=del_element_from_table.delete_from_db)
    delete_gard_button.pack(fill='y', expand=True, pady=0)

    update_button = ttk.Button(signin, text="update", command=gui_update.update_db)
    update_button.pack(fill='y', expand=True, pady=10)

    print_button = ttk.Button(signin, text="print", command=gui_print_table.print_db)
    print_button.pack(fill='y', expand=True, pady=10)

    root.mainloop()


#    print("The Max val is " + str(maxHeap.extractMax()))
if __name__ == "__main__":

    gui_main()

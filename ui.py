import psycopg2
import tkinter as tk
from tkinter import ttk
import backend

def get_selected(event):
    global selected_row
    index = list.curselection()[0]
    selected_row = list.get(index)
    title.delete(0, tk.END)
    title.insert(0, selected_row[1])
    author.delete(0, tk.END)
    author.insert(0, selected_row[2])
    year.delete(0, tk.END)
    year.insert(0, selected_row[3])
    isbn.delete(0, tk.END)
    isbn.insert(0, selected_row[4])

def view_command():
    list.delete(0, tk.END)
    data = backend.view()
    for d in data:
        list.insert(tk.END, d)

def search_command():
    list.delete(0, tk.END)
    data = backend.search(tl.get(), aut.get(), yr.get(), num.get())
    for d in data:
        list.insert(tk.END, d)

def add_command():
    backend.insert(tl.get(), aut.get(), yr.get(), isbn.get())
    list.delete(0, tk.END)
    list.insert(tk.END, (tl.get(), aut.get(), yr.get(), isbn.get()))

def delete_command():
    backend.delete(selected_row[0])
    view_command()

def update_command():
    backend.update(selected_row[0], selected_row[1], selected_row[2], selected_row[3], selected_row[4])
    view_command()

root = tk.Tk()
root.title("Bookstore")


mainframe = ttk.Frame(root)

#Title
tl = tk.StringVar()
ttk.Label(root, text="Title").grid(row=0, column=0)
title = ttk.Entry(root, textvariable = tl)
title.grid(row=0,column=1)


#Author
aut = tk.StringVar()
ttk.Label(root, text="Author").grid(row=0, column=2)
author = ttk.Entry(root, textvariable=aut)
author.grid(row=0,column=3)


#Year
yr = tk.StringVar()
ttk.Label(root, text="Year").grid(row=1, column=0)
year = ttk.Entry(root, textvariable = yr)
year.grid(row=1,column=1)

#ISBN
num = tk.StringVar()
ttk.Label(root, text="ISBN").grid(row=1,column=2)
isbn = ttk.Entry(root, textvariable = num)
isbn.grid(row=1,column=3)

#list
list = tk.Listbox(root)
list.grid(row=2, column=0,rowspan=6, columnspan=2)
scr = tk.Scrollbar(root)
scr.grid(row=2,column=2, rowspan=6)

list.configure(yscrollcommand=scr.set)
scr.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected)

#buttons
b1 = ttk.Button(root, text="View All", width=12, command=view_command).grid(row=2, column=3)
b2 = ttk.Button(root, text="Search Entry", width=12, command=search_command).grid(row=3, column=3)
b3 = ttk.Button(root, text="Add Entry", width=12, command=add_command).grid(row=4, column=3)
b4 = ttk.Button(root, text="Update", width=12, command=update_command).grid(row=5, column=3)
b5 = ttk.Button(root, text="Delete", width=12, command=delete_command).grid(row=6, column=3)
b6 = ttk.Button(root, text="Close", width=12).grid(row=7, column=3)



root.mainloop()

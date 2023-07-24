from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

clicks = 0
new_name = ""
name_list = []

def click_button():
    global new_name
    new_name = entry.get()
    name_list.append(new_name)
    entry.delete(0, END)
    entry.insert(0, "Вывожу список")
    for i in name_list:
        print(i)

def add_new():
    global new_name
    new_name = entry.get()
    name_list.append(new_name)
    entry.delete(0, END)


root = Tk()
root.title("Турнирная сетка")
root.geometry("250x200")

entry = ttk.Entry()
entry.pack(padx=6, pady=6)

btn_stop = ttk.Button(text="Стоп", command=click_button)
btn_stop.pack()
btn_add = ttk.Button(text="Добавить", command=add_new)
btn_add.pack()

root.mainloop()


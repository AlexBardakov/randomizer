from tkinter import *
from tkinter import ttk
import keyboard
import random

new_name = ""  # переменная для нового имени
name_list = []  # итоговый список имен


def enter_press():
    add_new()


def stop_button():
    global new_name
    new_name = entry.get()
    name_list.append(new_name)
    entry.delete(0, END)
    lbox.delete(0, END)
    entry.insert(0, "Вывожу список")
    btn_stop["state"] = "disabled"
    for i in name_list:
        lbox.insert(0, i)


def add_new():
    global new_name
    new_name = entry.get()
    name_list.append(new_name)
    entry.delete(0, END)
    lbox.delete(0, END)
    btn_stop["state"] = "enabled"
    for i in name_list:
        lbox.insert(0, i)


root = Tk()
root.title("Турнирная сетка")
root.geometry("200x200")

entry = ttk.Entry()
entry.pack(padx=6, pady=6)

btn_stop = ttk.Button(text="Стоп", command=stop_button)
btn_stop.pack()
btn_add = ttk.Button(text="Добавить", command=add_new)
btn_add.pack()

lbox = Listbox(width=15, height=5)
lbox.pack()

keyboard.add_hotkey("enter", enter_press)


root.mainloop()

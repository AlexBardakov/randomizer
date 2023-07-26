from tkinter import *
from tkinter import ttk
import keyboard
import random

new_name = ""  # переменная для нового имени
name_list = []  # итоговый список имен
num_pairs = 0


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

    new_name = entry.get()
    name_list.append(new_name)
    entry.delete(0, END)
    lbox.delete(0, END)
    btn_stop["state"] = "enabled"
    for i in name_list:
        lbox.insert(0, i)


def sort_button():
    num_pairs = len(name_list) / 2
    for i in name_list:
        sort1 = random.sample(name_list, num_pairs)


keyboard.add_hotkey("enter", enter_press)

root = Tk()
root.title("Турнирная сетка")
root.geometry("200x400")

entry = ttk.Entry()
entry.pack(fill=X, padx=[20,20], pady=6)

btn_add = ttk.Button(text="Добавить", command=add_new)
btn_add.pack()
btn_add.place(x=20, y=30)

btn_stop = ttk.Button(text="Стоп", command=stop_button)
btn_stop.pack()
btn_stop.place(x=105, y=30)

lbox = Listbox(width=26, height=7)
lbox.pack()
lbox.place(x=20, y=60)

btn_sort = ttk.Button(text="Сортировать", command=sort_button)
btn_sort.pack()
btn_sort.place(x=55, y=180)

root.mainloop()


import tkinter as tk
import ttkbootstrap as ttk
from ttkthemes import ThemedTk
import random

def saveList(): # Open the file in write mode
    with open('data.txt', 'w') as file: 
        listbox_items = list_box.get(0, tk.END)
        for item in listbox_items:
            file.write(item + "\n")

def addTo(): #add to the end of the list and saves list
    current_task = name_entry.get().strip()

    if current_task:
        list_box.insert(list_box.size(), name_entry.get())  
        name_entry.delete(0, 'end')
    
    saveList()

def delete(): #deletes selected task and saves list
    selected_indices = list_box.curselection()
    for index in selected_indices[::-1]:
        list_box.delete(index)
    saveList()


def randomTask(): #returns a random task in a new window
    newWindow = ThemedTk(theme = 'winxpblue')
    newWindow.title('Random Task')
    newWindow.geometry('400x200')
    random_items = list_box.get(0, tk.END)

    if random_items:
        task = random.choice(random_items)
        lbl_task = tk.Label(newWindow, text = task)
        lbl_task.pack(pady = 80)
    else:
        lbl_task = tk.Label(newWindow, text = "List is empty")
        lbl_task.pack(pady = 80)


#window
window = ThemedTk(theme = 'winxpblue')
window.title('To-do list')
window.geometry('800x600')

#title
title_label = ttk.Label(master = window, text = 'To-do List', font = 'Calibri 24 bold')

#input field
task_var = ttk.StringVar()
name_entry = ttk.Entry(window, textvariable = task_var, font=('calibre', 10, 'normal'))
btn_submit = ttk.Button(window, text = 'add to list', command = addTo)
btn_delete = ttk.Button(window, text = 'delete from list', command = delete)
btn_random = ttk.Button(window, text = 'random task from list', command = randomTask)
list_box = tk.Listbox(window, height = 16, width = 32, font=('calibre', 14, 'normal'))

#grid
window.rowconfigure(0, weight = 3)
window.rowconfigure(1, weight = 5)
window.rowconfigure(2, weight = 1)
window.rowconfigure(3, weight = 1)
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)
window.columnconfigure(4, weight = 1)

#place widget
title_label.grid(row = 0, column = 1, sticky = 'nw')
name_entry.grid(row = 0, column = 1, sticky = 'w') 
btn_submit.grid(row = 0, column = 1, sticky = 'e')
btn_delete.grid(row = 0, column = 2, sticky = 'e')
btn_random.grid(row = 0, column = 3, sticky = 'e')
list_box.grid(row = 1, column = 1, columnspan = 3, sticky= 'nesw')

def loadList():  # Open the file in read mode
    try:
        with open('data.txt', 'r') as file:
            for line in file:
                list_box.insert(tk.END, line.strip())
    except FileNotFoundError:
        print("data.txt not found, starting with an empty list")
        # If the file doesn't exist, it will start with an empty list

# Call loadList() when initializing to load any existing data
loadList()

#run
window.mainloop()

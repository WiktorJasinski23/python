import tkinter as tk
from tkinter import ttk


def clicked(color, num):
    print(color + ': ' + str(num))
    
scales = 3
form = tk.Tk()
form.title("Tkinter Database Form")
form.geometry('1920x1080')

tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="All Records")
tab_parent.add(tab2, text="Add New Record")

piano = tk.Frame(tab1)
piano.pack()
piano.place(x=100, y=200)

white_keys = 7 * scales
black = [1, 1, 0, 1, 1, 1, 0] * scales
cvs = tk.Canvas(tab1, width = 1920, height = 1080)
cvs.place(x=0, y=0)
cvs.create_line(100,100, 1500,100, fill="black")
cvs.create_line(100,120, 1500,120, fill="black")
cvs.create_line(100,140, 1500,140, fill="black")
cvs.create_line(100,160, 1500,160, fill="black")
cvs.create_line(100,180, 1500,180, fill="black")
for i in range(white_keys):
    tk.Button(piano, bg='white', text = 'ok', anchor = 's', height = 20, width = 8, activebackground='gray87', command=lambda i=i: clicked('White', i)).grid(row=0, column=i*3, rowspan=2, columnspan=3, sticky='nsew')

for i in range(white_keys - 1):
    if black[i]:
        tk.Button(piano, bg='black',height = 10, width = 8, activebackground='gray22', command=lambda i=i: clicked('Black', i)).grid(row=0, column=(i*3)+2, rowspan=1, columnspan=2, sticky='nsew')

for i in range(white_keys * 3):
    piano.columnconfigure(i, weight=1)

for i in range(2):
    piano.rowconfigure(i, weight=1)

piano.tkraise()
tab_parent.pack(expand=1, fill='both')

form.mainloop()



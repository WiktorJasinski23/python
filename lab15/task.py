#!/usr/bin/env python3

from tkinter import *
from PIL import Image
from scipy import integrate, optimize
import matplotlib.pyplot as plt
import tkinter.font
import numpy as np

entryCol='#000000'
bgCol="#ffffff"


########################################################################

def onclick1():
    entry.insert(END, "1")
def onclick2():
    entry.insert(END, "2")
def onclick3():
    entry.insert(END, "3")
def onclick4():
    entry.insert(END, "4")
def onclick5():
    entry.insert(END, "5")
def onclick6():
    entry.insert(END, "6")
def onclick7():
    entry.insert(END, "7")
def onclick8():
    entry.insert(END, "8")
def onclick9():
    entry.insert(END, "9")
def onclick0():
    entry.insert(END, "0")


def onclickAdd():
    entry.insert(END, "+")
def onclickSub():
    entry.insert(END, "-")
def onclickMul():
    entry.insert(END, "*")
def onclickDiv():
    entry.insert(END, "/")
def onclickMod():
    entry.insert(END, "%")
def onclickPow():
    entry.insert(END, "**")
def onclickOpen():
    entry.insert(END, "(")
def onclickClose():
    entry.insert(END, ")")
def onclickEq():
    wart=eval(entry.get())
    entry.delete(0,END)
    entry.insert(0, str(wart))

def onclickRysuj():
    try:
        xp = int(e1.get())
        xk = int(e2.get())
        x = np.arange(xp, xk, 0.01)
        y = eval(e3.get())
        plt.plot(x, y)
        plt.show()
    except:
        pass

def onclickCalkuj():
    try:
        xp = int(e1.get())
        xk = int(e2.get())
        fx = lambda x: eval(e3.get())
        result = integrate.quad(fx, xp, xk)
        entry.delete(0, END)
        entry.insert(0, str(result[0]))
    except:
        pass

def onclickZnajdzMiejscaZerowe():
    try:
        xp = int(e1.get())
        xk = int(e2.get())
        fx = lambda x: eval(e3.get())
        result = optimize.bisect(fx, xp, xk)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        pass

def onclickFit():
    data = np.loadtxt(e4.get())
    # print(data)


def cl():
    entry.delete(0,END)
    cv.delete('all')

def exit():
    plt.close()
    root.destroy()

########################################################################

root = Tk()
root.title('Kalkulator')
root.protocol("WM_DELETE_WINDOW", exit)
calcfont=tkinter.font.Font(font=("Courier", 10, "bold"))

########################################################################

entry = Entry(root)
entry.config(width=60, fg="white", bg=entryCol, font=calcfont)
entry.grid(row=1, column=0, columnspan=8, pady=10)

########################################################################

button = Button(root, text='1', command=onclick1, bg=bgCol, font=calcfont)
button.grid(row=2, column=0, sticky=EW)

button = Button(root, text='2', command=onclick2, bg=bgCol, font=calcfont)
button.grid(row=2, column=1, sticky=EW)

button = Button(root, text='3', command=onclick3, bg=bgCol, font=calcfont)
button.grid(row=2, column=2, sticky=EW)

button = Button(root, text='4', command=onclick4, bg=bgCol, font=calcfont)
button.grid(row=3, column=0, sticky=EW)

button = Button(root, text='5', command=onclick5, bg=bgCol, font=calcfont)
button.grid(row=3, column=1, sticky=EW)

button = Button(root, text='6', command=onclick6, bg=bgCol, font=calcfont)
button.grid(row=3, column=2, sticky=EW)

button = Button(root, text='7', command=onclick7, bg=bgCol, font=calcfont)
button.grid(row=4, column=0, sticky=EW)

button = Button(root, text='8', command=onclick8, bg=bgCol, font=calcfont)
button.grid(row=4, column=1, sticky=EW)

button = Button(root, text='9', command=onclick9, bg=bgCol, font=calcfont)
button.grid(row=4, column=2, sticky=EW)

button = Button(root, text='0', command=onclick0, bg=bgCol, font=calcfont)
button.grid(row=5, column=0, sticky=EW)

button = Button(root, text='+', command=onclickAdd, bg=bgCol, font=calcfont)
button.grid(row=2, column=4, sticky=EW)

button = Button(root, text='-', command=onclickSub, bg=bgCol, font=calcfont)
button.grid(row=2, column=5, sticky=EW)

button = Button(root, text='=', command=onclickEq, bg=bgCol, font=calcfont)
button.grid(row=2, column=6, sticky=EW)

button = Button(root, text='*', command=onclickMul, bg=bgCol, font=calcfont)
button.grid(row=3, column=4, sticky=EW)

button = Button(root, text='/', command=onclickDiv, bg=bgCol, font=calcfont)
button.grid(row=3, column=5, sticky=EW)

button = Button(root, text='%', command=onclickMod, bg=bgCol, font=calcfont)
button.grid(row=3, column=6, sticky=EW)

button = Button(root, text='**', command=onclickPow, bg=bgCol, font=calcfont)
button.grid(row=4, column=4, sticky=EW)

button = Button(root, text='(', command=onclickOpen, bg=bgCol, font=calcfont)
button.grid(row=4, column=5, sticky=EW)

button = Button(root, text=')', command=onclickClose, bg=bgCol, font=calcfont)
button.grid(row=4, column=6, sticky=EW)

Label(root, text="Xp").grid(row=6)
Label(root, text="Xk").grid(row=7)
Label(root, text="f(x)").grid(row=8)
root.grid_rowconfigure(9, minsize=20)
Label(root, text="Nazwa pliku").grid(row=10)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.grid(row=6, column=1)
e2.grid(row=7, column=1)
e3.grid(row=8, column=1)
e4.grid(row=10, column=1)

button = Button(root, text='Rysuj', command=onclickRysuj, bg=bgCol, font=calcfont)
button.grid(row=6, column=2, sticky=EW)
button = Button(root, text='Calkuj', command=onclickCalkuj, bg=bgCol, font=calcfont)
button.grid(row=7, column=2, sticky=EW)
button = Button(root, text='Miejsca zerowe', command=onclickZnajdzMiejscaZerowe, bg=bgCol, font=calcfont)
button.grid(row=8, column=2, sticky=EW)
button = Button(root, text='Fit', command=onclickFit, bg=bgCol, font=calcfont)
button.grid(row=10, column=2, sticky=EW)

button = Button(root, text='exit', command=exit, bg=bgCol, font=calcfont)
button.grid(row=5, column=5, sticky=EW)

button = Button(root, text='clear', command=cl, bg=bgCol, font=calcfont)
button.grid(row=5, column=4, sticky=EW)




########################################################################

cv = Canvas(root, width=400, height=300)
cv["background"] = "white"
cv["borderwidth"] = 0
cv.config()
cv.grid(row=12, column=0, columnspan=9)

########################################################################

root.mainloop()

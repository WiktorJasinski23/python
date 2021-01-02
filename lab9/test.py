# import matplotlib.pyplot as plt
# from scipy.io import wavfile as wav
# from scipy.fftpack import fft
# import numpy as np
# rate, data = wav.read('journey.wav')
# fft_out = fft(data)
# plt.plot(data, np.abs(fft_out))
# plt.show()
#
# wav.write('lol.wav', rate, data)

import tkinter
import tkinter as tk

root = tk.Tk()
root.geometry('1000x600')

var=tk.StringVar()

Frame1 = tk.Frame(root)
Frame1.configure(background='light blue',height='300',width='500')
Frame1.grid(row='0',column='0')

Frame2 = tk.Frame(root)
Frame2.configure(background='grey',height='300',width='500')
Frame2.grid(row='0',column='1')

Frame3 = tk.Frame(root)
Frame3.configure(background='grey',height='300',width='500')
Frame3.grid(row='1',column='0')

Frame4 = tk.Frame(root)
Frame4.configure(background='light blue',height='300',width='500')
Frame4.grid(row='1',column='1')


def PrintOrder():
    LabelOrder = tk.Label(Frame3,text="DONUT ORDER")
    LabelOrder.grid(row='0',column='0')
    return

Button1 = tk.Button(Frame1,text="Apple Cinnamon",height='2',width='15',command=PrintOrder).grid(row='0',column='0')
Button2 = tk.Button(Frame1,text="Strawberry",height='2',width='15',command=PrintOrder).grid(row='0',column='1')
Button3 = tk.Button(Frame1,text="Custard",height='2',width='15',command=PrintOrder).grid(row='0',column='2')
Button4 = tk.Button(Frame1,text="Sugar Ring",height='2',width='15',command=PrintOrder).grid(row='1',column='0')
Button5 = tk.Button(Frame1,text="Chocolate Caramel",height='2',width='15',command=PrintOrder).grid(row='1',column='1')
Button6 = tk.Button(Frame1,text="Lemon Circle",height='2',width='15',command=PrintOrder).grid(row='1',column='2')
Button7 = tk.Button(Frame1,text="Blueberry Blaster",height='2',width='15',command=PrintOrder).grid(row='2',column='0')
Button8 = tk.Button(Frame1,text="Strawberry Surprise",height='2',width='15',command=PrintOrder).grid(row='2',column='1')
Button9 = tk.Button(Frame1,text="Simple Sugar",height='2',width='15',command=PrintOrder).grid(row='2',column='2')

Label1 = tk.Label(Frame2,text="Donut special 6 for the price of 5").grid(row='0',column='0')
Button10 = tk.Button(Frame2,text="SPECIAL",height='5',width='20').grid(row='1',column='0')

root.mainloop()
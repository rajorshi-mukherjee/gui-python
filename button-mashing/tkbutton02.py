import tkinter as tk
#import tkMessageBox
from tkinter import messagebox
from tkinter.constants import ACTIVE, DISABLED, GROOVE, RAISED, RIDGE, SUNKEN
top = tk.Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B1 = tk.Button(top, text ="Hello", command = helloCallBack)

#B2 = tk.Button(top, text ="Hello", command = helloCallBack, state=DISABLED, relief=SUNKEN)
#B2 = tk.Button(top, text ="Hello", command = helloCallBack, state=DISABLED, relief=RAISED)
#B2 = tk.Button(top, text ="Hello", command = helloCallBack, state=DISABLED, relief=GROOVE)
#B2 = tk.Button(top, text ="Hello", command = helloCallBack, state=DISABLED, relief=RIDGE)
#B2 = tk.Button(top, text ="Hello", command = helloCallBack, state=DISABLED, relief=GROOVE, underline=1, pady=5)
#B2 = tk.Button(top, text ="Hello", command = helloCallBack, state=ACTIVE, relief=GROOVE, underline=1, pady=5, activebackground='AQUA')
B2 = tk.Button(top, text ="Hello", command = helloCallBack, state=ACTIVE, relief=GROOVE, underline=1, pady=5, activebackground='AQUA', activeforeground='GREEN')

B1.pack()
B2.pack()
top.mainloop()
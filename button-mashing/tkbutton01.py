import tkinter as tk
#import tkMessageBox
from tkinter import messagebox
top = tk.Tk()

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tk.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
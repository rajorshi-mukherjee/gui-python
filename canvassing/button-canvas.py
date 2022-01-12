import tkinter as tk
#import tkMessageBox
from tkinter import messagebox
top = tk.Tk()

def helloCallBack():
    top2 = tk.Tk()  
    top2.geometry("200x200")  
    #creating a simple canvas  
    c = tk.Canvas(top2,bg = "pink",height = "200",width = 200)  
    arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
    c.pack()  
    top2.mainloop()  

B = tk.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
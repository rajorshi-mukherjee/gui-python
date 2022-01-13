from tkinter import *
from tkinter import messagebox   
  
top = Tk()  
  
top.geometry("200x200")  
  
checkvar1 = IntVar()  
  
checkvar2 = IntVar()  
  
checkvar3 = IntVar()  

def cprogram():
    messagebox.showinfo( "Hello Programmer", "So you like C programming huh?")

def cppprogram():
    messagebox.showinfo( "Hello Programmer", "So you like C programming huh?")

def javaprogram():
    messagebox.showinfo( "Hello Programmer", "So you like C programming huh?")

chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  

#chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10,command=cprogram())  
  
#chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10, command=cppprogram())  
  
#chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10, command=javaprogram())  
  
chkbtn1.pack()  
  
chkbtn2.pack()  
  
chkbtn3.pack()  
  
top.mainloop()  
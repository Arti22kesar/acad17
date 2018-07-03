#Ques1.

from tkinter import*
root = Tk()
label =Label(root,text="hello world!!").pack()
button=Button(root,text="Quit",command=quit).pack()
root.mainloop()


#Ques2.
from tkinter import*
root = Tk()
def show():
   print("hy girl,\n i am your frd")
label = Label(root,text="Hello world!!").pack()
button = Button(root,text="Quit",command=quit).pack()
button2 = Button(root,text="Click me",command=show).pack()
root.mainloop()

#Ques3.

from tkinter import *
import tkinter as tk
a=tk.Tk()
a.title("hey")
def arc():
    a.distroy()
button1=tk.Button(a,text='exit',width=30,command=arc)
button1.pack()
def arc():
    var1 = StringVar()
    label1 = Label(a,textvariable=var1)
    var1.set("hey arc")
    label1.pack()
    label2.destroy()
button2=tk.Button(a,text='name',command=arc)
button2.pack()
var2 = StringVar()
label2 = Label(a,textvariable=var2)
var2.set("hey arc abc ")
label2.pack()
a.mainloop()

#Ques4.

from tkinter import *
import tkinter
import tkinter as tk
x=tk.Tk()
x.title("hello frds")
l1=Label(x,text='name')
l1.grid(row=0)
e1=Entry(x)
e1.grid(row=0,column=3)
def hellofrd():
    e=e1.get()
    print(e)
    x.destroy()
b1=Button(x,text='enter',width=30,command=hellofrd)
b1.grid(row=4,column=4)
mainloop()







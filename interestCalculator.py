import tkinter
from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.geometry("1350x750+0+0")
root.title("Interest Calculator")
root.configure(background='cornsilk2')

Tops = Frame(root,bg='mintcream',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

Bottom = Frame(root,bg='mintcream',bd=20,pady=5,relief=RIDGE)
Bottom.pack(side=BOTTOM)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='Interest Calculator',bd=21,bg='black',
                fg='mintcream',justify=CENTER)
lblTitle.grid(row=0)

lblTitle=Label(Bottom,font=('arial',24,'bold'),text='Interest Calculator',bd=10,bg='black',
                fg='mintcream',justify=CENTER)
lblTitle.grid(row=0)

root.mainloop()
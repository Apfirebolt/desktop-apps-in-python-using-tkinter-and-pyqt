from tkinter import *
from time import sleep
import threading #import the library

root = Tk()
words = 'Hey there, This is python3'.split()
l = Label(root) #empty label
l.pack() #pack()

def call():
    for w in words: #loop through the list
        l.config(text=w) #update label with each word over each iteration
        sleep(2) #sleep for 2 seconds

threading.Thread(target=call).start() #create a separate thread to not freeze the GUI

root.mainloop()
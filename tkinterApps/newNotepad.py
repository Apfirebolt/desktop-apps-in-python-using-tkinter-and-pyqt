from tkinter import *
import threading
import time

class ApplicationWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Notepad in Tkinter")


root = ApplicationWindow()

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("300x300")
 
    # A Label widget to show in toplevel
    Label(newWindow,text ="This is a new window").pack()

text = Text(root, width=200, undo=True)
text_size = 11
text_style = "Times New Roman"
text.configure(font=(text_style, text_size))
text.pack()
save_file_id = ""

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Exit", command=root.quit)

Editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=Editmenu)
Editmenu.add_command(label="Font Style")
Editmenu.add_command(label="Font Size")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=openNewWindow)

root.config(menu=menubar)
root.mainloop()

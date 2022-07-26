from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
import threading
import time

class ApplicationWindow(Tk):
    def __init__(self):
        super().__init__()
        self.showTopFrame = True
        self.title("Notepad in Tkinter")
        self.geometry('700x500')
        self.addMenu()
        self.addFrame()
        # self.addHeader()
    
    def NewFile(self):
        text.delete(1.0, END)
        save_file_id = ' '
    
    def openFile(self):
        try:
            global text, save_file_id
            open_file_loc = askopenfilename()
            open_file = open(open_file_loc, 'r')
            text.delete(1.0, END)
            text.insert(END, open_file.read())
            save_file_id = open_file_loc
        except Exception as err:
            print('Error is ', err)


    def saveAsFile(self):
        try:
            name = asksaveasfile(mode='w', defaultextension=".txt")
            text2save = str(self.text.get(0.0, END))
            name.write(text2save)
            name = str(name)[(str(name).find("name='") + 6):str(name).find("'", (str(name).find("name='") + 6))]
        except Exception as err:
            print('Some error happened')

    
    def saveFile(self):
        global text, save_file_id
        if save_file_id == "":
            save_as_file()
        else:
            with open(save_file_id, 'w') as f:
                f.write(text.get(0.0, END))


    def showEditContainer(self):
        self.topFrame.pack(side="right",expand=True, fill="x", padx=4, pady=4)

    def hideEditButton(self):
        self.topFrame.pack_forget()

    def addMenu(self):
        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open", command=self.openFile)
        self.filemenu.add_command(label="Save", command=self.saveFile)
        self.filemenu.add_command(label="Save as...", command=self.saveAsFile)
        self.filemenu.add_command(label="Exit", command=self.quit)

        self.Editmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.Editmenu)
        self.Editmenu.add_command(label="Edit", command=self.showEditContainer)
        self.Editmenu.add_command(label="Font Style")
        self.Editmenu.add_command(label="Font Size")

        self.config(menu=self.menubar)
    

    def addHeader(self):
        self.filewin = Toplevel(self)
        string = "This is a small text editor built using Tkinter a python which supports GUI programming\n"
        string += "This text editor unlike many others supports many functions like giving suggestions based on your previous data \n"
        string += "Small, easy to use and works like the future of text editors \n"
        button = Label(self.filewin, text=string)
        button.pack()
    

    def addFrame(self):
        self.topFrame = Frame()
        self.topFrame.pack(side=TOP)

        frameLabel = Label(self.topFrame, text='Notepad Frame')
        frameLabel.pack(side=TOP)

        self.text = Text(self.topFrame, width=200, undo=True)
        text_size = 11
        text_style = "Times New Roman"
        self.text.configure(font=(text_style, text_size))
        self.text.pack(padx=4, pady=4)

        self.hideFrame = Button(self, text='Close Frame', command=self.hideEditButton)
        self.hideFrame.pack(side=BOTTOM, padx=5, pady=5, ipadx=5, ipady=5)



root = ApplicationWindow()
root.mainloop()


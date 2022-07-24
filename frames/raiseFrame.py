import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Multiple Frames Raised')
        self.geometry('400x400')
        self.addFrames()        
    
    def hello(self):
        self.frame2.tkraise()
        print('hello')

    def world(self):
        self.frame3.tkraise()
        print('world')

    def vicky(self):
        self.frame4.tkraise()
        print('Vicky')

    def addFrames(self):
        self.frame1=tk.Frame(self)
        self.frame2=tk.Frame(self)
        self.frame3=tk.Frame(self)
        self.frame4=tk.Frame(self)

        self.frame1.grid(row=0,column=0,rowspan=2, padx=5, pady=5)
        self.frame2.grid(row=0,column=1,rowspan=2)
        self.frame3.grid(row=0,column=1,rowspan=2)
        self.frame4.grid(row=0,column=1,rowspan=2)

        self.tag1=tk.Label(self.frame2,text='hello')
        self.tag2=tk.Label(self.frame3,text='world')
        self.tag3=tk.Label(self.frame4,text='Vicky')

        self.tag1.grid()
        self.tag2.grid()
        self.tag3.grid()

        self.press1=tk.Button(self.frame1,text='hello',command=self.hello, bd=4, padx=10, pady=10)
        self.press2=tk.Button(self.frame1,text='world',command=self.world, bd=4, padx=10, pady=10)
        self.press3=tk.Button(self.frame1,text='Vicky',command=self.vicky, bd=4, padx=10, pady=10)

        self.press1.grid(row=0)
        self.press2.grid(row=1)
        self.press3.grid(row=2)


root=Application()
root.mainloop()
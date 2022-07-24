from tkinter import *
from tkinter import messagebox

class Calculator:
    
    def __init__(self,master):

        self.operator = ""
        self.var = StringVar()
        self.var.trace_add('write', self.checkNumber)
        self.previousValue = 0
        self.currentValue = 0
        frame_top = Frame(master, height=400, width=45)
        frame_top.pack(side=TOP, fill=BOTH, expand=True)

        frame_bottom = Frame(master, height=400, width=4, bg='#bbdeed')
        frame_bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.entry = Entry(frame_top,textvariable=self.var,bg='grey',width=45,bd=4, borderwidth=10, insertwidth=4,justify='right',font=('arial',10,'bold'))
        self.entry.pack()
        
        self.t = Text(self.entry,height=50)

        label_0 = Label(frame_bottom, bg='black')
        label_0.grid(row=3, column=0, padx=16, pady=16)
        button_0 = Button(label_0, text='0', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(0))
        button_0.pack()

        label_1 = Label(frame_bottom, bg='black')
        label_1.grid(row=3, column=1, padx=16, pady=16)
        button_1 = Button(label_1, text='1', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(1))
        button_1.pack()

        label_2 = Label(frame_bottom, bg='black')
        label_2.grid(row=3, column=2, padx=16, pady=16)
        button_2 = Button(label_2, text='2', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(2))
        button_2.pack()

        label_3 = Label(frame_bottom, bg='black')
        label_3.grid(row=4, column=0, padx=16, pady=16)
        button_3 = Button(label_3, text='3', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(3))
        button_3.pack()

        label_4 = Label(frame_bottom, bg='black')
        label_4.grid(row=4, column=1, padx=16, pady=16)
        button_4 = Button(label_4, text='4', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(4))
        button_4.pack()

        label_5 = Label(frame_bottom, bg='black')
        label_5.grid(row=4, column=2, padx=16, pady=16)
        button_5 = Button(label_5, text='5', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(5))
        button_5.pack()

        label_6 = Label(frame_bottom, bg='black')
        label_6.grid(row=5, column=0, padx=16, pady=16)
        button_6 = Button(label_6, text='6', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(6))
        button_6.pack()

        label_7 = Label(frame_bottom, bg='black')
        label_7.grid(row=5, column=1, padx=16, pady=16)
        button_7 = Button(label_7, text='7', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(7))
        button_7.pack()

        label_8 = Label(frame_bottom, bg='black')
        label_8.grid(row=5, column=2, padx=16, pady=16)
        button_8 = Button(label_8, text='8', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(8))
        button_8.pack()

        label_9 = Label(frame_bottom, bg='black')
        label_9.grid(row=6, column=0, padx=16, pady=16)
        button_9 = Button(label_9, text='9', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput(9))
        button_9.pack()

        label_dot = Label(frame_bottom, bg='black')
        label_dot.grid(row=6, column=1, padx=16, pady=16)
        button_dot = Button(label_dot, text='.', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.feedInput('.'))
        button_dot.pack()

        label_equal = Label(frame_bottom, bg='black')
        label_equal.grid(row=6, column=2, padx=16, pady=16)
        button_equal = Button(label_equal, text='=', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.calculateResult())
        button_equal.pack()

        label_plus = Label(frame_bottom, bg='black')
        label_plus.grid(row=3, column=9, padx=16, pady=16)
        button_plus = Button(label_plus, text='+', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.operate('+'))
        button_plus.pack()

        label_minus = Label(frame_bottom, bg='black')
        label_minus.grid(row=4, column=9, padx=16, pady=16)
        button_minus = Button(label_minus, text='-', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.operate('-'))
        button_minus.pack()

        label_multiply = Label(frame_bottom, bg='black')
        label_multiply.grid(row=5, column=9, columnspan=2, padx=16, pady=16)
        button_multiply = Button(label_multiply, text='*', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.operate('*'))
        button_multiply.pack()

        label_divide = Label(frame_bottom, bg='black')
        label_divide.grid(row=6, column=9, padx=16, pady=16)
        button_divide = Button(label_divide, text='/', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.operate('/'))
        button_divide.pack()

        label_clear = Label(frame_bottom, bg='black')
        label_clear.grid(row=4, column=11, padx=16, pady=16)
        button_clear = Button(label_clear, text='CLEAR', font=('Helvetica', '16'),bg='black',fg='cyan', command=lambda:self.clear())
        button_clear.pack()
    
    def operate(self, operator):
        self.operator = operator
        self.previousValue = int(self.var.get())
        textValue = ''
        if self.operator == '+':
            textValue = 'Enter value to add to ' + str(self.previousValue)
        elif self.operator == '-':
            textValue = 'Enter value to subtract from ' + str(self.previousValue)
        elif self.operator == '*':
            textValue = 'Enter value to multiply to ' + str(self.previousValue)
        else:
            textValue = 'Enter value to divided by ' + str(self.previousValue)
        self.var.set('')
        messagebox.showinfo("showinfo", textValue)
        

    def calculateResult(self):
        result = 0
        self.currentValue = int(self.var.get())
        if self.operator == '+':
            result = self.previousValue + self.currentValue
        elif self.operator == '-':
            result = self.previousValue - self.currentValue
        elif self.operator == '*':
            result = self.previousValue * self.currentValue
        else:
            result = self.previousValue / self.currentValue
        messagebox.showinfo("showinfo", result)
        self.var.set(str(result))
        self.operator = ""

    def clear(self):
        self.entry.delete(0,END)

    def feedInput(self, value):
        previousValue = self.var.get()
        newValue = str(previousValue) + str(value)
        self.var.set(newValue)

    def checkNumber(self, *args):
        if not str(self.var.get()).isnumeric() and self.var.get() != '':
            messagebox.showerror("showerror", "Only numbers are accepted")
            self.var.set('')


root = Tk()
c = Calculator(root)
root.title("New Calculator")
root.geometry('400x400')
root.mainloop()
from tkinter import *

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = Tk()

column1 = Frame(root)
column1.pack(side=LEFT, fill=X)

metres_label = Label(column1, text="Metres To Feet:")
metres_label.pack(padx=5, pady=5)

metres_entry = Entry(column1, text="Metres:")
metres_entry.pack(padx=5, pady=5)

result_label = Label(column1, text="Result in Feet:")
result_label.pack(padx=5, pady=5)

column2 = Frame(root)
column2.pack(side=RIGHT, fill=X)

feet_label = Label(column2, text="Feet To Metre:")
feet_label.pack(padx=5, pady=5)

feet_entry = Entry(column2, text="Feet:")
feet_entry.pack(padx=5, pady=5)

result_label_feet = Label(column2, text="Result in Metre:")
result_label_feet.pack(padx=5, pady=5)

def convertMeterToFeet():
    try:
        metres = float(metres_entry.get())
        feet = metres * 3.28084
        result_label['text'] = f"{feet:.3f}"
    except ValueError:
        pass

def convertFeetToMeter():
    try:
        feet = float(feet_entry.get())
        result_label_feet['text'] = '%.3f' % (feet / 3.28084)
    except ValueError:
        pass

def clearFields():
    result_label['text'] = ''
    result_label_feet['text'] = ''
    metres_entry.delete(0,END)
    feet_entry.delete(0,END)


b1 = Button(column1, text='Metre to Feet', command=convertMeterToFeet)
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(column2, text='Feet To Metre', command=convertFeetToMeter)
b2.pack(side=LEFT, padx=5, pady=5)
b3 = Button(column1, text='Quit', command=root.quit)
b3.pack(side=LEFT, padx=5, pady=5)
b4 = Button(column2, text='Clear', command=clearFields)
b4.pack(side=LEFT, padx=5, pady=5)

root.title('Distance conversion program')
root.geometry('400x300') 
root.mainloop()   
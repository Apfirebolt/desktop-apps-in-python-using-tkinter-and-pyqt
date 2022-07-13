from tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        currentFrame = Frame(root)
        currentFrame.grid(row=i, column=j)

        currentLabel = Label(currentFrame, text='Current')
        currentLabel.pack(side=TOP)

        currentEntry = Entry(currentFrame)
        currentEntry.pack(side=BOTTOM)

mainloop()
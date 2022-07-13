# importing module
from tkinter import *


def helloCommand():
    print('Hello command', textBox.get("1.0", "end-1c"))


# main container
root = Tk()
root.title('A sample margin Example')

# first frame
frame1 = Frame(root, relief='sunken',
              bd=10, bg='white')
frame1.pack(fill='both', expand=True,
           padx=30, pady=20)

# second frame
frame2 = Frame(root, relief='sunken',
              bd=10, bg='white')
frame2.pack(fill='both', expand=True,
           padx=30, pady=20)

# container content
label = Label(frame1, text='GeeksForGeeks.org!',
              width=45, height=10, bg="black",
              fg="white")
label.pack()

textBox = Text(frame2, height = 5, width = 52)
textBox.pack(side=TOP, expand=True, fill='x')

button1 = Button(frame2, text ="Hello", command = helloCommand)
button1.pack(side=LEFT, expand=True, fill='x')

button2 = Button(frame2, text ="Magnetar", command = helloCommand)
button2.pack(side=LEFT, expand=True, fill='x')

root.mainloop()
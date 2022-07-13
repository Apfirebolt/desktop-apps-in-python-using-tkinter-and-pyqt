from tkinter import *

# Create a GUI app
app = Tk()

# Give a title to your app
app.title("My New App")

frame1 = LabelFrame(app, text="Fruit", bg="green",fg="white", padx=15, pady=15)
frame1.pack(expand=True, side=RIGHT)

b1 = Button(frame1, text="Apple")
b1.pack()

frame2 = LabelFrame(app, text="Vegetable", bg="yellow", padx=25, pady=5)
frame2.pack(expand=True, side=TOP)

b2 = Button(frame2, text="Tomato")
b2.pack()

app.mainloop()

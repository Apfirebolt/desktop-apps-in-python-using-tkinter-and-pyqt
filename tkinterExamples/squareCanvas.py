from tkinter import *
master = Tk()

w = Canvas(master, width=250, height=200)
w.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
w.create_rectangle(50, 50, 100, 100, fill="red", outline = 'blue') 
points = [10,20, 30,40, 50,60]
w.create_polygon(points, fill='red')
w.pack()
master.mainloop()
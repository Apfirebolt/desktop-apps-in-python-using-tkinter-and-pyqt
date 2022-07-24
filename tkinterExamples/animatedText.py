import tkinter as tk


def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")

canvas_width = 400
canvas_height = 200 

root = tk.Tk()
canvas = tk.Canvas(root, width=canvas_width,height=canvas_height)
canvas.pack()
checkered(canvas,10)

canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW)

test_string = "This is a test"
#Time delay between chars, in milliseconds
delta = 500 
delay = 500
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta


root.mainloop()
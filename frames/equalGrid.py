import tkinter as tk

class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('Two frames of equal size')

root = ApplicationWindow()

left_frame = tk.Frame(root, bg = 'yellow')
left_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

right_frame = tk.Frame(root, bg = 'lime')
right_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

root.mainloop()
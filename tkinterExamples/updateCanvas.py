import tkinter as tk
import string
import random


class Welcome(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.time_track = 0
        self.geometry("500x200")
        self.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(width=300, height=300, bg='red')   
        self.canvas.pack(expand=True, fill="both")    
        self.lbl = tk.Label(self.canvas, text="0% complete!")
        self.lbl.pack()

        tk.Button(self, text="Start", command=self.update_time).pack()


    def update_time(self):
        if self.time_track != 100:
            self.lbl.config(text="{}% complete!".format(self.time_track))
            self.time_track += 1
            self.after(100, self.update_time)
        else:
            self.lbl.config(text="Complete!")


b = Welcome()
b.mainloop()
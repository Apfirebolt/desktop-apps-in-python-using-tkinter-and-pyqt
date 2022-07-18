import tkinter as tk
import tkinter.ttk

colours = ['red','green','orange','white','yellow','blue']


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cinema Booking')
        self.geometry('400x400')
        self.addWidget()

    def addWidget(self):
        headingLabel = tk.Label(self, text="Cinema Bookings", font="Roboto 12")
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")

        r = 4
        for c in colours:
            currentLabel = tk.Label(self, text=c, relief=tk.RIDGE, width=15).grid(row=r,column=0)
            currentEntry = tk.Entry(self, bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
            r = r + 1



app = Application()
app.mainloop()
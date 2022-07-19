import tkinter as tk
from tkinter import ttk


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.master.configure(background='green')
        self.user_input = tk.StringVar()
        self.width = 360

        label = ttk.Label(self, text="Enter your name: ")
        entry = ttk.Entry(self)
        button = ttk.Button(self, command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")

    def greet(self):
        print(f"Hello, {self.user_input.get()}!")


class LightFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.master.configure(background='red')
        self.user_input = tk.StringVar()
        self.width = 360

        label = ttk.Label(self, text="Enter your name sidewalk: ")
        entry = ttk.Entry(self)
        button = ttk.Button(self, command=self.greet)

        label.pack(side="right")
        entry.pack(side="right")
        button.pack(side="right")

    def greet(self):
        print(f"Hello, {self.user_input.get()}!")


root = tk.Tk()
frame = UserInputFrame(root)
frame.pack(side=tk.RIGHT)

nextFrame = LightFrame(root)
nextFrame.pack(side=tk.LEFT)

root.mainloop()
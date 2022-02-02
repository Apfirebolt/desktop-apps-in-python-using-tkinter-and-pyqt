import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Separator Example")

label = ttk.Label(root, text="Hello, World!", padding=20)
label.pack()

main_sep = ttk.Separator(root, orient="horizontal")
main_sep.pack(fill="x")

label = ttk.Label(root, text="Hello, World!", padding=20)
label.pack()

root.mainloop()
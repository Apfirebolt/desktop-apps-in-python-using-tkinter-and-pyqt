"""
Classic vs Themed Labels
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

tk.Button(root, text='Classic Label').pack()
ttk.Button(root, text='Themed Label').pack()

root.mainloop()
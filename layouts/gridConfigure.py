import tkinter as tk
from tkinter import ttk


class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry('300x300')
        self.columnconfigure(1, weight=1)

        # username
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_entry = ttk.Entry(self,  show="*")
        self.password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # salary
        self.salary_label = ttk.Label(self, text="Salary:")
        self.salary_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.salary_entry = ttk.Entry(self,  show="*")
        self.salary_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # login button
        self.login_button = ttk.Button(self, text="Login")
        self.login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

# root window
root = ApplicationWindow()
root.mainloop()
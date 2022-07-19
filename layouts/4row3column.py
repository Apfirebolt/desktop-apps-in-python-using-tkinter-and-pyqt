import tkinter as tk
from tkinter import ttk


class ApplicationWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry('400x300')
        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(1, weight=3)
        self.createWidgets()

    def createWidgets(self):
        # username
        self.firstNameLabel = ttk.Label(self, text="First Name :")
        self.firstNameLabel.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.firstNameEntry = ttk.Entry(self)
        self.firstNameEntry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.lastNameLabel = ttk.Label(self, text="Last Name:")
        self.lastNameLabel.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

        self.lastNameEntry = ttk.Entry(self)
        self.lastNameEntry.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        self.passwordLabel = ttk.Label(self, text="Password:")
        self.passwordLabel.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.passwordEntry = ttk.Entry(self,  show="*")
        self.passwordEntry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # confirm password
        self.confirmPasswordLabel = ttk.Label(self, text="Confirm Password:")
        self.confirmPasswordLabel.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

        self.confirmPasswordEntry = ttk.Entry(self,  show="*")
        self.confirmPasswordEntry.grid(column=3, row=1, sticky=tk.E, padx=5, pady=5)

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
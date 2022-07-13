"""
A GUI Program to calculate loan interest
"""

from tkinter import *
from tkinter import messagebox


def calculateInterest():
    alertMessage = ''
    amount = principalAmount.get()
    rate = rateOfInterest.get()
    years = numberOfYears.get()

    if not amount:
        alertMessage = 'Please enter principal amount'
    if not rate:
        alertMessage = 'Please enter rate of interest'
    if not years:
        alertMessage = 'Please enter number of years'

    if alertMessage:
        messagebox.showinfo("Important Information", alertMessage)
    else:
        totalAmount = 0
        totalInterest = 0
        interestPerMonth = 0
        amountPerMonth = 0


root = Tk()
root.title("Loan Interest Calculator")

root.resizable(False, False)
cal = Frame(root)
cal.pack(side=BOTTOM, padx=10, pady=8)
cal.configure(bg="burlywood4")

header = Frame(root)
header.pack(side=TOP)
header.configure(bg="red")

headerLabel = Label(header, width=20, text="Loan Interest Calculator", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

headerLabel.grid(row=1, column=4)

principalLabel = Label(cal, width=20, text="Enter Principal Amount", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

principalLabel.grid(row=1, column=4)

principalAmount = Entry(cal, width=40, font=("Comic Sans MS", 15), bd=10, justify=LEFT,
             disabledbackground="white", disabledforeground="black")

principalAmount.grid(row=1, column=5)

rateOfInterestLabel = Label(cal, width=20, text="Enter Rate of Interest", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

rateOfInterestLabel.grid(row=2, column=4)

rateOfInterest = Entry(cal, width=40, font=("Comic Sans MS", 15), bd=10, justify=LEFT,
             disabledbackground="white", disabledforeground="black")

rateOfInterest.grid(row=2, column=5)

numberOfYearsLabel = Label(cal, width=20, text="Enter Number Of Years", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

numberOfYearsLabel.grid(row=3, column=4)

numberOfYears = Entry(cal, width=40, font=("Comic Sans MS", 15), bd=10, justify=LEFT,
             disabledbackground="white", disabledforeground="black")

numberOfYears.grid(row=3, column=5)

interestButton = Button(cal, font=("Comic Sans MS", 15), command=calculateInterest, text = "Calculate Interest")
interestButton.grid(row=4, column=5, pady=10)

totalAmountLabel = Label(cal, width=20, text="Total Amount", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

totalAmountLabel.grid(row=5, column=4)

totalAmountEntry = Entry(cal, width=40, state='disabled', font=("Comic Sans MS", 15), bd=10, justify=LEFT,
             disabledbackground="white", disabledforeground="black")

totalAmountEntry.grid(row=5, column=5)

totalAmountPerMonthLabel = Label(cal, width=20, text="Total Amount Per Month", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

totalAmountPerMonthLabel.grid(row=6, column=4)

totalAmountPerMonthEntry = Entry(cal, width=40, state='disabled', font=("Comic Sans MS", 15), bd=10, justify=LEFT,
             disabledbackground="white", disabledforeground="black")

totalAmountPerMonthEntry.grid(row=6, column=5)

totalInterestLabel = Label(cal, width=20, text="Total Interest", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

totalInterestLabel.grid(row=8, column=4)

totalInterestEntry = Entry(cal, width=40, state='disabled', font=("Comic Sans MS", 15), bd=10, justify=LEFT,
             disabledbackground="white", disabledforeground="black")

totalInterestEntry.grid(row=8, column=5)

totalInterestPerMonthLabel = Label(cal, width=20, text="Total Interest Per Month", font=("Comic Sans MS", 12), bd=8, justify=LEFT)

totalInterestPerMonthLabel.grid(row=9, column=4)

totalInterestPerMonthEntry = Entry(cal, width=40, state='disabled', font=("Comic Sans MS", 15), bd=10, justify=LEFT,
             disabledbackground="white", disabledforeground="black")

totalInterestPerMonthEntry.grid(row=9, column=5)

header.mainloop()
cal.mainloop()
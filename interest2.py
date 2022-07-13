from tkinter import *


def interest():
    label_p.grid(row=1, column=1)
    p.grid(row=1, column=2)

    label_r.grid(row=2, column=1)
    r.grid(row=2, column=2)

    label_t.grid(row=3, column=1)
    t.grid(row=3, column=2)

    find.grid(row=4, column=1, columnspan=2)


def check():
    C.delete(0, END)
    S.delete(0, END)
    principle = p.get()
    principle = int(principle)
    rate = r.get()
    rate = int(rate)
    time = t.get()
    time = int(time)

    Label(top, text="Compound Interest", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic").grid(
        row=5, column=1)
    Label(top, text="simple Interest", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic").grid(row=6,
                                                                                                                 column=1)
    # Driver Code
    top = Tk()
    top.title("SIMPLE and COMPOUND INTEREST")
    top.geometry("500x250")
    # top.configure(bg="yellow")
    top["background"] = "#ffffff"

    find = Button(top, text="CALCULATE INTEREST", command=lambda: check(), width=20, background="#5D6D7E",
                  foreground="white")

    # gui for Interest
    label_p = Label(top, text="Enter Principle", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic")
    label_r = Label(top, text="Enter rate", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic")
    label_t = Label(top, text="Enter Years", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic")

    p = Entry(top, width=20)
    r = Entry(top, width=20)
    t = Entry(top, width=20)

    C = Entry(top, width=20)
    S = Entry(top, width=20)
    interest()
    top.mainloop()
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    C.grid(row=5, column=2)
    C.insert(INSERT, CI)

    si = (principle * rate * time) / 100
    S.grid(row=6, column=2)
    S.insert(INSERT, si)
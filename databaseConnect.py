import tkinter as tk
import mysql.connector
from tkinter import *


def submitUser():
    user = Username.get()
    passw = password.get()

    print(f"The name entered by you is {user} {passw}")

    login(user, passw)


def login(user, passw):
    if passw:
        db = mysql.connector.connect(host="localhost",
                                     user=user,
                                     password=passw,
                                     db="College")
        cursor = db.cursor()

    # If no password is enetered by the
    # user
    else:
        db = mysql.connector.connect(host="localhost",
                                     user=user,
                                     db="College")
        cursor = db.cursor()

    # A Table in the database
    savequery = "select * from STUDENT"

    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()

        for x in myresult:
            print(x)
        print("Query Executed successfully")

    except:
        db.rollback()
        print("Error occured")


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login",
                      bg='blue', command=submitUser)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()

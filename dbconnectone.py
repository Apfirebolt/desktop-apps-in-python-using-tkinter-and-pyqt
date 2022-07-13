import tkinter as tk
import mysql.connector
from tkinter import *


def access_database():
    db = mysql.connector.connect(host="localhost",
                                 user='root',
                                 password='',
                                 db="stocks")
    cursor = db.cursor()
    savequery = "select * from stocks"

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
root.title("Access Database Stocks")


submitbtn = tk.Button(root, text="Login", command=access_database)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()

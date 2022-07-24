from tkinter import*
import random
import time

def  btnclick(numbers):
    pass


def clrdisplay():
    pass

def equals():
    pass

root = Tk()
root.geometry("1600x700+0+0")
root.title("Grocery Bill Management System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

groceryFrame = Frame(root,width = 900,height=700,relief=SUNKEN, padx=20, pady=20)
groceryFrame.pack(side=LEFT)

calculatorFrame = Frame(root ,width = 400,height=700,relief=SUNKEN, padx=20, pady=20)
calculatorFrame.pack(side=RIGHT)

# Adding Calculator buttons
btn7=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="#03fc77", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="#03fc77", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="#03fc77", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="#03fc77", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="#03fc77", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="#03fc77", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="#03fc77", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="#03fc77", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)

btn1=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="#03fc77", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="#03fc77", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="#03fc77", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="#03fc77", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)

btn0=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="#03fc77", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="#03fc77", command=clrdisplay)
btnc.grid(row=5,column=1)

btnEqual=Button(calculatorFrame,padx=16,pady=16,bd=4,width = 16, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="#03fc77",command=equals)
btnEqual.grid(columnspan=4)

Decimal=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text=".",bg="#03fc77", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(calculatorFrame,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="#03fc77", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)

#-----------------INFO TOP------------
labelTitle = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Grocery Management System",fg="steel blue",bd=10,anchor='w')
labelTitle.grid(row=0,column=0)

# Declare text variables

rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

orderLabel = Label(groceryFrame, font=('Lucida Console' ,12, 'bold' ),text="Order No.",fg="steel blue",bd=4)
orderLabel.grid(row=0,column=0)
orderText = Entry(groceryFrame,font=('Courier New Greek' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
orderText.grid(row=0,column=1)

lblfries = Label(groceryFrame, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=4,anchor='w')
lblfries.grid(row=0,column=2)
txtfries = Entry(groceryFrame,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=0,column=3)

lblLargefries = Label(groceryFrame, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=4,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(groceryFrame,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)


root.mainloop()
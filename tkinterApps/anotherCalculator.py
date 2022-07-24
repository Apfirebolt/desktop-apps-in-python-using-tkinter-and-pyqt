import tkinter
from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.geometry("850x550+0+0")
root.title("Silky Calculator")
root.configure(background='cornsilk2')

Tops = Frame(root,bg='cornsilk2',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',32,'bold'),text='New Calculator System',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)

calculatorFrame = Frame(root,bg='cornsilk2',bd=10,relief=RIDGE)
calculatorFrame.pack(side=TOP, padx=20, pady=20)

Buttons_F=Frame(calculatorFrame,bg='cornsilk2',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(calculatorFrame,bg='cornsilk2',bd=6,relief=RIDGE)
Cal_F.pack(side=BOTTOM)

text_Input = StringVar()
operator = ""


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


#############################################Calculator###############################################################################
txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn2=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='cornsilk2',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='cornsilk2',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='cornsilk2',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='cornsilk2',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='cornsilk2',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='cornsilk2',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='cornsilk2',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='cornsilk2',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='cornsilk2',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='cornsilk2',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='cornsilk2',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='cornsilk2',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='cornsilk2',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='cornsilk2',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='cornsilk2',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=2,bd=2,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='cornsilk2',command=lambda:btnClick('/')).grid(row=5,column=3)


root.mainloop()
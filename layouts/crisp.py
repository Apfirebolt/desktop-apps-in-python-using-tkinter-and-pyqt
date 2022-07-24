from tkinter import *



if __name__ == '__main__':
   root = Tk()
   root.title('A sample app')

   header = Frame(root)
   header.pack(side=TOP, fill=X, pady=20)

   headingLabel = Label(header, text="A sample App", font=("Arial", 18), pady=8, padx=8, bg='#000', fg='#ff0',)
   headingLabel.pack()

   bottom = Frame(root)
   bottom.pack(side=BOTTOM, fill=X)

   footerLabel = Label(bottom, text="@copyright 2022, all rights reserved", font=("Arial", 16), pady=8)
   footerLabel.pack()

   content = Frame(root)
   content.pack(side=TOP, fill=X)

   column1 = Frame(content, bg='#00A')
   column1.pack(side=LEFT, expand= True, fill=BOTH)
   column2 = Frame(content, bg='red')
   column2.pack(side=RIGHT, expand = True, fill=BOTH)

   b1 = Button(column1, text='Final Balance')
   b1.pack(side=LEFT, padx=5, pady=5)

   b3 = Button(column2, text='Quit', command=root.quit)
   b3.pack(side=RIGHT, padx=5, pady=5)

   root.geometry('400x400') 
   root.mainloop()
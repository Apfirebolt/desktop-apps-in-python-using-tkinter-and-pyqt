from tkinter import *
col1fields = ['Annual Rate', 'Number of Payments']
col2fields = ['Interest Rate', 'Interest Per Month']

def makeform(root, fields, container):
   entries = {}
   for field in fields:
      row = Frame(container)
      label = Label(row, width=22, text=field+": ", anchor='w')
      entry = Entry(row)
      entry.insert(0,"0")

      row.pack(side=TOP, fill=BOTH, padx=5, pady=5)
      label.pack(side=LEFT)
      entry.pack(side=RIGHT, expand=YES, fill=X)


if __name__ == '__main__':
   root = Tk()

   column1 = Frame(root)
   column1.pack(side=LEFT, fill=X)
   column2 = Frame(root)
   column2.pack(side=RIGHT, fill=X)

   makeform(root, col1fields, column1)
   makeform(root, col2fields, column2)

   b1 = Button(column1, text='Final Balance')
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(column1, text='Monthly Payment')
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(column1, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)

   root.mainloop()
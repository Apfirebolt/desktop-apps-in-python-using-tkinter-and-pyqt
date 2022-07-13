from tkinter import *
fields = ('Annual Rate', 'Number of Payments')

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      label = Label(row, width=22, text=field+": ", anchor='w')
      entry = Entry(row)
      entry.insert(0,"0")

      row.pack(side=TOP, fill=BOTH, padx=5, pady=5)
      label.pack(side=LEFT)
      entry.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = entry
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)

   b1 = Button(root, text='Final Balance')
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Monthly Payment')
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
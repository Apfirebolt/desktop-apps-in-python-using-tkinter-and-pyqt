from tkinter import *
 
# Create object
root = Tk()
 
# Adjust size
root.geometry("500x500")

#Create an frame
frame1= Frame(root, bg= "red", padx=5, pady=5, width=385, height=460, relief='raised', borderwidth=5)
frame2= Frame(root, bg="cyan", padx=5, pady=5, width=385, height=460, relief='raised', borderwidth=5)

frame1.pack(padx=8, pady=8)
frame2.pack(padx=8, pady=8)
 
# Specify Grid
buttonFrame = Frame(root)

Grid.columnconfigure(frame2,0,weight=1)
Grid.columnconfigure(frame2,1,weight=1)
Grid.columnconfigure(frame2,2,weight=1)
Grid.columnconfigure(frame2,3,weight=1)
Grid.columnconfigure(frame2,4,weight=1)

Grid.rowconfigure(frame1,0,weight=1)
Grid.rowconfigure(frame1,1,weight=1)
Grid.rowconfigure(frame1,2,weight=1)
Grid.rowconfigure(frame1,3,weight=1)
Grid.rowconfigure(frame1,4,weight=1)

for i in range(5):
    currentButton = Button(frame2,text="Button - " + str(i),  borderwidth = 2)
    currentButton.grid(row=0,column=i,sticky="NSEW")

for i in range(5):
    currentButton = Button(frame1,text="Button - " + str(i),  borderwidth = 2)
    currentButton.grid(row=i,column=0,sticky="NS")

 
# Execute tkinter
root.mainloop()
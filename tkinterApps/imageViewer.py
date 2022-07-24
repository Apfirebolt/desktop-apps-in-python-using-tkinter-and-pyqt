# importing the tkinter module and PIL
# that is pillow module
import tkinter as tk
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
 

class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Image Viewer in Tkinter')
        self.geometry('400x400')
        self.addWidget()
    
    def addWidget(self):
        self.fileButton = tk.Button(text='Click to Open File', command=self.selectFiles)
        self.fileButton.pack()

    def selectFiles(self):
        filetypes = (
            ('Images', '*.png'),
            ('All files', '*.*')
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected Files',
            message=filenames
        )

        image_no_1 = ImageTk.PhotoImage(Image.open(filenames[0]))
        self.imageLabel = tk.Label(self, image=image_no_1)
 
        # We have to show the box so this below line is needed
        self.imageLabel.pack()

    
root = AppWindow()
root.mainloop()
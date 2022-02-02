import tkinter as tk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

root = tk.Tk()
root.resizable(False, False)
root.title("Widget Examples")

text = tk.Text(root, height=16)  # Show what happens if you `.pack()` here, while still assigning to variable.
text.pack()

# Insert content into the text area
text.insert("2.5", "Please enter a comment...")  # Can use \n to insert multiple lines.

text_content = text.get("1.0", "end")
print(text_content)

root.mainloop()
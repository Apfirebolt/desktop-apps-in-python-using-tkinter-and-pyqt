import tkinter as tk
from datetime import datetime
import time
counter = 66600

running = False
class Clock(tk.Label):
    def __init__(self, parent=None, seconds=True):
        tk.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time = time.strftime('%I:%M:%S')
        else:
            self.time = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        self.after(200, self.tick)

    def tick(self):
        if self.display_seconds:
            new_time = time.strftime('%I:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)

def timestamp():
    print(time.strftime("%I:%M:%S"))

def count():
    if running:
        global counter

        # To manage the initial delay.
        if counter==66600:            
            display="Starting..."
        else:
            tt = datetime.fromtimestamp(counter)
            string = tt.strftime("%H:%M:%S")
            display=string

        label['text']=display 
        label.after(1000, count) 
        counter += 1
   
def counter_label(label):
    # Triggering the start of the counter.
    count()     

# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
   
# Stop function of the stopwatch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    listbox.insert(1, label['text'])

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
    listbox.delete(0, 'end')
   
    # If rest is pressed after pressing stop.
    if running==False:      
        reset['state']='disabled'
        label['text']='Stopwatch!'
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'

applicationWindow = tk.Tk()
applicationWindow.title('Stop Watch in Tkinter')
applicationWindow.minsize(width=250, height=70)
applicationWindow.geometry('400x400')

# Add normal clock timing through Clock class
clock = Clock(applicationWindow)
clock.pack()
clock.configure(bg='white', fg='black', font=("helvetica", 65))

label = tk.Label(applicationWindow, text="Stopwatch!", fg="#eb344f", font="Verdana 24 bold")
label.pack(padx=4, pady=4)

listbox = tk.Listbox(applicationWindow, width=30, fg="#349eeb", font="Verdana 12", justify='center')

listbox.pack(padx=4, pady=4)
f = tk.Frame(applicationWindow)

start = tk.Button(f, text='Start', width=10, bg='#eb344f', fg='white', command=lambda:Start(label))
stop = tk.Button(f, text='Stop',width=10, bg='#eb344f', state='disabled', fg='white', command=Stop)
reset = tk.Button(f, text='Reset',width=10, bg='#eb344f', state='disabled', fg='white', command=lambda:Reset(label))

f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")

applicationWindow.mainloop()

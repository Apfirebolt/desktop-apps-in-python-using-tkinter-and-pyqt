import time
import random
import tkinter as tk

global randomNum
tries = 0

def getNumber():
    guess = entry.get()
    global randomNum
    if len(guess) > 0 and guess.lower() == guess.upper():
        guess = int(guess)
        mainGame(guess)
    else:
        label["text"] = "You must enter a number"
        entry.delete("0", "end")


def pickNumber():
    global randomNum
    label.config(text="The system has picked a number", fg="black")
    randomNum = random.randint(1, 100)
    # print(randomNum)
    entry.focus_force()

def mainGame(guess):
    global tries
    global randomNum
    tries = tries + 1
    entry.delete("0", "end")
    if tries > 5:
        label.config(text=f"You have lost the game.", fg="#a8325c")
        root.update()
        time.sleep(4)
        pickNumber()
    if guess < randomNum:
        label["text"] = "Selected Number is higher!"
    elif guess > randomNum:
        label["text"] = "Selected Number is lower"
    else:
        label.config(text=f"CORRECT! You got it in {tries} tries", fg="#32a852")
        root.update()
        time.sleep(4)
        pickNumber()
        count = 0

    
root = tk.Tk()
root.title("The Number Guessing Game")

label = tk.Label(root, text="The Number Guessing Game", font="Verdana 20")
label.pack(fill=tk.BOTH, expand=True)

helpLabel = tk.Label(root, text="The number would be between 1-100, you have 5 tries to guess the number", font="Verdana 12", wraplength=350)
helpLabel.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font="Verdana 15 normal")
entry.pack(fill=tk.BOTH, expand=True)

guessButton = tk.Button(root, bg='#CCC', text="Guess Number", command=getNumber)
guessButton.config( height = 2, width = 15)
guessButton.pack(padx=10, pady=10)

pickNumber()

root.geometry("550x250")
root.minsize(470, 110)

root.mainloop()
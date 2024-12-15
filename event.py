from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")
window.config(bg="light pink")

def handle_keypress(event):
    print(event.char)
    
window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")
    
button =Button(text="Click me!", bg="light blue")
button.pack(pady=15)

button.bind("<Button-1>", handle_click)

window.mainloop()
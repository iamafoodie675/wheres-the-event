from tkinter import *

def convert_to_cm():
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text=f"{inches} inches ={cm:.2f} cm")
    
    
    
root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x200")

instruction_label = Label(root, text="Enter length in inches:", font=("Arial", 12))
instruction_label.pack(pady=10)

entry = Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

convert_button = Button(root, text="Convert", command=convert_to_cm, bg="#f78272", fg="white", font=("Arial", 12))
convert_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14), fg="#333333")
result_label.pack(pady=10)

root.mainloop()
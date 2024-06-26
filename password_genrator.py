import tkinter as tk
from tkinter import messagebox
import string
import secrets


def generate_password():
    password_length = int(length_entry.get())
    
   
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(secrets.choice(characters) for i in range(password_length))
    
   
    password_display.config(text=password)


win = tk.Tk()
win.title("Password Generator")

length_label = tk.Label(win, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(win, width=20)
length_entry.pack()


generate_button = tk.Button(win, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


password_display = tk.Label(win, text="", font=("bold", 16))
password_display.pack(pady=10)

win.mainloop()

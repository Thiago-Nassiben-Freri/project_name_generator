import tkinter as tk
from tkinter import messagebox
from random import choice

def name_generator(): 
    with open('names.txt', 'r') as file: 
        names = file.read().splitlines()
    with open('surnames.txt', 'r') as file: 
        surnames = file.read().splitlines()
    name = choice(names)
    surname = choice(surnames)

    full_name = name + ' ' + surname
    return full_name

def display_name():
    generated_name = name_generator()
    name_label.config(text=generated_name)

def exit_app(): 
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"): 
        root.destroy()

root = tk.Tk()
root.title("Name Generator")

name_label = tk.Label(root, text="", font=("Arial", 12))
name_label.pack(pady=10)

generate_button = tk.Button(root, text="Generate Name", command=display_name)
generate_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()


import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Input Error", "Password length must be an integer.")
        return

    if length < 8:
        messagebox.showwarning("Weak Password", "Password length should be at least 8 characters for better security.")
        return

    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()
    exclude_chars = exclude_var.get()

    if not (include_uppercase or include_lowercase or include_digits or include_special):
        messagebox.showwarning("Selection Error", "Select at least one character type.")
        return

    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if exclude_chars:
        characters = ''.join(c for c in characters if c not in exclude_chars)

    if not characters:
        messagebox.showwarning("Exclusion Error", "Excluding too many characters, no characters left to generate password.")
        return

    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Clipboard", "Your Password had been copied to clipboard.")

root = tk.Tk()
root.title("Yash's Password Generator")
root.geometry("350x280")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var).grid(row=0, column=1, padx=10, pady=5)

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=1, column=0, padx=10, pady=2, sticky='w')

lowercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var).grid(row=1, column=1, padx=10, pady=2, sticky='w')

digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, column=0, padx=10, pady=2, sticky='w')

special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=2, column=1, padx=10, pady=2, sticky='w')

tk.Label(root, text="Exclude Characters:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
exclude_var = tk.StringVar()
tk.Entry(root, textvariable=exclude_var).grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
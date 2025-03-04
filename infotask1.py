import itertools
import string
import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "apple"

# Updated Dictionary List
DICTIONARY = ["password123", "letmein", "qwerty", "123456", "admin", "hunter2", "trustno1", "iloveyou", "welcome1", "abc123"]

def dictionary_attack(username):
    """Performs a dictionary attack."""
    if username != CORRECT_USERNAME:
        messagebox.showerror("Error", "Invalid username.")
        return False

    log_text.set("Starting Dictionary Attack...\n")
    window.update()

    for password in DICTIONARY:
        log_text.set(log_text.get() + f"Trying: {password}\n")
        window.update()
        
        if password == CORRECT_PASSWORD:
            messagebox.showinfo("Success", f"Password found: {password}")
            return True

    log_text.set(log_text.get() + "Dictionary Attack failed.\n")
    return False

def brute_force_attack():
    """Performs a brute force attack."""
    log_text.set(log_text.get() + "\nStarting Brute Force Attack...\n")
    window.update()

    characters = string.ascii_letters  # A-Z, a-z
    attempts = 0

    for password in itertools.product(characters, repeat=5):
        attempts += 1
        attempt = "".join(password)

        if attempts % 50000 == 0:  # Update GUI every 50,000 attempts
            log_text.set(log_text.get() + f"Attempts: {attempts}, Trying: {attempt}\n")
            window.update()

        if attempt == CORRECT_PASSWORD:
            messagebox.showinfo("Success", f"Password found: {attempt}\nTotal attempts: {attempts}")
            return True

    messagebox.showerror("Failed", "Brute Force Attack failed.")
    return False

def start_attack():
    """Starts the attack process."""
    username = username_entry.get().strip()

    if dictionary_attack(username) == False:
        brute_force_attack()





# Function placeholder
def start_attack():
    log_text.set("Attack started...")

# GUI Setup
window = tk.Tk()
window.title("Password Cracker")
window.geometry("500x400")
window.configure(bg="#1e1e1e")  # Dark background

# Username Label & Entry
tk.Label(window, text="Enter Username:", font=("Arial", 12), bg="#1e1e1e", fg="white").pack(pady=5)
username_entry = tk.Entry(window, font=("Arial", 12), bg="#333", fg="white", insertbackground="white")
username_entry.pack(pady=5)

# Start Button
start_button = tk.Button(window, text="Start Attack", font=("Arial", 12), bg="#ff5555", fg="white", command=start_attack)
start_button.pack(pady=10)

# Log Box
log_text = tk.StringVar()
log_label = tk.Label(window, textvariable=log_text, justify="left", font=("Arial", 10), anchor="w", bg="#1e1e1e", fg="#00ff00")
log_label.pack(padx=10, pady=10, fill="both")

# Run GUI
window.mainloop()
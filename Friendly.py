import tkinter as tk
from tkinter import messagebox
import webbrowser

def close_program():
    window.destroy()

def start_action():
    # You can define the action to be performed when the button is clicked here
    print("Action started")

def open_new_window():
    # Create a new top-level window
    new_window = tk.Toplevel(window)
    new_window.title("PLEASE")

    # Add text to the new window
    text_label = tk.Label(new_window, text="Hey, please, you can delete some files\n files that u don`t need anymore\n really\nor just send me to your friends\n and told them that i`m very dangerous)", font=("Arial", 12), padx=20, pady=20)
    text_label.pack()

    # Add buttons to the new window
    button_close = tk.Button(new_window, text="Okay, I will do this", command=close_program, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
    button_close.pack(side=tk.LEFT, padx=10, pady=10)
    button_action = tk.Button(new_window, text="Still no :( )", command=open_urls, bg="#f44336", fg="white", font=("Arial", 12), padx=10, pady=5)
    button_action.pack(side=tk.RIGHT, padx=10, pady=10)

def open_urls():
    urls = [
        "https://github.com/BAD-PI-cybsec/Friendly",
        "https://github.com/BAD-PI-cybsec/Friendly",
        "https://github.com/BAD-PI-cybsec/Friendly",
        "https://github.com/BAD-PI-cybsec/Friendly"
    ]
    for url in urls:
        webbrowser.open(url)

# Create the main application window
window = tk.Tk()
window.title("Friendly")
window.configure(bg="#f0f0f0")

# Create and add multi-line text to the window
text = "Hello dear user\nI`m just Friendly virus\nMy dev is so lazy, so can you...\n...just delete fome files from your PC\n and send me to your friends pls <3\n"
text_label = tk.Label(window, text=text, justify=tk.LEFT, font=("Arial", 14), padx=20, pady=20, bg="#f0f0f0")
text_label.pack()

# Create and add buttons to the window
button_close = tk.Button(window, text="Yeah, I will do this", command=close_program, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
button_close.pack(side=tk.LEFT, padx=10, pady=10)
button_open_window = tk.Button(window, text="Sorry, but I don`t", command=open_new_window, bg="#f44336", fg="white", font=("Arial", 12), padx=10, pady=5)
button_open_window.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the application
window.mainloop()

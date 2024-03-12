import tkinter as tk
import requests
import random
import webbrowser

def move_window():
    x = random.randint(0, root.winfo_screenwidth() - root.winfo_width())
    y = random.randint(0, root.winfo_screenheight() - root.winfo_height())
    root.geometry(f"+{x}+{y}")
    root.after(1000, move_window)

def open_urls():
    urls = [
        "https://bit.ly/3uY43pf"
    ]
    for url in urls:
        webbrowser.open(url)
    root.after(5000, open_urls)  # Call open_urls again after 5 seconds

root = tk.Tk()
root.title("Friendly")
root.configure(bg="#f0f0f0")

text = "Hello dear user\nI`m just Friendly virus\nMy dev is so lazy, so can you...\n...just delete some files from your PC\n and send me to your friends pls <3\n"
text_label = tk.Label(root, text=text, justify=tk.LEFT, font=("Arial", 14), padx=20, pady=20, bg="#f0f0f0")
text_label.pack()

# Get and display the public IP address
response = requests.get('https://api64.ipify.org?format=json')
public_ip = response.json()['ip']
ip_label = tk.Label(root, text=f"Your Public IP Address is: {public_ip}", font=("Arial", 12), padx=20, pady=10, bg="#f0f0f0")
ip_label.pack()

# Start moving window
move_window()

# Start opening websites every 5 seconds
open_urls()

root.mainloop()
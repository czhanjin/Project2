import tkinter as tk
import threading
import pygame


def close_window():
    root.destroy()

# Tkinter window
root = tk.Tk()
root.title("Hygiene Reminder")

message_label = tk.Label(root, text="Hi, Mr. Li! It's time to shower!", font=("Helvetica", 30))
message_label.pack(pady=20)

# Button to close the window and stop audio
close_button = tk.Button(root, text="OK", command=close_window, font=("Helvetica", 18))
close_button.pack(pady=10)

# Pop-up Window size
root.geometry("600x200")

root.mainloop()
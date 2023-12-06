import tkinter as tk
import threading
import pygame

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("bird.mp3")  
    pygame.mixer.music.play()

def close_window():
    pygame.mixer.music.stop()
    root.destroy()

# Tkinter window
root = tk.Tk()
root.title("Medicine Reminder")

message_label = tk.Label(root, text="Hi, Mr.Li! It's time to take the pills!", font=("Helvetica", 30))
message_label.pack(pady=20)

# Button to close the window and stop audio
close_button = tk.Button(root, text="OK", command=close_window, font=("Helvetica", 18))
close_button.pack(pady=10)

# Pop-up Window size
root.geometry("600x200")

# Audio playing
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

root.mainloop()
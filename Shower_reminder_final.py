import tkinter as tk
import threading
import pygame

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("shower.mp3")  
    pygame.mixer.music.play()

def close_window():
    pygame.mixer.music.stop()
    root.destroy()

# Tkinter window
root = tk.Tk()
root.title("Shower Reminder")

message_label = tk.Label(root, text="Hi, Mr.Li! It's time to shower! \n 你好，李先生。该洗澡啦！ ", font=("Helvetica", 30))
message_label.pack(pady=20)

# Close the window and stop audio
close_button = tk.Button(root, text="OK", command=close_window, font=("Helvetica", 18))
close_button.pack(pady=10)

# Pop-up Window size
root.geometry("600x200")

# Audio playing
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

root.mainloop()
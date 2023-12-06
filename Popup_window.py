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

# Create a Tkinter window
root = tk.Tk()
root.title("Audio Player")

# Message label with larger font size
message_label = tk.Label(root, text="Hi, Mr.Li! It's time to take the pills!", font=("Helvetica", 30))
message_label.pack(pady=20)

# Button to close the window and stop audio
close_button = tk.Button(root, text="OK", command=close_window, font=("Helvetica", 18))
close_button.pack(pady=10)

# Set the initial size of the window
root.geometry("600x200")

# Start playing audio in a separate thread
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

# Run the Tkinter main loop
root.mainloop()
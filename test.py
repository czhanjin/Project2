from pygame import mixer
import time
import schedule

### 11/29/23: Alarm will play at user selected time and play for 30sec. Terminal display: time to take med!! 
### Goal: press button to stop alarm, display on screen 

def play_alarm():
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("bird.mp3")

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Display a message before starting the music
    print("Time to take Med!!")

    # Start playing the song
    mixer.music.play()

    # Play for 30 seconds
    time.sleep(30)

    # Stop the music after 30 seconds
    mixer.music.stop()

# Schedule the alarm to run every day at 8 am
schedule.every().day.at("13:15").do(play_alarm)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)


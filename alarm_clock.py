# let's import some modules that will help us to run the code
from datetime import datetime # for the time
import pygame # to execute our ringtone

# let's initialize pygame mixer
pygame.mixer.init()

# setting variables for alarm time

time = input("Enter the time you want to ring the alarm(HH:MM:SS): ")
hour = time[0:2]
minute = time[3:5]
seconds = time[6:8]
period_alarm = time[9:11].upper()

# printing words while setting your alarm
print("Hold on! Your alarm is about to ring yet. Take a rest for a while!")

# while loop to set up the alarm
while True:
    # these variables will detect the current time
    time_now = datetime.now()
    hour_now = time_now.strftime('%I')
    minute_now = time_now.strftime('%M')
    seconds_now = time_now.strftime('%S')
    time_period_now = time_now.strftime('%p')
    # if statements
    if period_alarm == time_period_now:
        if hour == hour_now:
            if minute == minute_now:
                if seconds == seconds_now:
                    print("Alarm is ringing. Time to wake up!") # print something if the alarm already hits
                    pygame.mixer.music.load(r'C:\Users\USER\Downloads\ringtone.mp3') # location of the ringtone that i want to use
                    pygame.mixer.music.play()  # it will play the ringtone
                    while pygame.mixer.music.get_busy(): # this will continue playing the ringtone if the user did not stop it
                        continue
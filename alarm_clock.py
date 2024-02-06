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

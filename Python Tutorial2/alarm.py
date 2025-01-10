# python alarm clock

import time
import datetime
import pygame

def format_time(input_time):
    parts = input_time.split(":")
    
    hours = int(parts[0]) if len(parts) > 0 and parts[0] else 0
    minutes = int(parts[1]) if len(parts) > 1 and parts[1] else 0
    seconds = int(parts[2]) if len(parts) > 2 and parts[2] else 0
    
    formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
    return formatted_time

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "alarm_tune.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time+" "+alarm_time)
        if current_time == alarm_time:
            print("Wake Up")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)




if __name__ == "__main__":
    alarm_time = input("Enter the alarm time:(HH:MM:SS) ")
    alarm_time = format_time(alarm_time)
    set_alarm(alarm_time)
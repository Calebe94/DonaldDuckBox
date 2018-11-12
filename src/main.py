import vlc
import os
import time
from mutagen.mp3 import MP3

# In project modules

import donaldduck
from presence import has_presence
import motor
from constants import DONALD_TRACK

# AUDIO_PATH = os.path.dirname(os.path.abspath(__file__)).replace("src", "res/audio")

# audio = MP3(AUDIO_PATH+"/donald_duck_laugh.mp3")

def main():
    motor.init()
    while True:
        if has_presence() == True:
            motor.on()
            # donaldduck.play("donald_duck_laugh.mp3")
            # donaldduck.play_donald_laugh()
            # donaldduck.play_random()
            donaldduck.play(DONALD_TRACK)
            motor.off()
        time.sleep(1)

if __name__ == "__main__":
    main()


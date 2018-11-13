import vlc
import os
import time
from mutagen.mp3 import MP3

# In project modules

import donaldduck
from presence import Presence
from motor import Motor
from constants import DONALD_TRACK

AUDIO_PATH = os.path.dirname(os.path.abspath(__file__)).replace("src", "res/audio")

audio = MP3(AUDIO_PATH+"/"+DONALD_TRACK)
print(audio.info.length)
print("> Ready to use...")
def main():
    motor = Motor()
    print("> Motor initialized")
    presence = Presence()
    print("> Presence initialized")
    while True:
        if presence.has_presence() == True:
            motor.on()
            print("> Motor ON!")
            # donaldduck.play(DONALD_TRACK)

            p = vlc.MediaPlayer(AUDIO_PATH+"/"+DONALD_TRACK)
            p.play()
            start = time.time()

            while audio.info.length > (time.time() - start):
                if ((time.time()-start) > 0.0) and (time.time()-start) < 1.0:
                    motor.on()
                elif ((time.time()-start) > 1.1) and ((time.time()-start) < 20.0):
                    motor.off()
                elif ((time.time()-start) > 20.1) and ((time.time()-start) < 22.0):
                    motor.on()
                elif ((time.time()-start) > 21.1):
                    motor.off()
                    
                
                    
            # time.sleep(int(audio.info.length))
            # Measure Elapsed Time
            print("> Playing Track!")
            motor.off()
            print("> Motor OFF!")
        time.sleep(1)

if __name__ == "__main__":
    main()


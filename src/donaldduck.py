import vlc
import os
import time
from mutagen.mp3 import MP3
import random

AUDIO_PATH = os.path.dirname(os.path.abspath(__file__)).replace("src", "res/audio")

def play(track):
    try:
        audio = MP3(AUDIO_PATH+"/"+str(track))
        p = vlc.MediaPlayer(AUDIO_PATH+"/"+str(track))
        p.play()
        time.sleep(int(audio.info.length))
        pass
    except Exception as error:
        print(error)
        pass

def play_donald_laugh():
    play("donald_duck_laugh.mp3")

def play_by_index(index):
    play_donald_laugh()
    return "PLAY "+str(index)

def play_random():
    random_number = random.random()*10
    print("> Playing "+str(int(random_number))+" track!")
    play_by_index(random_number)
    return "LAUGH"
import vlc
import os
import time
from mutagen.mp3 import MP3


print(os.path.dirname(os.path.abspath(__file__)))

AUDIO_PATH = os.path.dirname(os.path.abspath(__file__)).replace("tests", "res/audio")

print(AUDIO_PATH)

audio = MP3(AUDIO_PATH+"/donald_duck_laugh.mp3")
print(audio.info.length)

p = vlc.MediaPlayer(AUDIO_PATH+"/donald_duck_laugh.mp3")
p.play()

time.sleep(int(audio.info.length))

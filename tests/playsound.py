# import playsound
from playsound import playsound
import os
# print(os.path.dirname(os.path.abspath(__file__)))

AUDIO_PATH = os.path.dirname(os.path.abspath(__file__)).replace("tests", "res/audio")

print(AUDIO_PATH+'/donald_duck_laugh.mp3')
# playsound.playsound(AUDIO_PATH+'/donald_duck_laugh.mp3', True)

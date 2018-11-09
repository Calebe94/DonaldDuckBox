import webbrowser
import os
# print(os.path.dirname(os.path.abspath(__file__)))

AUDIO_PATH = os.path.dirname(os.path.abspath(__file__)).replace("tests", "res/audio")
print(AUDIO_PATH)

os.system("start "+AUDIO_PATH+'/donald_duck_laugh.mp3')

# webbrowser.open(AUDIO_PATH+'/donald_duck_laugh.mp3')

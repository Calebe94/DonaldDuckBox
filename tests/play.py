import vlc
import os
print(os.path.dirname(os.path.abspath(__file__)))

AUDIO_PATH = os.path.dirname(os.path.abspath(__file__)).replace("tests", "res/audio")

print(AUDIO_PATH)

p = vlc.MediaPlayer(AUDIO_PATH+"/donald_duck_laugh.mp3")
# p = vlc.MediaPlayer("file:///"+AUDIO_PATH+"/donald_duck_laugh.mp3")
p.play()

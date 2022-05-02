from pydub import AudioSegment
from pydub.playback import play
import random

def Chief():
    audio = "Don't Like.mp3"
    start = random.randrange(0, 292500)
    end = start + 4000
    sound = AudioSegment.from_mp3(audio)
    splice = sound[start:end]
    play(splice)

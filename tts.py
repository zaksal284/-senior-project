from pydub import AudioSegment
from pydub.playback import play

def helmet():
    file_path = "/home/keepboard/Desktop/helmet.mp3"
    sound = AudioSegment.from_file(file_path, format='mp3')
    play(sound)

def twopeople():
    file_path = "/home/keepboard/Desktop/keepboard.mp3"
    sound = AudioSegment.from_file(file_path, format='mp3')
    play(sound)

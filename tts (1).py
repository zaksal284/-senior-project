import pyttsx3

sound= pyttsx3.init()

def helmet():
    tts = "헬멧을 착용해주세요"
    sound = pyttsx3.init()
    sound.setProperty('rate', 150)
    sound.setProperty('voice', 'korean')
    sound.say(tts)
    sound.runAndWait()

def twopeople():
    tts="100kg 초과로 인해 탑승이 불가합니다."
    sound = pyttsx3.init()
    sound.setProperty('rate', 150)
    sound.setProperty('voice', 'korean')
    sound.say(tts)
    sound.runAndWait()

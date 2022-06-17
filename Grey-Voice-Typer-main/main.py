# made by Grey
import speech_recognition as grey
from pynput.keyboard import Key,Controller

keyboard = Controller()
g = grey.Recognizer()

while True:

    with grey.Microphone() as source:

        audio = g.listen(source)
        voice = g.recognize_google(audio, language='tr-TR')
        keyboard.type(voice)
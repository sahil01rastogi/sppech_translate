import time

import googletrans
import speech_recognition as sr                      # from google_trans_new import google_translator
from deep_translator import GoogleTranslator
from playsound import playsound
from gtts import gTTS
import os

print(googletrans.LANGUAGES)

r = sr.Recognizer()
translator = GoogleTranslator()
while True:
    with sr.Microphone() as source:
        print("speak now")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if (speech_text == "exit"):
                break
        except sr.UnknownValueError:
            print("could not understand")
        except sr.RequestError:
            print("could not request result from google")

        translated_text = GoogleTranslator(source='auto', target='en').translate(speech_text)
        print(translated_text)

        voice = gTTS(translated_text, lang='en')
        voice.save("one.mp3")
        playsound("one.mp3")
        os.remove("one.mp3")


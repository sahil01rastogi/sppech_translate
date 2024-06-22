import speech_recognition as sr
from deep_translator import GoogleTranslator

def speech_to_text_and_translate():
    r = sr.Recognizer()
    translator = GoogleTranslator()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print("Recognized speech:", speech_text)
            translated_text = translator.translate(speech_text, source='auto', target='en')
            print("Translated text:", translated_text)
            return translated_text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "Could not understand audio"
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return "Could not request results"

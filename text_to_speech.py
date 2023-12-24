from googletrans import Translator
from gtts import gTTS
import googletrans
from deep_translator import GoogleTranslator
from playsound import playsound
import os

def text_to_speech(input_text, source_lang='en', target_lang='en'):
    # Translate the input text to the target language
    translator = Translator()
    translation = translator.translate(input_text, src=source_lang, dest=target_lang)
    translated_text = translation.text

    # Convert the translated text to speech
    tts = gTTS(text=translated_text, lang=target_lang, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")

if __name__ == "__main__":
    # Input text and language settings
    input_text = input("Enter the text you want to convert to speech: ")
    source_lang = input("Enter the source language code (e.g., en for English): ")
    target_lang = input("Enter the target language code (e.g., es for Spanish): ")

    # Convert text to speech
    text_to_speech(input_text, source_lang, target_lang)


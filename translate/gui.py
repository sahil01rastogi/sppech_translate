import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import googletrans
import speech_recognition as sr
from deep_translator import GoogleTranslator
from playsound import playsound
from gtts import gTTS
import os

def translate():
    input_text = input_text_entry.get()
    source_lang = source_lang_entry.get()
    target_lang = target_lang_entry.get()
    translated_text = translate_text(input_text, source_lang, target_lang)
    translated_text_label.config(text=translated_text)

def convert_to_speech():
    input_text = input_text_entry.get()
    source_lang = source_lang_entry.get()
    target_lang = target_lang_entry.get()
    text_to_speech(input_text, source_lang, target_lang)

def speech_to_text():
    speech_text = speech_to_text_and_translate()
    translated_text_label.config(text=speech_text)

def voice_translation():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            translator = GoogleTranslator(source=source_lang_entry.get(), target=target_lang_entry.get())
            translated_text = translator.translate(speech_text)
            print(translated_text)
            voice = gTTS(translated_text, lang=target_lang_entry.get())
            voice.save("translation.mp3")
            playsound("translation.mp3")
            os.remove("translation.mp3")
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print("Could not request result from Google")

def translate_text(text, source_lang, target_lang):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translated_text = translator.translate(text)
    return translated_text

def text_to_speech(text, source_lang, target_lang):
    tts = gTTS(text, lang=target_lang)
    tts.save("translation.mp3")
    playsound("translation.mp3")
    os.remove("translation.mp3")

def speech_to_text_and_translate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        speech_text = r.recognize_google(audio)
        print("You said:", speech_text)
        return speech_text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return "Could not understand audio."
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return f"Could not request results; {e}"

root = tk.Tk()
root.title("Translation App")

# Input section
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

ttk.Label(input_frame, text="Input Text:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_text_entry = ttk.Entry(input_frame, width=50)
input_text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Source Language:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
source_lang_entry = ttk.Combobox(input_frame, width=20, values=["en", "hi", "bn", "ml", "mr"])
source_lang_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
source_lang_entry.set("en")

ttk.Label(input_frame, text="Target Language:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
target_lang_entry = ttk.Combobox(input_frame, width=20, values=["en", "hi", "bn", "ml", "mr"])
target_lang_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
target_lang_entry.set("en")

# Buttons for actions
action_frame = ttk.Frame(root)
action_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")


voice_translation_button = ttk.Button(action_frame, text="Voice Translation", command=voice_translation)
voice_translation_button.grid(row=0, column=3, padx=5, pady=5)

# Display translated text
translated_text_label = ttk.Label(root, text="")
translated_text_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

root.mainloop()

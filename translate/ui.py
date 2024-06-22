import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from module1 import translate_text
from module2 import text_to_speech
from module3 import speech_to_text_and_translate

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

root = tk.Tk()
root.title("Translation App")

# Input section
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

ttk.Label(input_frame, text="Input Text:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_text_entry = ttk.Entry(input_frame, width=50)
input_text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Source Language:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
source_lang_entry = ttk.Entry(input_frame, width=20)
source_lang_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Target Language:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
target_lang_entry = ttk.Entry(input_frame, width=20)
target_lang_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

# Buttons for actions
action_frame = ttk.Frame(root)
action_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

translate_button = ttk.Button(action_frame, text="Translate", command=translate)
translate_button.grid(row=0, column=0, padx=5, pady=5)

convert_button = ttk.Button(action_frame, text="Convert to Speech", command=convert_to_speech)
convert_button.grid(row=0, column=1, padx=5, pady=5)

# Display translated text
translated_text_label = ttk.Label(root, text="")
translated_text_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

root.mainloop()

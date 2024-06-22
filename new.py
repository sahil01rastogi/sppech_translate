import subprocess
import tempfile
import tkinter as tk

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS


class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Translator")

        self.source_language_var = tk.StringVar(value="en")
        self.target_language_var = tk.StringVar(value="en")

        self.create_widgets()

    def create_widgets(self):
        # Language selection
        source_lang_label = tk.Label(self.root, text="Source Language:")
        source_lang_entry = tk.Entry(self.root, textvariable=self.source_language_var)
        target_lang_label = tk.Label(self.root, text="Target Language:")
        target_lang_entry = tk.Entry(self.root, textvariable=self.target_language_var)

        source_lang_label.grid(row=0, column=0, padx=5, pady=5)
        source_lang_entry.grid(row=0, column=1, padx=5, pady=5)
        target_lang_label.grid(row=0, column=2, padx=5, pady=5)
        target_lang_entry.grid(row=0, column=3, padx=5, pady=5)

        # Text input and translation
        text_input_label = tk.Label(self.root, text="Enter Text:")
        self.text_input_entry = tk.Entry(self.root)
        translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)

        text_input_label.grid(row=1, column=0, padx=5, pady=5)
        self.text_input_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        translate_button.grid(row=1, column=4, padx=5, pady=5)

        # Voice input and translation
        voice_input_button = tk.Button(self.root, text="Voice Input", command=self.voice_to_text)
        voice_output_button = tk.Button(self.root, text="Voice Output", command=self.text_to_voice)

        voice_input_button.grid(row=2, column=0, padx=5, pady=5)
        voice_output_button.grid(row=2, column=1, padx=5, pady=5)

    def translate_text(self):
        input_text = self.text_input_entry.get()
        translator = Translator()
        translation = translator.translate(input_text, src=self.source_language_var.get(), dest=self.target_language_var.get())
        translated_text = translation.text
        tk.messagebox.showinfo("Translation Result", f"Translated Text: {translated_text}")

    def voice_to_text(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source)

        try:
            input_text = recognizer.recognize_google(audio)
            self.text_inpt_entry.delete(0, tk.END)
            self.text_input_entry.insert(0, input_text)
        except sr.UnknownValueError:
            tk.messagebox.showwarning("Error", "Could not understand audio")

    def text_to_voice(self):
        input_text = self.text_input_entry.get()
        translator = Translator()
        translation = translator.translate(input_text, src=self.source_language_var.get(), dest=self.target_language_var.get())
        translated_text = translation.text

        # Convert translated text to voice
        tts = gTTS(text=translated_text, lang=self.target_language_var.get(), slow=False)
        audio_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        tts.save(audio_file.name)
        audio_file_path = audio_file.name

        # Play the generated audio file
        subprocess.run(["start", audio_file_path], shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()

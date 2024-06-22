from googletrans import Translator

def translate_text(input_text, source_lang='en', target_lang='en'):
    translator = Translator()
    translation = translator.translate(input_text, src=source_lang, dest=target_lang)
    translated_text = translation.text
    return translated_text

if __name__ == "__main__":
    # Input text and language settings
    input_text = input("Enter the text you want to translate: ")
    source_lang = input("Enter the source language code (e.g., en for English): ")
    target_lang = input("Enter the target language code (e.g., es for Spanish): ")

    # Translate text
    translated_text = translate_text(input_text, source_lang, target_lang)

    # Display the translated text
    print(f"Translated text: {translated_text}")

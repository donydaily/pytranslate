import os
import time
from deep_translator import GoogleTranslator

# Daftar kode bahasa yang didukung
LANGUAGES = {
    'de': 'German',
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'id': 'Indonesian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh-cn': 'Chinese (Simplified)',
    # Tambahkan kode bahasa lainnya sesuai kebutuhan
}

def clear():
    os.system('clear')

def banner():
    print("""
••-_-┏┓_-_-_-_-_-_-_-_-_-_-_-_-_••
••_-_┃┃┓┏-_-•by @donydaily_-_-_-••
••-_-┣┛┗┫-_-_-_-_-_-_-_-_-_-_-_-••
••_-_┏┳┓┛_-_-_-┓-_-_-_-_-_-_-_-_••
••-_-_┃ ┏┓┏┓┏┓┏┃┏┓╋┏┓_-_-_-_-_-_••
••- - ┻ ┛ ┗┻┛┗┛┗┗┻┗┗- - - - - - ••
""")

def display_languages():
    print("•"*34)
    print("Available languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")
    print("•"*34)    

def get_language_code(prompt):
    lang_code = input(prompt).strip()
    if lang_code not in LANGUAGES:
        print("Invalid language code. Using default 'en' (English).")
        return lang_code
        #lang_code = 'en'
    return lang_code

def translate_text(text, src_lang='en', dest_lang='id'):
    # Inisialisasi penerjemah
    translator = GoogleTranslator(source=src_lang, target=dest_lang)
    # Tampilkan pesan proses
    print("\nProcessing your translation, please wait...")
    time.sleep(2)
    # Terjemahkan teks
    return translator.translate(text)

def handle_user_choice():
    while True:
        user_choice = input("Do you want to translate another text? (y/n): ").strip().lower()
        if user_choice == 'y':
            time.sleep(1)
            clear()
            return True
        elif user_choice == 'n':
            print("Thank you for using the translator. Goodbye!")
            time.sleep(1)
            clear()
            exit()
        elif user_choice == '':
            print("Invalid choice. Please enter 'y' or 'n'.")
            time.sleep(1)
            clear()
            main()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
            time.sleep(1)
            clear()
            main()

def main():
    while True:
        clear()
        banner()
        display_languages()
        # Minta pilihan bahasa sumber dari pengguna
        src_lang = get_language_code("\nSource language code: ")
        # Minta pilihan bahasa tujuan dari pengguna
        dest_lang = get_language_code("Target language code: ")
        # Minta teks dari pengguna
        text_to_translate = input(f"Text to translate from {LANGUAGES[src_lang]} to {LANGUAGES[dest_lang]}: ")
        # Terjemahkan teks dengan jeda waktu
        translated_text = translate_text(text_to_translate, src_lang, dest_lang)
        print("•"*34)
        # Tampilkan hasil terjemahan
        print(f"Original text ({LANGUAGES[src_lang]}): {text_to_translate}")
        print(f"Translated text ({LANGUAGES[dest_lang]}): {translated_text}")
        print("•"*34)
        # Tangani pilihan pengguna untuk keluar atau ulangi
        if not handle_user_choice():
            clear()
            main()

if __name__ == "__main__":
    main()

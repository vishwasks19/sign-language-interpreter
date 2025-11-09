from gtts import gTTS
from googletrans import Translator
from playsound import playsound
import time
import os

def text_to_speech_in_language(text, lang_code):
    translator = Translator()
    translation = translator.translate(text, src="en", dest=lang_code)
    translated_text = translation.text
    print(f"Translated text in {lang_code}: {translated_text}")
    current_time = time.strftime("%Y%m%d_%H%M%S") + f"_{int((time.time() % 1) * 1000):03d}"
    audio_folder = "audio"
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    
    # Define the audio file path in the audio folder
    audio_file = os.path.join(audio_folder, f"response_{lang_code}_{current_time}.mp3")
    
    tts = gTTS(text=translated_text, lang=lang_code)
    tts.save(audio_file)
    playsound(audio_file)
    time.sleep(1)
if __name__=="__main__":
    text_to_speech_in_language("Hello, how are you?", "hi")
    text_to_speech_in_language("Hello, how are you?", "ta")

import pygame
from gtts import gTTS
import io

# Initialize the pygame mixer
pygame.mixer.init()

# Function to play speech directly
def play_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    
    # Save to an in-memory byte stream
    mp3_data = io.BytesIO()
    tts.save(mp3_data)
    
    # Move the cursor to the beginning of the BytesIO stream
    mp3_data.seek(0)

    # Load the in-memory MP3 file into pygame
    pygame.mixer.music.load(mp3_data)
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# For Hindi
play_speech("नमस्ते, कैसे हो?", lang='hi')

# For Kannada
# play_speech("ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?", lang='kn')

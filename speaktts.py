from gtts import gTTS

# For Hindi
tts_hindi = gTTS("नमस्ते, कैसे हो?", lang='hi')
tts_hindi.save("hindi_output.mp3")

# For Kannada
tts_kannada = gTTS("ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?", lang='kn')
tts_kannada.save("kannada_output.mp3")

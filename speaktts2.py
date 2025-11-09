import pyttsx3

engine = pyttsx3.init()

# For Hindi (Make sure the Hindi voice is installed)
engine.setProperty('language', 'hi')
engine.say("नमस्ते, आप कैसे हैं?")
engine.runAndWait()

# For Kannada (Make sure the Kannada voice is installed)
engine.setProperty('language', 'kn')
engine.say("ಹಲೋ, ನೀವು ಹೇಗಿದ್ದೀರಿ?")
engine.runAndWait()

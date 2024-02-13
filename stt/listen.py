import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")

    # Adjust ambient noise for better recognition (optional)
    recognizer.adjust_for_ambient_noise(source)

    # Record audio from the microphone
    audio = recognizer.listen(source)

try:
    print("Recognizing...")
    # Use Google Web Speech API (requires internet connection)
    text = recognizer.recognize_google(audio)

    # Use CMU Sphinx (offline speech recognition engine)
    # text = recognizer.recognize_sphinx(audio)

    print("Recognized Text:", text)

except sr.UnknownValueError:
    print("Speech recognition could not understand audio.")

except sr.RequestError as e:
    print("Could not request results from Speech Recognition service:", str(e))
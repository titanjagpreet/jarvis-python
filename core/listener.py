import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    global recognizer
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.7)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        text = recognizer.recognize_google(audio)
        return text.lower().strip()

    except:
        return ""

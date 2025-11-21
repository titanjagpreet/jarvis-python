import pyttsx3
import threading
import queue

engine = pyttsx3.init()
speech_queue = queue.Queue()

def _tts_loop():
    while True:
        text = speech_queue.get()
        if text is None:
            break  # exit loop
        engine.say(text)
        engine.runAndWait()
        speech_queue.task_done()

# Start 1 background thread for TTS
tts_thread = threading.Thread(target=_tts_loop, daemon=True)
tts_thread.start()

def speak(text):
    speech_queue.put(text)

from core.listener import listen
from core.speaker import speak
from core.agent import ask_gpt
import json

from tools.browser import open_website, search_google, search_youtube
from tools.apps import open_app
from tools.music import play_music
from tools.system import system_command

if __name__ == "__main__":
    speak("Jarvis online.")

    while True:
        command = listen()
        if not command:
            continue

        speak("Processing...")
        raw = ask_gpt(command)

        try:
            action = json.loads(raw)
        except:
            speak("Sorry, I had trouble understanding.")
            continue

        if action["action"] == "open_website":
            open_website(action["url"])
        
        elif action["action"] == "search_website":
            search_google(action["query"])

        elif action["action"] == "play_music":
            play_music(action["query"])

        elif action["action"] == "open_app":
            if not open_app(action["name"]):
                speak(f"I couldn't find {action['name']} on your system.")

        elif action["action"] == "system_command":
            system_command(action["command"])

        elif action["action"] == "response":
            speak(action["text"])

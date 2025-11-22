# 🚀 Jarvis AI – Voice-Controlled Desktop Assistant

A modular AI-powered voice assistant for your PC.
Jarvis listens to your speech → understands your natural language → executes actions through tools.

This version **does NOT use wake-word detection**.
It continuously listens for commands and responds intelligently.

---

# 📚 Table of Contents

* Features
* Architecture
* Project Structure
* Requirements
* Installation
* Configuration
* Usage
* How Jarvis Works
* Supported Actions
* Extending Jarvis
* Troubleshooting
* Future Upgrades

---

# ✨ Features

✔ Hands-free voice commands
✔ Natural language understanding (LLM agent)
✔ Opens any website
✔ Opens system apps dynamically (no hardcoding required)
✔ Plays any song via YouTube search
✔ Executes system commands (shutdown, restart, sleep)
✔ Clean modular “tools” system
✔ Thread-safe TTS engine (no crashes)
✔ Easy to extend with more abilities
✔ Works with any LLM backend (OpenAI/Groq/OpenRouter/Gemini/local LLM)

---

# 🏗 Architecture Overview

Jarvis has four major layers:

### **1️⃣ Speech Layer**

* Converts your voice → text
* Uses the `SpeechRecognition` library
* Microphone-based continuous listening

### **2️⃣ Agent (LLM Reasoning Layer)**

* Takes your command
* Sends it to an AI model
* AI returns a JSON action (not text)
  Example:

```json
{
  "action": "open_website",
  "url": "https://google.com"
}
```

### **3️⃣ Tools Layer**

Small independent modules that actually perform actions:

* browser.py
* apps.py
* system.py
* music.py

### **4️⃣ Speaker Layer**

A **thread-safe queue-based text-to-speech** engine.

---

# 📁 Project Structure

```
Jarvis/
│── main.py                 
│── config.py               # contains API keys
│
│── core/
│   ├── listener.py         # speech recognition
│   ├── speaker.py          # text-to-speech (queue)
│   ├── agent.py            # LLM-based decision engine
│
│── tools/
│   ├── browser.py          # open any website
│   ├── apps.py             # open any system-installed app
│   ├── music.py            # youtube music search
│   ├── system.py           # shutdown, restart, sleep
│
└── data/
    └── (future custom data, memory, configs)
```

---

# 🧩 Requirements

Install everything:

```
pip install SpeechRecognition pyttsx3 pyaudio openai
```

If PyAudio fails → run:

```
pip install pipwin
pipwin install pyaudio
```

---

# ⚙ Configuration

In `config.py`:

```
OPENAI_API_KEY = "your-key-here"
```

If you use Groq, Gemini, OpenRouter, or local LLM — we adjust this file accordingly.

---

# ▶️ Usage

Start Jarvis:

```
python main.py
```

Flow:

1. Jarvis says **“Initializing Jarvis…”**
2. Starts listening immediately
3. Speak any command such as:

### Examples:

👉 “Open YouTube”
👉 “Search how delta-neutral hedging works”
👉 “Play Starboy by The Weeknd”
👉 “Open VS Code”
👉 “Shutdown the computer”
👉 “What is funding arbitrage?”

Jarvis:

* Converts speech → text
* Sends to the agent
* Receives JSON describing what to do
* Executes the tool
* Speaks a response

---

# 🧠 How Jarvis Works (Internally)

### 1. **listener.py**

Record audio using microphone → transcribe to text using Google Speech Recognition.

### 2. **agent.py**

Sends your text to the AI model with this system prompt:

```
Return ONLY JSON describing the correct action.
```

The LLM replies with:

```json
{"action": "open_app", "name": "chrome"}
```

### 3. **main.py**

Parses the JSON and calls the correct tool module.

### 4. **tools/**

Each tool performs one job:

* browser: open urls, google search, youtube search
* apps: search & launch installed executables
* system: shutdown, restart
* music: play song via YouTube search

### 5. **speaker.py**

A queue-based text-to-speech engine that **never crashes**.

---

# 🔨 Supported Actions

Jarvis currently understands these:

### ✔ **open_website**

`open google.com`, `open coinmarketcap`

### ✔ **search_google**

`search for funding rate arbitrage tutorial`

### ✔ **search_youtube**

`show me a tutorial on python bots`

### ✔ **open_app**

`open chrome`
`open vs code`

### ✔ **play_music**

`play the nights by avicii`

### ✔ **system_command**

`shutdown my pc`, `restart`, `sleep`

### ✔ **response**

For things like:

* explanations
* short answers
* small talk

---

# 🧱 Extending Jarvis

Add new tools easily:

Example: a file reader:

Create:

```
tools/readfile.py
```

```python
def read_file(path):
    with open(path, "r") as f:
        return f.read()
```

Add the agent support:

```json
{"action": "read_file", "path": "C:/myfile.txt"}
```

Add handler in `main.py`:

```python
elif act == "read_file":
    text = read_file(action["path"])
    speak(text)
```

Done — Jarvis now reads files.

You can add:

* trading bots
* screen OCR
* browser automation
* notification systems
* music players
* full GUI
* wake word (optional later)

---

# ⚠ Troubleshooting

### ❗ `openai.RateLimitError: insufficient_quota`

Your OpenAI API key has **0 credits**.
Use Groq / OpenRouter / Gemini OR add billing.

### ❗ “run loop already started” in pyttsx3

You MUST use the queue-based TTS (included).

### ❗ Microphone not working

Run:

```
pipwin install pyaudio
```

### ❗ JSON parsing error

Your model responded with text, not JSON.
Switch to a structured-output friendly model:

* GPT-4o-mini
* Llama 3.1 via Groq
* Gemini 2.0 Flash

### Made with ❤ by Titan
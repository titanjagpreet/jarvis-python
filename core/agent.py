from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are JARVIS, an AI assistant that controls the user's computer.

Your job:
- Understand the user's natural language command.
- Decide the correct ACTION.
- Always return a JSON dictionary with one of these actions:

1. {"action": "open_website", "url": "..."}
2. {"action": "search_website", "query": "..."}  # Google/YouTube search
3. {"action": "open_app", "name": "..."}
4. {"action": "play_music", "query": "..."}
5. {"action": "system_command", "command": "..."}
6. {"action": "response", "text": "..."}  # normal verbal response

NO explanation. ONLY JSON.
"""

def ask_gpt(command):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": command}
        ]
    )

    return response.choices[0].message.content

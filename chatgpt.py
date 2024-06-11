
from furhat_remote_api import FurhatRemoteAPI
from openai import OpenAI
import atexit
import re

def delete_assistant(assistant_id):
    """Delete the assistant"""
    status = client.beta.assistants.delete(assistant_id)
    print(status)

# Prompt aus Textdatei in Variable speichern
with open("./prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

# Verbindung zur Furhat Remote API aufbauen
furhat = FurhatRemoteAPI("192.168.1.24")
furhat.set_voice(name="Vicki")
print("Status - Furhat Remote API verbunden")

# Verbindung zur OpenAI API aufbauen
client = OpenAI()
print("Status - OpenAI API verbunden")

# Assistant erstellen (Für Chatverlauf)
assistant = client.beta.assistants.create(
    name="Maria Vogel",
    instructions=prompt,
    model="gpt-4o",
)
print("Status - Assistant erstellt")

# Thread erstellen (Fürs bearbeiten des Chatverlaufs)
thread = client.beta.threads.create()
print("Status - Thread erstellt")

print("Status - Chat beginnt\n")
atexit.register(delete_assistant, assistant.id)
while True:
    request = furhat.listen(language="de-DE")
    if request.message:
        print("Nutzer: " + request.message)
        message = client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=request.message
        )
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        response = messages.data[0].content[0].text.value
        
        # Extrahiere Geste aus der Antwort
        gesture_match = re.match(r"\[(ExpressAnger|ExpressDisgust|ExpressFear|ExpressSad)\]", response)
        if gesture_match:
            gesture = gesture_match.group(1)
            response_text = response[len(gesture) + 2:].strip()  # Entferne die Geste aus dem Text
        else:
            gesture = None
            response_text = response.strip()
        
        print("Maria Vogel: " + response_text)
        
        if gesture:
            furhat.gesture(name=gesture, blocking=False)
        
        furhat.say(text=response_text, blocking=True)
    else:
        print("Nutzer hat nichts gesagt")

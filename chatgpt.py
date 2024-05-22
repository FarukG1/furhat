from furhat_remote_api import FurhatRemoteAPI
from openai import OpenAI

# Prompt aus Textdatei in Variable speichern
with open("./prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

# Verbindung zur Furhat Remote API aufbauen
furhat = FurhatRemoteAPI("localhost")
furhat.set_voice(name="Marlene")
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
        print("Maria Vogel: " + response)
        furhat.say(text=response, blocking=True)
    else:
        print("Nutzer hat nichts gesagt")

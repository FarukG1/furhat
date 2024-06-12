from furhat_remote_api import FurhatRemoteAPI
from openai import OpenAI
import atexit
import re

# Terminal Farben
class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored(color, text):
    """Fügt Farbe zum Text hinzu."""
    return f"{color}{text}{colors.RESET}"

def programm_exit(assistant_id):
    """Löscht den Assistenten und setzt die LED Farbe auf schwarz."""
    client.beta.assistants.delete(assistant_id)
    furhat.set_led(red=0, green=0, blue=0)
    print(colored(colors.PURPLE + colors.BOLD,"Status - Chat beendet"))


# Prompt aus Textdatei in Variable speichern
with open("./prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

# Verbindung zur Furhat Remote API aufbauen
furhat = FurhatRemoteAPI("localhost")
furhat.set_voice(name="Vicki")
print(colored(colors.PURPLE + colors.BOLD,"Status - Furhat Remote API verbunden"))

# Verbindung zur OpenAI API aufbauen
client = OpenAI()
print(colored(colors.PURPLE + colors.BOLD,"Status - OpenAI API verbunden"))

# Assistant erstellen (Für Chatverlauf)
assistant = client.beta.assistants.create(
    name="Maria Vogel",
    instructions=prompt,
    model="gpt-4o",
)
print(colored(colors.PURPLE + colors.BOLD,"Status - Assistant erstellt"))

# Thread erstellen (Fürs bearbeiten des Chatverlaufs)
thread = client.beta.threads.create()
print(colored(colors.PURPLE + colors.BOLD,"Status - Thread erstellt"))

print(colored(colors.PURPLE + colors.BOLD,"Status - Chat beginnt"))
atexit.register(programm_exit, assistant.id)
while True:
    # Fokus auf den Benutzer mit geringster Entfernung
    furhat.attend(user="CLOSEST")

    # Nutzer zuhören
    print(colored(colors.GREEN,"\nFurhat - Zuhören"))
    furhat.set_led(red=0, green=255, blue=0)
    request = furhat.listen(language="de-DE")
    while not request.message:
        print(colored(colors.ERROR,"Furhat - Nutzer hat nichts gesagt, es wird erneut zugehört"))
        request = furhat.listen(language="de-DE")

    furhat.set_led(red=255, green=0, blue=0)
    # Nutzeranfrage als Nachricht im Thread erstellen
    message = client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=request.message
    )
    # Thread ausführen
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    messages = client.beta.threads.messages.list(thread_id=thread.id)
    # "ß" mit "ss" ersetzen, da die Stimme "ß" nicht korrekt ausspricht
    response = messages.data[0].content[0].text.value.replace("ß", "ss")

    # Antwort aufteilen
    response_splitted = re.split(r"\[(\w+)\]", response)

    if len(response_splitted) > 1:
        index = 1
        loop = True
        while loop:
            if index < len(response_splitted):

                # Geste ausführen
                response_gesture = response_splitted[index]
                print(colored(colors.CYAN,"\nFurhat - Gestikuliert: " + response_gesture))
                furhat.gesture(name=response_gesture, blocking=False)

                # Antwort ausgeben
                response_text = response_splitted[index + 1]
                print(colored(colors.BLUE,"Furhat - Spricht: " + response_text))
                furhat.say(text=response_text, blocking=True)

                index += 2
            else:
                loop = False
    else:
        # Antwort ausgeben
        print(colored(colors.BLUE,"\nFurhat - Spricht: " + response))
        furhat.say(text=response, blocking=True)

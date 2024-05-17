from furhat_remote_api import FurhatRemoteAPI
import openai
import os
from dotenv import load_dotenv

load_dotenv()
#Verbindung zur Furhat Remote API aufbauen
furhat = FurhatRemoteAPI("localhost")

voices = furhat.get_voices()

furhat.set_voice(name='Marlene')

#API einbinden
openai.api_key = os.getenv("API_KEY")

# Prompt aus Textdatei in Variable speichern
with open('./prompt.txt', 'r', encoding='utf-8') as file:
    prompt = file.read()

message = [{"role": "user", "content": prompt}]

# ChatGPT anfrage mit dem Prompt erstellen
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=message
)

# Antwort wird rausgefiltert und in openai_response speichern
openai_response = response['choices'][0]['message']['content'].strip()
furhat.say(text=openai_response, blocking = True)


while True:
    # TO-DO: Dafür sorgen dass Furhat erst dann anfängt zu hören wenn er fertig geredet hat. HINWEIS: Parameter Blocking anschauen
    # Furhat hört zu und das gesagte wird in result gespeichert
    #result = furhat.listen(language="de-DE")  
    anfrage = input("Helf Maria: ")
    # ChatGPT Anfrage mit Result erstellen
    message.append({"role": "user", "content": anfrage})
    response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=message
    )

    # Antwort wird rausgefiltert und in openai_response gespeichert
    openai_response = response['choices'][0]['message']['content'].strip()

    # Furhat sagt die antwort
    furhat.say(text=openai_response)
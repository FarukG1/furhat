from furhat_remote_api import FurhatRemoteAPI
import time

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
furhat = FurhatRemoteAPI("localhost")

# Get the voices on the robot
voices = furhat.get_voices()

#print(voices)

# Set the voice of the robot
furhat.set_voice(name='Hans')

# Begrüßung
furhat.say(text="Hallo, wer sind Sie?")  # Warten, bis das Sprechen beendet ist

# Fokus auf den Benutzer mit geringster Entfernung
furhat.attend(user="CLOSEST")

while True:
    time.sleep(3)
    furhat.gesture(name="BigSmile")
    # Listen to user speech and return ASR result
    result = furhat.listen(language="de-DE")  # Blockieren bis Hören beendet ist

    # Check if the user wants to stop the conversation
    if result.message == "Stopp":
        print("User stopped the conversation")
        break

    # Echo only the user's speech
    furhat.say(text=result.message)  # Warten, bis das Sprechen beendet ist
    
furhat.say(text="Tschüss")

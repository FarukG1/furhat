from furhat_remote_api import FurhatRemoteAPI

# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
furhat = FurhatRemoteAPI("localhost")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Hans')

# Begrüßung
furhat.say(text="Hallo wer sind sie?")

# Fokus auf den benutzer mit geringster entfernung
furhat.attend(user="CLOSEST")

while(True):
    # Listen to user speech and return ASR result
    result = furhat.listen(language="de-DE")

    # Abbruchbedingung
    if result.message == "Stopp":
        print("User stopped the conversation")
        break

    # Echo the user's speech
    furhat.say(text=result.message)

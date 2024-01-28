# Author: S-Tech @ Youtube

import speech_recognition as sr
import time

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Test")
        audio = r.listen(source)
        query = ''

        try:
            print("Hearing")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Exception: " + str(e))
            return ''  # Return an empty string if speech recognition fails

if __name__ == "__main__":
    while True:
        spoken = takeCommand()
        if "help" in spoken:
            print("User said help")
        time.sleep(2)

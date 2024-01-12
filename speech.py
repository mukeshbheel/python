import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
name = input("Name : ")

engine.say(f"Hello")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        engine.say(command)
        engine.runAndWait
except:
    pass
import pyttsx3

engine = pyttsx3.init()

text = "Hello"
engine.say(text)
engine.runAndWait()

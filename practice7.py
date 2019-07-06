import speech_recognition as sr
import pyaudio
r=sr.Recognizer()
with sr.Microphone()as source:
    audio=r.listen(source)
try:
    print("audio files contain:"+ r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition did not understand")



import pyaudio
import speech_recognition as sr
# i = sr.Microphone.list_microphone_names()
mic = sr.Microphone(1)

recog = sr.Recognizer()

with mic as source:
    while True:
        audio = recog.listen(source)
        try:
            result = recog.recognize_google(audio, language='en')
            print(result)
        except:
            continue

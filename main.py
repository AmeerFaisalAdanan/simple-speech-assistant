import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS



r = sr.Recognizer()

def record_audio(ask=False):

    with sr.Microphone() as source:
        if ask:
            kaede_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            kaede_speak('Sorry, I did not get that!')
        except sr.RequestError:
            kaede_speak('Sorry, my speech service is not activated')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        kaede_speak('My name is Kaede')
    if 'what time is it' in voice_data:
        kaede_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        kaede_speak('Here is what i found for '+ search)
    if 'bye' in voice_data:
        kaede_speak('See ya!')
        exit()


def kaede_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)
kaede_speak('Hi, how can i help')
while 1:
    voice_data = record_audio()
    respond(voice_data)

import pyttsx3
import datetime
import speech_recognition as sr
import os


# sapi5 is the microsoft speech recognition API
engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')

# voice [0] stands for  male(David) voice, 1 for unknown(hazel) & 2 for female(zira) voice
engine.setProperty('voice',voices[0].id) 
# print(voices[2].id) # <== checking the voices

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
        datetime_in_string = datetime.datetime.now().strftime("%H,%M")
        formt_time = datetime_in_string.replace(','," ")
        spk_time ="the time is "+formt_time+"AM"
        speak(spk_time)
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        datetime_in_string = datetime.datetime.now().strftime("%H,%M")
        formt_time = datetime_in_string.replace(','," ")
        spk_time ="the time is "+formt_time+"PM"
        speak(spk_time)
    else:
        speak("Good Evening")
        datetime_in_string = datetime.datetime.now().strftime("%H,%M")
        formt_time = datetime_in_string.replace(','," ")
        spk_time ="the time is "+formt_time+"PM"
        speak(spk_time)


    # speak(datetime.datetime.now())

if __name__ == "__main__":
    wishme()
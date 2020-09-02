import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


# sapi5 is the microsoft speech recognition API
engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')

# voice [0] stands for  male(David) voice, 1 for unknown(hazel) & 2 for female(zira) voice. i used david here.
engine.setProperty('voice',voices[0].id) 
# print(voices[2].id) # <== checking the voices

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Chhotta bhheeem. please tell me sir how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-us")
        print(f"User Said :{query}\n")
    except Exception as e:
        # print(e)  # we will not print error because the error are mostly unidentifiable for a user
        print(e,"\n Sorry! please say that again")
        return "None"
    return query

def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('saurav.sharma.zz45@gmail.com','Wrestling-india2020pAssWoRd')
     server.sendmail('saurav.sharma.zz45@gmail.com',to,content)
     server.close




if __name__ == "__main__":
    wishme()
    while True: 
        query= takecommand().lower()
        
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia.....please wait...")
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            time_in_string = datetime.datetime.now().strftime('%H:%M:%S')
            print('the time is',time_in_string)
            speak(f'Sir, the time is {time_in_string}')

        elif 'open code' in query:
            code_path = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)

        elif 'send email' in query:
            try:
                speak('what should i say')
                content = takecommand()
                to = "saurav.sharma.zz45@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("i am sorry my friend saurav sharma. i am unable to send the email at this time.. there is some problem in my programming.")
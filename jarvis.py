import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
import pywhatkit
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ")

    elif hour>=12 and hour<18:
        speak("Good afternoon ")

    else:
        speak("Good evening ")

    speak("i am jarvis how can i help you")

def takeCommand():

    #for mic input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" I am listning now...")
        r.pause_threshold = 0.8
        r.non_speaking_duration = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing sir...")
        command = r.recognize_google(audio,language='en-in')
        print("user said:", command) 
        
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return command

def whatsapp():
    speak('tell me the name of person')
    name = takeCommand().lower()

    if 'kalpesh' in name:
        speak('what is the message tell me sir.')
        msg = takeCommand()
        speak('sir, at what time you want to send message')
        speak('tell me the only number of hour')
        hour = int(takeCommand())
        speak('tell me the minutes')
        minutes = int(takeCommand())
        pywhatkit.sendwhatmsg("+919326545595",msg,hour,minutes,20)
        speak('sir, message is now sending please wait!')

    elif 'pooja' in name or 'puja' in name:
        speak('what is the message tell me sir.')
        msg = takeCommand()
        speak('sir, at what time you want to send message')
        speak('tell me the only number of hour')
        hour = int(takeCommand())
        speak('tell me the minutes')
        minutes = int(takeCommand())
        pywhatkit.sendwhatmsg("+918424074993",msg,hour,minutes,20)
        speak('sir, message is now sending please wait!')

    elif 'pradeep' in name or 'Pradip' in name:
        speak('what is the message tell me sir.')
        msg = takeCommand()
        speak('sir, at what time you want to send message')
        speak('tell me the only number of hour')
        hour = int(takeCommand())
        speak('tell me the minutes')
        minutes = int(takeCommand())
        pywhatkit.sendwhatmsg("+917304090923",msg,hour,minutes,20)
        speak('sir, message is now sent!')

    elif 'rohit' in name:
        speak('what is the message tell me sir.')
        msg = takeCommand()
        speak('sir, at what time you want to send message')
        speak('tell me the only number of hour')
        hour = int(takeCommand())
        speak('tell me the minutes')
        minutes = int(takeCommand())
        pywhatkit.sendwhatmsg("+919167690040",msg,hour,minutes,10)
        speak('sir, message is now sent!')

    if 'rahul' in name:
        speak('what is the message tell me sir.')
        msg = takeCommand()
        speak('sir, at what time you want to send message')
        speak('tell me the only number of hour')
        hour = int(takeCommand())
        speak('tell me the minutes')
        minutes = int(takeCommand())
        pywhatkit.sendwhatmsg("+918898726788",msg,hour,minutes,10)
        speak('sir, message is now sent!')
    
    if 'gaurav' in name:
        speak('what is the message tell me sir.')
        msg = takeCommand()
        speak('sir, at what time you want to send message')
        speak('tell me the only number of hour')
        hour = int(takeCommand())
        speak('tell me the minutes')
        minutes = int(takeCommand())
        pywhatkit.sendwhatmsg("+919167950567",msg,hour,minutes,10)
        speak('sir, message is sent now!')

    if 'unknown' in name:
        speak('type the number sir')
        a= "+91"
        b =input("enter the number: ")
        num = a+b
        speak('what is the message tell me sir.')
        msg = takeCommand()
        speak('sir, at what time you want to send message')
        speak('tell me the only number of hour')
        hour = int(takeCommand())
        speak('tell me the minutes')
        minutes = int(takeCommand())
        pywhatkit.sendwhatmsg(num,msg,hour,minutes,10)
        speak('sir, message is sent now!')


def perform():

    #wishMe()
    while True:

        command = takeCommand().lower()

        # logic building for tasks 

        if 'wikipedia' in command:
            speak('searchng wikipedia...')
            command = command.replace('wikipedia',"")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'play ' in command:
            song = command.replace('play','')
            speak('playing'+ song)
            pywhatkit.playonyt(song)

        elif 'open file' in command or 'file exporer' in command:
            filepath = "C:\\Users\\Admin\\OneDrive\\Desktop"
            os.startfile(filepath)


        elif 'open youtube' in command:
            speak('opening youtube')
            webbrowser.open("youtube.com")
        
        elif 'open google' in command:
            speak('google is opened. now search anything')
            webbrowser.open("google.com")

        elif 'jarvis' in command or 'jarvis are you listening' in command:
            speak('yes sir, i am listening')
        
        elif 'how are you' in command:
            speak('I am working properly sir, whats about you ')

        elif 'i am good' in command:
            speak('Its awesome, what can i do for you sir')

        elif 'hindi song' in command:
            webbrowser.open("https://www.youtube.com/watch?v=1c2Y5EShSSg")

        elif 'send message' in command or 'send message on whatsapp' in command or 'send a whatsapp message' in command:
            whatsapp()

        elif ' english song' in command:
            webbrowser.open("https://www.youtube.com/watch?v=a8Foq32Qr90")

        elif ' punjabi song' in command:
            webbrowser.open("https://www.youtube.com/watch?v=SAN0IDZAHME")
        elif ' marathi news' in command:
            webbrowser.open("https://www.youtube.com/watch?v=-Ku6BOxFIkc")

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M %p")
            speak(f"sir, the time is {strTime}")

        elif 'open pycharm'in command:
            codepath="F:\\Program Files\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe"
            speak('opening paycharm please wait sir till the pychamr open properly')
            os.startfile(codepath)

        elif 'open notepad' in command:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)
            speak("notepad is opened")

        elif 'open vs code' in command or 'open vscode' in command:
            path = "E:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            speak('opening sir')

        elif 'close notepad' in command or 'close the notepad' in command:
            os.system("taskkill /f /im notepad.exe")
            speak('notepad is closed')


        elif 'close vs code' in command or 'close vscode' in command:
            os.system("taskkill /f /im Code.exe")
            speak('vs code is closed')

        elif 'open chrome' in command:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening chrome browser")
            os.startfile(path)

        elif 'new file' in command:
            keyboard.press_and_release('Windows logo key+I')


        

        elif ('you can sleep' in command or 'sleep now' in command or 'stop listening' in command) :
            speak('okay sir, i am going to sleep you can call me any time i will be there to help you. Bye sir you can do your work now')
            break


if __name__ == "__main__":
    while True:
        permission = takeCommand().lower()
        if 'listen jarvis' in permission or 'hey jarvis' in permission or 'wake up' in permission or 'hi jarvis' in permission:
            speak('hello sir')
            perform()
        elif 'jarvis' in permission:
            speak('yes,sir')
            perform()

        elif 'good bye' in permission or 'goodbye' in permission:
            speak('Thanks for using me sir, you can access me any time by going to your desktop home screen . have a good day sir. bye')
            sys.exit()


   

























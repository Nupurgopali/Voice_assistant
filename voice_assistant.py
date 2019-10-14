from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import pyttsx3
import pyjokes



def talkToMe(audio):
    "speaks audio passed as argument"
    #tts=gTTS(text=audio,lang='en')
    #tts.save('audio.mp3')
    #os.system('mpg123 audio.mp3') 
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()






def myStatement():
    "listens for commands"

    rc = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        rc.pause_threshold = 1
        rc.adjust_for_ambient_noise(source, duration=1)
        audio = rc.listen(source)

    try:
        command = rc.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myStatement();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open google' in command:
        a_website = "https://www.google.com"
       # Open url in a new window of the default browser, if possible
        webbrowser.open_new(a_website)
        print('Done!')
        talkToMe('Google opened!')

    elif 'open youtube' in command:
        b_website = "https://www.youtube.com"
       # Open url in a new window of the default browser, if possible
        webbrowser.open_new(b_website)
        print('Done!')
        talkToMe('Youtube opened!')
 
    elif 'hello'in command :
        talkToMe('Hello,how are you?')

    elif 'joke' in command:
            jk= pyjokes.get_joke()
            print(jk)
            talkToMe(jk)
    elif 'bye' in command:
        talkToMe('Bye have a great day!')
talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myStatement())

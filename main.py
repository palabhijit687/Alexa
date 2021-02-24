import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import wikipedia as wk
import pyjokes as pk

listener = sr.Recognizer()
engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = dt.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+ time)

    elif 'wikipedia' or 'who' or 'what' in command:
        info = wk.summary(command, 1)
        print(info)
        talk(info)
    
    elif 'jokes' or 'joke' in command:
        talk(pk.get_joke())
    
    elif 'are you single' in command:
        talk('sorry i am in a relationship with the wifi')

    elif 'birthday' in command:
        talk("its on 6th october, year two thousand")

    elif 'i love you' in command:
        talk("love you too")

    
    else:
        talk("could'nt understand, please repeat it again")

while True:
    run_alexa()
import speech_recognition as sr          #this module is use as sr as you see we use for microphone access and recogonizing voice(also it is use as translator for google)
import pyttsx3                           #this is python text to speech module where we only use our system in talking way
import wikipedia                         #use for wikipedia search only take 'name' and return how many lines of 'information' you want
import datetime                          #this is use for current time and date
import pywhatkit                         #this module is use for searching in youtube
import pyaudio                           #audio input output stream library 
import pyjokes                           #jokes library for python





def talk(voice):
    engine.say(voice)
    engine.runAndWait()


engine=pyttsx3.init()
listner=sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)           #0 for female voice 1 for male voice


def take_command(): 
    try:
        with sr.Microphone() as source:
            command=''
            print("Listning....")
            listner.adjust_for_ambient_noise(source=source)    # this function is use for clear voice when voice is not coming in such a good way
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command=command.lower()
            
            if 'alexa' or 'election' in command:
                command=command.replace('alexa','')
                return command
            
    except:
        pass
    return command if command or command!='' else 'nothing'

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        if 'please' in command:
            song=command.replace('please','')
        song=command.replace('play','')
        print('Playing'+song)
        talk('Playing'+song)
        pywhatkit.playonyt(song)
        run_alexa()

    if 'tell me a joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
        run_alexa()
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
        run_alexa()
    elif 'jokes' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
        run_alexa()
        
        
    if 'who' in command:
        if 'who' in command:
            person = command.replace('who','')
        if 'search' in command:
            person = command.replace('search','')
        if 'is' in command:
            person = command.replace('is','')
        info=wikipedia.summary(person,1)       # 1 is for getting result only 1 line
        print(info)
        talk(info)
        run_alexa()
    elif 'wikipedia' in command:
        person=command.replace('wikipedia','')
        if 'who' in command:
            person = command.replace('who','')
        if 'search' in command:
            person = command.replace('search','')
        if 'is' in command:
            person = command.replace('is','')
        info=wikipedia.summary(person,1)       # 1 is for getting result only 1 line
        print(info)
        talk(info)
        run_alexa()
    elif 'the heck is' in command:
        if 'who' in command:
            person = command.replace('who','')
        if 'search' in command:
            person = command.replace('search','')
        person=command.replace('the heck is','')
        info=wikipedia.summary(person,1)       # 1 is for getting result only 1 line
        print(info)
        talk(info)
        run_alexa()
        




    if 'date' in command:
        print('OOOOOOOPS..... I have a headache')
        talk('OOOOOOOPS..... I have a headache')
        run_alexa()






    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')     #%p for (am or pm) %I for 12 hour fomat not 24 
        print(time)
        talk('current time is'+time)
        run_alexa()
    elif 'timing' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')     #%p for (am or pm) %I for 12 hour fomat not 24 
        print(time)
        talk('current time is'+time)
        run_alexa()





            
    if 'nothing' in command:
        exit(0)
        
        
run_alexa()


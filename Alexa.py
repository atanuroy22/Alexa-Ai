import time

import listener as listener
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
from wikipedia import wikipedia
import pyjokes

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice for the assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            voice_data = ''
        except sr.RequestError:
            voice_data = ''
        return voice_data.lower()



speak("Hey ")
time.sleep(0.2)
speak("I,m Alexa")
time.sleep(0.5)
speak("How can I Assist You")

# Function to process user's voice input and provide responses

    # if 'what is your name' in voice_data:
    #     speak("My name is Alexa.")
    # elif 'what time is it' in voice_data:
    #     current_time = datetime.datetime.now().strftime("%I:%M %p")
    #     speak(f"The current time is {current_time}.")

    # else:
    #     speak("I'm sorry, I didn't understand that.")

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
def process_command(voice_data):
        command = voice_data
        print(command)
        if 'wake up' in voice_data:
            is_awake = True
            speak("I am Online")

        elif 'open website' in voice_data:
            speak("Sure, which website would you like me to open?")
            website = listen()
            if website:
                url = f"https://www.{website}.com"
                webbrowser.open(url)
                speak(f"Opening {website} in your browser.")
            else:
                speak("I'm sorry,Please Tell Again.")
        elif 'open application' in voice_data:
            speak("which application?")
            application = listen()
            if application:
                os.system(f"open -a {application}")
                speak(f"Opening {application}.")
            else:
                speak("I'm sorry, I didn't catch the name.")

        elif 'play' in command:
            command = command.replace('alexa', '')
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
        elif 'what is' in command:
            person = command.replace('alexa', '')
            info = wikipedia.summary(person,3)
            print(info)
            speak(info)
        elif 'who' in command:
            person = command.replace('alexa', '')
            info = wikipedia.summary(person,3)
            print(info)
            speak(info)    
        elif 'date' in command:
            speak('sorry, I have a headache')
        elif 'are you single' in command:
            speak('I am in a relationship with wifi')
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif 'exit' in voice_data:
            speak("Goodbye!")
            exit()
        else:
        
            speak('')
# Main loop to continuously listen for user's voice input
while True:
    try:
        # speak("How can I assist you?")
        voice_input = listen()
        if voice_input:
            process_command(voice_input)
    except KeyboardInterrupt:
        break

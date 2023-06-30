import time
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import pyjokes
import pywhatkit
from os import listdir
from os.path import isfile, join
import pyautogui
import keyboard

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

def listen2():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            voice_data = ''
        except sr.RequestError:
            voice_data = ''
        return voice_data

speak("Hey")
time.sleep(0.2)
speak("I'm Alexa")
time.sleep(0.5)
speak("How can I assist you?")

# Function to process user's voice input and provide responses
def process_command(voice_data):
    command = voice_data
    if 'wake up' in voice_data:
        speak("I am online")
    elif 'open website' in voice_data:
        speak("Sure, which website would you like me to open?")
        website = listen()
        if website:
            url = f"https://www.{website}.com"
            webbrowser.open(url)
            speak(f"Opening {website} in your browser.")
        else:
            speak("I'm sorry, please tell me again.")

            #Open application or folder in c/user/atanu
    elif 'open folder' in voice_data:
        speak("Which folder or application in atanu folder?")
        try:
           application = listen2()
           if application:
               os.startfile(application)
               speak(f"Opening {application}.")
           else:
               speak("I'm sorry, I didn't catch the name.")
        except:
            speak("file not found")
    
    elif 'play' in command:
        command = command.replace('alexa', '')
        song = command.replace('play', '')
        speak('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak('The current time is ' + current_time)
    elif 'what is' in command or 'who' in command:
        person = command.replace('alexa', '')
        info = wikipedia.summary(person, sentences=2)
        print(info)
        speak(info)
    elif 'date' in command:
        speak("Sorry, I have a headache.")
    elif 'are you single' in command:
        speak('I am in a relationship with Wi-Fi.')
    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'code' in voice_data:
        speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('code')[1])
        a = voice_data.lstrip("alexa ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            speak('Wait a moment')
        except:
            speak('Please check your Internet')

    elif 'write' in voice_data:
        speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('write')[1])
        a = voice_data.lstrip("alexa ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            speak('Wait a moment')
        except:
            speak('Please check your Internet')
            
    elif 'give' in voice_data:
        speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('give')[1])
        a = voice_data.lstrip("alexa ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            speak('Wait a moment')
        except:
            speak('Please check your Internet')
            
    elif 'tell' in voice_data:
        speak('Please Wait a Moment Wile Generating From an Ai' + voice_data.split('tell')[1])
        a = voice_data.lstrip("alexa ")
        search_query = a.replace(" ", "+")
        url = 'https://www.perplexity.ai/search?q=' + search_query
        try:
            webbrowser.get().open(url)
            speak('Wait a moment')
        except:
            speak('Please check your Internet')
            
    elif 'pause' in command:
        # Simulate spacebar press to pause/play
        keyboard.press('space')
        keyboard.release('space')
        speak("Playback paused.")
        
    elif 'fast' in command:
        # Simulate spacebar press to >
        keyboard.press('shift')
        keyboard.press('>')
        
        keyboard.release('shift')
        keyboard.release('>')
        speak("speed fast.")

    elif 'slow' in command:
        # Simulate spacebar press to <
        keyboard.press('shift')
        keyboard.press('<')
        
        keyboard.release('shift')
        keyboard.release('<')
        speak("speed Slowed.")

    elif 'full' in command:
        # Simulate spacebar press to full screen
        keyboard.press('f')
        keyboard.release('f')
        speak("full screen.")
                
    elif 'skip five' in command:
        # Simulate spacebar press to right
        keyboard.press('right')
        keyboard.release('right')
        speak("skipped 5 seconds.")
    
    elif 'skip ten' in command:
        # Simulate spacebar press to l
        keyboard.press('l')
        keyboard.release('l')
        speak("skipped 10 seconds.")

    elif 'next' in command:
        # Simulate right arrow press to play next video
        keyboard.press('shift')
        keyboard.press('n')
        
        keyboard.release('shift')
        keyboard.release('n')
        speak("Playing next video.")

    elif 'previous' in command:
        # Simulate left arrow press to play previous video
        keyboard.press('shift')
        keyboard.press('p')
        
        keyboard.release('shift')
        keyboard.release('p')
        speak("Playing previous video.")

    elif 'mute' in command:
        # Simulate left arrow press to play previous video
        keyboard.press('m')
        keyboard.release('m')
        speak("Video is now mute.")
    
    elif 'volume up' in command:
        # Simulate left arrow press to volume up
        keyboard.press('up')
        keyboard.release('up')
        speak("Volume up.")

    elif 'volume down' in command:
        # Simulate left arrow press to volume down
        keyboard.press('down')
        keyboard.release('down')
        speak("Volume down.")

    elif 'stop' in command:
        # Simulate spacebar press to stop playback
        keyboard.press('q')
        keyboard.release('q')
        speak("Playback stopped.")

    elif 'subtitle' in command:
            # Simulate left arrow press to volume up
            keyboard.press('c')
            keyboard.release('c')
            speak("Subtitle.")
        
    elif 'mini' in command:
        # Simulate left arrow press to volume up
        keyboard.press('i')
        keyboard.release('i')
        speak("PIP mode.")    
    elif 'volume down' in command:
        # Simulate left arrow press to play volume down
        keyboard.press('down')
        keyboard.release('down')
        speak("Volume down.")
    elif 'search video' in command:
        # Simulate left arrow press to play SEARCH
        speak("Tell the video name?")
        search_query = listen()
        if search_query:
            pywhatkit.playonyt(search_query)
            speak("Searching " + search_query + ".")
        else:
            speak("I'm sorry, I didn't catch hear your voice.")

            # open a drive folder navigation

    # elif 'open' in voice_data and ('drive' in voice_data or 'folder' in voice_data or 'file' in voice_data):
    #     speak("Sure, please provide the details of the drive, folder, and file.")
    #     path = ['D:\\']
    #     current_folder = ''
    #     while True:
    #         user_input = listen().lower()
    #         if 'drive' in user_input:
    #             speak("Tell the drive name?")
    #             drive = listen2()
    #             print('drive')
    #             drive = user_input.split()[0]
    #             current_folder = fr"{drive}:/"
    #             path.append(current_folder)
    #             speak(f"Opening {drive} drive.")
    #         elif 'folder' in user_input:
    #             speak("Tell the folder name?")
    #             folder = listen2()
    #             print(folder)
    #             folder = ' '.join(user_input.split()[1:])
    #             current_folder = os.path.join(current_folder, folder)
    #             path.append(current_folder)
    #             speak(f"Opening folder {folder}.")
    #         elif 'back' in user_input:
    #             if len(path) > 1:
    #                 path.pop()
    #                 current_folder = path[-1]
    #                 speak("Going back to the previous folder.")
    #             else:
    #                 speak("You are already at the root folder.")
    #         elif 'file' in user_input:
    #             file_name = ' '.join(user_input.split()[1:])
    #             file_path = os.path.join(current_folder, file_name)
    #             if os.path.isfile(file_path):
    #                 os.startfile(file_path)
    #                 speak(f"Opening file {file_name}.")
    #             else:
    #                 speak("Sorry, the specified file was not found.")
    #         elif 'stop' in user_input:
    #             speak("Stopping folder navigation.")
    #             break
    #         else:
    #             speak("Invalid command. Please try again.")


    
    elif 'screenshot' in command:
        # Take a screenshot using prnt scrn
        keyboard.press('Alt')
        keyboard.press('Prnt Scrn')
        keyboard.release('Alt')
        keyboard.release('Prnt Scrn')
        speak("Screenshot captured & Saved To Dexktop.")
        
    elif 'close this' in command:
        # Close app
        keyboard.press('Alt')
        keyboard.press('F4')
        keyboard.release('Alt')
        keyboard.release('F4')
        speak("App Closed.")    
    
    elif 'shutdown' in command:
        speak("Shutting down")
        os.system("shutdown /s /t 1")
        
    elif 'exit' in command:
        speak("Goodbye!")
        exit()

# Main loop to continuously listen for user's commands
while True:
    voice_input = listen()
    process_command(voice_input)

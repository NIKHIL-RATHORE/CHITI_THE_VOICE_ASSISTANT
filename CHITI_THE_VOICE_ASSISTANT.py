from ast import Pass
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




eng=pyttsx3.init('sapi5')

voices=eng.getProperty('voices')
#print(voices[0].id)//TO CHECK FOR THE VOICE WE ARE USING

eng.setProperty('voice',voices[0].id)

def speak(audio):
#THIS FUNCTION SPEAKS WHAT EVER IS GIVEN TO IT
    eng.say(audio)
    eng.runAndWait()

def wishme():
#TO GREET THE USER WHENEVER HE COMES
    hr=int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("GOOD MORNING!")
    elif hr>=12 and hr<18:
        speak("GOOD AFTERNOON!")
    else:
        speak("GOOD EVENING !")
    speak("I AM CHITI SIR. HOW MAY I HELP YOU")
def takecommdand():
#TO TAKE COMMANDS FROM THE USER FROM MICROPHONE AND RETURNS STRING OUTPUT
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING.....")
        r.pause_threshold=1
        r.energy_threshold=270
        audio=r.listen(source)
    try:
        print("RECOGNIZING....")
        query=r.recognize_google(audio,language='en-in')
        print(f"USER SAID: {query}\n")

    except Exception as e:
        #print(e) this is to show the error in the terminal
        print("CAN YOU REPEAT THAT AGAIN PLZ......")
        return "None"

    return query

def sendemail(to,content):
    pass


if __name__=="__main__":
    wishme()
    while True:
        query=takecommdand().lower()

# logic for executing tasks based on query
        if "wikipedia" in query:
            speak('SEARCHING WIKIPEDIA......')
            query = query.replace('wikipedia','')
            results=wikipedia.summary(query, sentences=2)
            speak("ACCORDING TO WIKIPEDIA")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open gfg' in query:
            webbrowser.open('geekforgeeks.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'youtubemusic' in query:
            webbrowser.open('youtubemusic.com')
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir, the time is {strtime}")
        elif 'open code' in query:
            path="C:\\Users\\rnikk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open chrome' in query:
            path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)        
        #elif 'email to piyush' in query:
         #   try:
          #     content=takecommdand()
           #     to="nikhilemail@gmail.com"
            ##   speak("Email has been sent")
#
 #           except Exception as e:
  #              #print(e)
   #             speak("Sorry i cant send this at the moment")
    
        elif "who are you" in query:
            content="I AM CHITI YOU COMPUTER BUDDY"
            print(content)
            speak(content)
        elif "quit" in query or "bye" in query:
            content="QUITING SIR......,SEE YOU SOON"
            print(content)
            speak(content)
            quit()
        elif "how are you" in query:
            content="I AM REALLY FINE SIR,WHAT ABOUT YOU"
            print(content)
            speak(content)
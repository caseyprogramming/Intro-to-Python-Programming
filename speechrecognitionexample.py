
import speech_recognition as sr
import sys, string, os,subprocess, webbrowser

def openAndroid():
    subprocess.Popen(r"C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe");
    
def closeAndroid():
    os.system('TASKKILL /F /IM studio64.exe')

def openWord():
    subprocess.Popen(r"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE");

def closeWord():
    os.system('TASKKILL /F /IM WINWORD.EXE')

def openMySQL():
    subprocess.Popen(r"C:\\Program Files\\MySQL\\MySQL Workbench 6.3 CE\\MySQLWorkbench.exe");

def openGoogle():
    print("What do you want me to search for?")
    audio = r.listen(source)
    webbrowser.open('https://www.google.com/search?q=' + str(r.recognize_google(audio)))
    
def closeGoogle():
    os.system('TASKKILL /F /IM CHROME.EXE')
    
def openFacebook():
    webbrowser.open('http://facebook.com')
    

# audio from the microphone
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        # using Google Speech Recognition
        try:     
            print("You said: " + r.recognize_google(audio))
            
        except sr.UnknownValueError:
            print("I could not understand audio")
            continue
              
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))

        if r.recognize_google(audio).lower() == "stop listening":
            print("GoodBye!!!")
            break
            
        if r.recognize_google(audio) == "open Google":
            openGoogle()
            print("opening google")

        if r.recognize_google(audio) == "close Google":
            closeGoogle()
            print("closing google")
            
        if r.recognize_google(audio).lower() == "open android studio":
            openAndroid()
            print("Okay I will open Android studio... give me a second ")

        if r.recognize_google(audio).lower() == "close android studio":
            print("Closing Android Studio...")
            closeAndroid()
               
        if r.recognize_google(audio) == "open Facebook":
            openFacebook()
            print("opening Facebook")

        if r.recognize_google(audio) == "open Word":
            openWord()
            print("it worked")

        if r.recognize_google(audio) == "open MySQL":
            openMySQL()
            print("it worked")

        if r.recognize_google(audio) == "open my sequel":
            openMySQL()
            print("it worked")

            
     





import speech_recognition as sr #to recognise speech
import playsound                #to play an audio
import random                   #to ganerate random number and actions ans value
from gtts import gTTS           #google text to speech
import webbrowser               #open browser
import ssl                      #secure sockets layer ......to creat secure connection b/w cilent and server
import certifi                  #full health score report for certifi, including popularity, security, maintenance & community analysis
import time                     #many awys ofrepresenting time in codes,waiting during code execution
import os                       #remove the audio files
import subprocess               #to run new codes and applications by creating new processes
from PIL import Image           #to deal with image
import pyautogui #screenshot    #ability to sumilate mouse cursor moves and clicks and keyboard buttonpress
import pyttsx3                  #text to speech .... works offline and is compatible with both python 2 ans 3
import bs4 as bs                #beautiful soap.....  pulling data out of HTML and XML files
import urllib.request           #capable of fetching URLs using a varity of different protocols

class person:
    name=''
    def setName(self, name):
        self.name=name

class asis:
    name=''
    def setName(self, name):
        self.name=name

def there_exists(terms):
    for term  in terms:
        if term in voice_data:
            return True
def engine_speak(text):
    text= str(text)
    engine.say(text)
    engine.runAndWait()

r= sr.Recognizer() #intialise the recogniser
#listen for audio and convert it to text

def record_audio(ask=""):
    with sr.Microphone() as source: #microphone as source
        if ask:
            engine_speak(ask)
        audio= r.listen(source, 5, 5) #listen for audio via source
        print("Done Listening")
        voice_data=""
        try:
            voice_data= r.recognize_google(audio) #convert audio to text
        except sr.UnknownValuError: #error : recogniser does not  understand
            engine_speak("Sorry sir,i did not get that")
        except sr.RequestError:
            engine_speak("Sorry the server is down") #the recogniser iss not connected
            print(">>", voice_data.lower()) #print what the user said
            return voice_data.lower()

# get string and make audio file to be played
def engine_speak(audio_string):
    audio_string= str(audio_string)
    tts= gTTS(text= audio_string, lang= 'en') #text to speech
    r= random.randint(1, 20000000)
    audio_file='audio' +str(r) +'.mp3'
    tts.save(audio_file)  #save as mp3
    playsound.playsound(audio_file)   #help us to play the audio
    print(asis_obj.name +":", audio_string)  #print what app said
    os.remove(audio_file) #Remove audio files

def respond(voice_data):
    #1)greeting
    if there_exists(['hello','hey','hi','hey boss','hola']):
       greetings=['hey, how can i help you'+person_obj.name,'how can i help  you'+person_obj.name]
       greet= greetings[random.randint(0, len(greetings)-1)]

    #2) name
    if there_exists(["what isyour name","tellme your name"]):
        if person_obj.name:
            engine_speak("i don't know my name, please tell me my nameby saying command your name should be,,,,what is your name ")
        else:
            engine_speak("whats your name sir")

    if there_exists(["my  name is"]):
        person_name= voice_data.split("is")[-1].strip()
        engine_speak("okay  i will remember that your name is "+person_name())
        person_obj.setName(asis_name)           #name is asis object
    
    if there_exists(["your name should be"]):
        asis_name=voice_data.split("be")[-1].strip()
        engine_speak("okay i will remember that my name is"+ asis_name)
        asis_obj.setName(asis_name) #remembeer name is asis object

    #3) greetings
    if there_exists(["how are you", "hoe are you doing"]):
        engine_speak("i am very wellthanks for asking"+ person_obj.name)


    #4) time
    if there_exists(["whats the time tell me the time"]):
        time=ctime().split(" ")[3].split(":")[0:2]
        if time[0]=="00":
            hours='12'
        else:
            hours= time[0]
            minutes=time[1]
            time=hours+"hours and "+ minutes +"minutes"
            engine_speak(time)

    #5) search goggle
    if there_exists(["search for"]) and "youtube" not in voice_data:
        search_term=voice_data.split("for")[-1]
        url="https://google.com/search?q"+ search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for"+ search_term+"on goggle")


    #6) search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url= "https://www.youtube.com/results?search_query="+ search_term
        webbrowser.get().open(url)
        engine_speak("here what i found for"+ search_term+"on youtube")

    #7) get to know the stock price
    if there_exists(['price of']):
        search_term= voice_data.split("for")[-1]
        url="https://google.com/search?q"+ search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for"+ search_term+"on goggle")

    #8) search for music
    if there_exists(["play music"]):
        search_term= voice_data.split("for")[-1]
        url= "https://open.spotify.com/search/"+search_term
        webbrowser.get.open(url)
        engine_speak("you are listening to"+search_term+"enjoy sir")

    #9) search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.amazon.in"+ search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+ search_term+ "on amazon.com")

    #10) make a note
    if there_exists(["make a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("here you can make notes")

    #11) open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")

    #12) open twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")

    #13) oen time table
    if there_exists(["show my time table"]):
        im= Image.open("D:\WhatsApp Image 2022-09-19 at 11.19.10.jpeg")
        im.show()

    #14) weather
    if there_exists(["weather","tell me weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url= "https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN1016IN1016&oq=weather&aqs=chrome..69i57.2628j0j15&sourceid=chrome&ie=UTF-8"
        webbrowser.get().open(url)
        engine_speak("here what i found about weather condition")

    #15) open gmail
    if there_exists(["open my mail","gmail","check my mail"]):
        search_term= voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your mail")
    
    # screenshot
        if there_exists(["capture","screenshot","my screen"]):
            myScreenshot= pyautogui.screenshot() #.........error ho 
            myScreenshot.save('')
    
    #16) search wikipedia for definition

    if there_exists(["definition of"]):
        definition= record_audio("what do you need the definition of")
        url=urllib.request.urlopen("https://en.wikipedia.org/wiki/"+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definition=[]
        for paragraph in soup.find_all('p'):
            definition.append(str(paragraph.txt))
        if definition:
            if definition[0]: #if condi is false
                engine_speak('here what I found for'+ definition[1])
                #else:
                #engine_speak('heree what i found'+definition[2])
            else:
                engine_speak('i could not find the definition of'+ definition +'server down:have a websearch')

    #game ----stone, paper .. .

    if there_exists(["game"]):
        voice_data= record_audio("choose among rock, paper,scissor")
        moves=["rock","paper","scissor"]
        cmove= random.choice(moves)
        pmove= voice_data
        engine_speak("the computer choose"+cmove)

        if pmove==cmove:
            engine_speak("the match draw")
        elif pmove=="rock" and cmove=="paper":
            engine_speak("Player wins")
        
        elif pmove=="rock" and cmove=="scissor":
            engine_speak("player wins")

        elif pmove=="scissor" and cmove=="rock":
            engine_speak("computer wins")

        elif pmove=="paper" and cmove=="rock":
            engine_speak("computer wins")
        
        elif pmove=="paper"and cmove=="scissor":
            engine_speak("computer wins")

        elif pmove=="scissor"and cmove=="paper":
            engine_speak("player wins")
        
        #toss a coin 
        if there_exists(["toss","flip","coins"]):
            moves=["head","tails"]
            cmove=random.choice(moves)
            engine_speak("the coputer choose"+cmove)

        #calculator
        if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
            opr= voice_data.split()[1]

            if opr == 'pluse':
                engine_speak(int(voice_data.split()[0])+ int(voice_data.split()[2]))
            
            elif opr == "minus":
                engine_speak(int(voice_data.split()[0])- int(voice_data.split[2]))
            
            elif opr == "multiply":
                engine_speak(int(voice_data.split()[0])* int(voice_data.split()[2]))

            elif opr=="divide":
                engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))

            elif opr=="power":
                engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))

            else:
                engine_speak("wrong operation")

        #for exist
        if there_exists(["exist","goodbye","quit","take some rest bro"]):
            engine_speak("we could continue more sir, well goodbye")
            exit()

        
time.sleep(1)
asis.obj= asis()
person_obj= person()
asis_obj.name= 'Nick'
engine = pyttsx3.init() #.... error may come

while(1):
    voice_data= record_audio("recording") #get the voice input
    print("done")
    print("Q:", voice_data)

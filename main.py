import speech_recognition as sr
import webbrowser 
import pyttsx3
import pygame
import os
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
#import pygame
#import os
 #####jode na chala tahola sob extension aber dowload korta hoba 
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "87817dd460c747d9af6effaceaee61a2"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save('text.mp3')
    
    
    #Initialize Pygame mixer
    pygame.mixer.init()
    
    #load the MP3 file
    pygame.mixer.music.load('text.mp3')
    
    #play the MP3 file
    pygame.mixer.music.play()
    
    #keep the program running untill the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("text.mp3")
    
    #################################################################################################
    
    
# def cal_day():
#     day = datetime.datetime.today().weekday() + 1
#     day_dict={
#         1:"Monday",
#         2:"Tuesday",
#         3:"Wednesday",
#         4:"Thursday",
#         5:"Friday",
#         6:"Saturday",
#         7:"Sunday"
#     }
#     if day in day_dict.keys():
#         day_of_week = day_dict[day]
#         print(day_of_week)
#     return day_of_week


# def schedule():
#     day = cal_day().lower()
#     speak("Boss today's schedule is ")
#     week={
#     "monday": "Boss, from 9:00 to 9:50 you have Algorithms class, from 10:00 to 11:50 you have System Design class, from 12:00 to 2:00 you have a break, and today you have Programming Lab from 2:00 onwards.",
#     "tuesday": "Boss, from 9:00 to 9:50 you have Web Development class, from 10:00 to 10:50 you have a break, from 11:00 to 12:50 you have Database Systems class, from 1:00 to 2:00 you have a break, and today you have Open Source Projects lab from 2:00 onwards.",
#     "wednesday": "Boss, today you have a full day of classes. From 9:00 to 10:50 you have Machine Learning class, from 11:00 to 11:50 you have Operating Systems class, from 12:00 to 12:50 you have Ethics in Technology class, from 1:00 to 2:00 you have a break, and today you have Software Engineering workshop from 2:00 onwards.",
#     "thursday": "Boss, today you have a full day of classes. From 9:00 to 10:50 you have Computer Networks class, from 11:00 to 12:50 you have Cloud Computing class, from 1:00 to 2:00 you have a break, and today you have Cybersecurity lab from 2:00 onwards.",
#     "friday": "Boss, today you have a full day of classes. From 9:00 to 9:50 you have Artificial Intelligence class, from 10:00 to 10:50 you have Advanced Programming class, from 11:00 to 12:50 you have UI/UX Design class, from 1:00 to 2:00 you have a break, and today you have Capstone Project work from 2:00 onwards.",
#     "saturday": "Boss, today you have a more relaxed day. From 9:00 to 11:50 you have team meetings for your Capstone Project, from 12:00 to 12:50 you have Innovation and Entrepreneurship class, from 1:00 to 2:00 you have a break, and today you have extra time to work on personal development and coding practice from 2:00 onwards.",
#     "sunday": "Boss, today is a holiday, but keep an eye on upcoming deadlines and use this time to catch up on any reading or project work."
#     }
#     if day in week.keys():
#         speak(week[day])

# # def wishMe():
# #     hour = int(datetime.datetime.now().hour)
# #     t = time.strftime("%I:%M:%p")
# #     day = cal_day()

# #     if(hour>=0) and (hour<=12) and ('AM' in t):
# #         speak(f"Good morning sir, it's {day} and the time is {t}")
# #     elif(hour>=12)  and (hour<=16) and ('PM' in t):
# #         speak(f"Good afternoon sir, it's {day} and the time is {t}")
# #     else:
# #         speak(f"Good evening sir, it's {day} and the time is {t}")


# def openApp(command):
#     if "calculator" in command:
#         speak("opening calculator")
#         os.startfile('search-ms:displayname=Search%20Results%20in%20This%20PC&crumb=location:%3A%3A{20D04FE0-3AEA-1069-A2D8-08002B30309D}\Calculator')
#     elif "notepad" in command:
#         speak("opening notepad")
#         os.startfile('C:\\Windows\\System32\\notepad.exe')
#     elif "paint" in command:
#         speak("opening paint")
#         os.startfile('C:\\Windows\\System32\\mspaint.exe')
        
        


###################################################################################################
    
    
def aiprocess(command):
    client = OpenAI(
    api_key="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",
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud, Give short responses please"},
    {"role": "user", "content": command}
  ]
)

    return (completion.choices[0].message.content)

def processCommand(c):
    if  "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif  "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f" https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON request
            data = r.Json()                       #news cheak korta hoba 
            
            #Extract the articales
            articles = data.get('articles' , [])
            
            #print the headlines
            for articles in articles:
                speak(articles.get['title'])
                
                
                
                
    else:
        # Let openAi handle the requeste 
        output = aiprocess(c)
        speak(output)
        pass
        


if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        #listen for the wake word "Jarvis"
        #obtain audio from microphone
        r = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("Jarvis is listening...")
        #     audio = r.listen(source , timeout=2 , phrase_time_limit=1)
        
        
        print("recognizing.........")
        try:
            with sr.Microphone() as source:
                print("Jarvis is listening...")
                audio = r.listen(source , timeout=3 , phrase_time_limit=4)  #change timeout and phase time 
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("ya")
                 #listen for command 
                with sr.Microphone() as source:
                    print("Jarvis active ...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    
                    processCommand(command)
            # print(command)
        # except sr.UnKnownValueError:
        #     print("sphinx could not understand audio")
        except Exception as e:
            print("Error ; {0}".format(e))
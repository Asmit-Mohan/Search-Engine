import speech_recognition as sr
import weather_forecast as wf
from ecapture import ecapture as ec
from gnewsclient import gnewsclient
import requests
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
import os
import calendar
import smtplib

listener = sr.Recognizer()
listener.energy_threshold = 500
listener.pause_threshold = 1
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("I am jarvis sir Please tell me what can i do for you")


def take_command():
    try:
        with sr.Microphone(device_index=2) as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                # print(command)
    except:
        pass
    return command


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('asmitmurari@gmail.com', '9771447147')
    server.sendmail('asmitmurari@gmail.com', to, content)
    server.close()


def run_alexa():
    command = take_command()
    # print(command)
    if 'play from youtube' in command:
        song = command.replace('play', '')
        talk('ok sir playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Sir, Current time is' + time)
    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you, Sir")
    elif "who are you" in command:
        talk("I am your virtual assistant created by Asmit")
    elif "camera" in command or "take a photo" in command:
        ec.capture(0, "Jarvis Camera ", "img.jpg")
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        talk(info)
    elif 'what is' in command:
        query = command.replace('who is', '')
        data = wikipedia.summary(query, 2)
        talk(data)
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        talk('Opening google sir')
        webbrowser.open('www.google.com')
    elif 'shutdown' in command:
        talk('Turning off your laptop sir')
        os.system("shutdown /s /t 1")
    elif 'weather report' in command:
        # datetime.today().strftime('%Y-%m-%d')
        talk('Ok Sir Giving your weather Report')
        print(wf.forecast(place="patna", time="10:30:00", date="2020-12-21", forecast="daily"))
    elif 'bored' in command:
        talk('Sir, I think you should take rest or watch any movie')
    elif 'love' in command:
        talk('Sorry, Sir love is not in my dictionary you should contact alexa')
    elif 'news' in command:
        client = gnewsclient.NewsClient(language='english', location='india', topic='Business', max_results=3)
        print(client.get_news())
    elif 'open gmail' in command:
        talk('Opening gmail sir')
        webbrowser.open('www.gmail.com')
    elif 'open facebook' in command:
        talk('Opening facebook sir')
        webbrowser.open('www.facebook.com')
    elif 'cricket' in command:
        talk('Opening cricbuzz  Sir')
        webbrowser.open('www.cricbuzz.com')
    elif 'location' in command:
        talk('Giving your location Sir')
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        region = data['region']
        country = data['country']
        talk('Sir you are in city' + city)
        talk('State' + region)
        talk('and country is' + country)
    elif 'notepad' in command:
        talk('opening notepad Sir')
        subprocess.call("notepad.exe")
    elif "restart" in command:
        subprocess.call(["shutdown", "/r"])
    elif 'calculator' in command:
        talk('opening calculator Sir')
        subprocess.call("calc.exe")
    elif 'calendar' in command:
        talk('Showing Current Month Calender Sir')
        print(calendar.month(2020, 12))
    elif 'codeblocks' in command:
        talk('Opening codeblocks Sir')
        subprocess.call("C://Program Files (x86)//CodeBlocks//codeblocks.exe")
    elif 'open music from my pc' in command:
        music_dir = 'G:\\ASMIT\\bhakti songs\\RADHE KRISHNA'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'email to asmit' in command:
        try:
            talk("What should I say?")
            content = take_command()
            to = "mohanasmit@gmail.com"
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry my friend, I am not able to send this email")
    else:
        talk('Sir, I did not get it Kindly tell again.')


if __name__ == "__main__":
    wishMe()
    while True:
        run_alexa()

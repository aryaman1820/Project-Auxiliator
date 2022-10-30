import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import random
import webbrowser
import smtplib
import json
import re
import time
import winwifi
import requests
import pyjokes
from word2number import w2n
import pywhatkit as kit
from functools import lru_cache


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 120)
di={"aman":"amanshukla5614@gmail.com","user":"khalidabdullah512@gmail.com"}
song = {}
contacts = {"Aryaman": "+917033592833",
            "harry": "+917491843847"
            }

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def ffile(file):
    for i in range(0, len(file)):
        file[i] = file[i].replace("\n", "")
        file[i] = file[i].replace("\\", "\\")
        file[i] = file[i].replace("\\", "\\")


f = open("media.txt", "r")
file = f.readlines()
f.close()
if (len(file) == 0):
    s = open("media.txt", "a")
    print("hello")
    a = input("enter the music location")
    s.write(f"{a}\n")
    a = input("enter the pictures location")
    s.write(f"{a}\n")
    a = input("enter the document location")
    s.write(f"{a}\n")
    a = input("enter the video location")
    s.write(f"{a}\n")
    a = input("enter the wifi name")
    s.write(f"{a}\n")
    s.close()
    f = open("media.txt", "r")
    file = f.readlines()
    f.close()
    ffile(file)
else:
    ffile(file)
#print(file)
winwifi.WinWiFi.connect(f"{file[4]}")

f1 = open("location.txt", "r")
file1 = f1.readlines()
f1.close()
if (len(file1) == 0):
    t = open("location.txt", "a")
    b = input("enter Vs Code location: ")
    t.write(f"{b}\n")
    b = input("enter the Pycharm location: ")
    t.write(f"{b}\n")
    b = input("enter the Webex location: ")
    t.write(f"{b}\n")
    b = input("enter the chrome location: ")
    t.write(f"{b}\n")
    b = input("enter the skype location: ")
    t.write(f"{b}\n")
    b = input("enter the zoom location: ")
    t.write(f"{b}\n")
    b = input("enter the paint location: ")
    t.write(f"{b}\n")
    t.close()
    f1 = open("location.txt", "r")
    file1 = f1.readlines()
    f1.close()
    ffile(file1)
else:
    ffile(file1)
#print(file1)


doc = {}




def setdocument():
    mudir = file[2]
    u = os.listdir(mudir)
    i = 0
    for items in u:
        v = items.split(".")[0].lower()
        doc.update({v: i})
        i += 1
    print(doc)
    return doc


setdocument()


def setsongs():
    mudir = file[0]
    songs = os.listdir(mudir)
    i = 0
    for items in songs:
        v = items.split(".")[0].lower()
        song.update({v: i})
        i += 1
    print(song)
    return song


op = {}
video = {}


def video_set():
    mudir = file[3]
    picu = os.listdir(mudir)
    i = 0
    for items in picu:
        v = items.split(".")[0].lower()
        video.update({v: i})
        i += 1
    print(video)
    return video


video_set()


def setpicture():
    mudir = file[1]
    picture = os.listdir(mudir)
    i = 0
    for items in picture:
        v = items.split(".")[0].lower()
        op.update({v: i})
        i += 1
    print(op)
    return song


setpicture()


def wishme():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning sir..")
    elif hour > 12 and hour < 16:
        speak("Good Afternoon sir...")
    elif hour >= 16 and hour <= 24:
        speak("Good Evening sir..")
    speak(f" i am alex....how may i help you")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"u said {query}")
    except Exception as e:
        print("Say it again")
        return "none"
    return query


lru_cache(maxsize=10)


def playsongs():
    try:
        mudir = file[0]
        songs = os.listdir(mudir)
        speak("what would you like to hear sir...")
        song_name = command().lower()
        if "rehane do" in song_name or "nothing" in song_name:
            return
        elif "koi bhi" in song_name or "any one" in query:
            v = len(songs)
            i = random.randint(0, v - 1)
        elif song_name == "none":
            speak("which song sir..")
        else:
            i = song[song_name]
        speak("wait sir")
        os.startfile(os.path.join(mudir, songs[i]))
    except Exception as e:
        speak("this song is not exist please search a valid song")


def document():
    try:
        mud = file[2]
        l = os.listdir(mud)
        speak("which document sir..")
        dir = command().lower()
        if "rahane do" in dir or "rehane do" in dir:
            return
        elif "koi bhi" in dir or "any file":
            v = len(l)
            i = random.randint(0, v - 1)
        elif dir == "none":
            speak("which document sir..")
        else:
            i = doc[dir]
        speak("wait sir")
        os.startfile(os.path.join(mud, l[i]))
    except Exception as e:
        speak("this document is not exist please search a valid song")


def video():
    try:
        mud = file[3]
        l = os.listdir(mud)
        speak("which video sir..")
        dir = command().lower()
        if "nothing" in dir or "rehane do" in dir:
            return
        elif "koi bhi" in dir:
            v = len(l)
            i = random.randint(0, v - 1)
        elif dir == "none":
            speak("which video sir..")
        else:
            i = doc[dir]
        speak("wait sir")
        os.startfile(os.path.join(mud, l[i]))
    except Exception as e:
        speak("this video is not exist please search a valid song")


def picture_set():
    try:
        mudiru = file[1]
        pic = os.listdir(mudiru)
        speak("which picture sir..")
        pic_name = command().lower()
        if "nothing" in pic_name or "rehane do" in pic_name:
            return
        elif "koi bhi" in pic_name:
            v = len(pic)
            i = random.randint(0, v - 1)
        elif pic_name == "none":
            speak("which picture sir..")
        else:
            i = op[pic_name]
        speak("wait sir")
        os.startfile(os.path.join(mudiru, pic[i]))
    except Exception as e:
        speak("this picture is not exist please search a valid song")


def sendemail(content, to):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    fr = "alextheauxiliator@gmail.com"
    server.login(fr, "alexpass")
    server.sendmail(fr, to, content)
    server.close()


def confirm():
    ch = "y"
    i = 1
    while ch == "y" and i <= 5:
        speak("sir please enter password")
        pas = input("enter your password\n")
        with open("password.text") as f:
            a = f.read()
            if a == pas:
                break
            else:
                if i == 5:
                    exit()
                else:
                    i += 1


def shurukartehain():
    query = command().lower()
    while not (
            "start all task" in query or "lets start" in query or "Ready" in query):
        query = command().lower()
    speak("   all systems are online, initiating all tasks. Let's do something stormy today ")


def daily():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)
    if hour == 16 and min == 30:
        speak("sorry for disturbing you sir..but this is your coaching time")
    if hour == 20 and min == 0:
        speak("sorry for disturbing you sir..but this is your english speaking course time")
    if hour == 22 and min == 30:
        speak("sorry for disturbing you sir..but this is your aptitude practice time")
    if hour == 12 and min == 30:
        speak("sorry for disturbing you sir..but this is your django study time")
    return


if __name__ == '__main__':
    setsongs()
    confirm()
    wishme()
    shurukartehain()

    ch = "y"
    while ch == "y":
        daily()
        query = command().lower()

        if "wikipedia" in query and "alex" in query:
            try:
                speak("searching sir...")
                query = query.replace("search ", "")
                query = query.replace("alex ", "")
                query = query.replace("about ", "")
                query = query.replace(" in wikipedia", "")
                result = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia...")
                speak(result)
            except Exception as e:
                speak(f"soryy sir there is no information about {query} in wikipedia")
        elif "document" in query and "alex"in query:
            document()

        elif "google" in query and"alex"in query:
            speak("wait sir")
            speak("what should i search sir")
            search = command()
            while search == "none":
                speak("what should i search")
                search = command()
            kit.search(search)

        elif "youtube" in query and"alex"in query:
            speak("what should i search")
            search = command()
            while search == "none":
                speak("what should i search")
                search = command()
            search.replace("search", "")
            speak("wait sir.")
            kit.playonyt(search)

        elif "open hackerrank" in query and"alex"in query:
            webbrowser.open("hackerrank.com")

        elif "open gallery" in query and"alex"in query:
            picture_set()

        elif "play music" in query or "play songs" in query or "play song" in query or "play a song" in query or "please a song" in query or "please song" in query and"alex"in query:
            playsongs()


        elif "time" in query and"alex"in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)

        #local directories opening and closing
        elif " open visual code" in query and"alex"in query:
            speak("Opening visual code")
            os.startfile(file1[0])

        elif "close visual code" in query and"alex"in query:
            speak("closing visual code")
            os.system("taskkill /f /im Code.exe")

        elif " open pycharm" in query and "alex" in query:
            speak("opening pycharm")
            os.startfile(file1[1])

        elif "close pycharm" in query and"alex"in query:
            speak("Closing pycharm")
            os.system("taskkill /f /im pycharm64.exe")

        elif "open command prompt" in query and "alex" in query:
            speak("Opening command prompt")
            os.startfile("C:\\Windows\\System32\\cmd.exe")

        elif "close command prompt" in query and "alex" in query:
            speak("Closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif "open webex" in query and "alex" in query:
            speak("Opening")
            os.startfile(file1[2])

        elif "close webex" in query and"alex"in query:
            speak("Closing")
            os.system("taskkill /f /im CiscoCollabHost.exe")

        elif "open word" in query and "alex" in query:
            speak("Opening")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

        elif "close word" in query and "alex" in query:
            speak("Closing")
            os.system("taskkill /f /im WINWORD.EXE")

        elif "open file explorer" in query and "alex" in query:
            speak("Opening")
            os.startfile("C:\\Windows\\explorer.exe")

        elif "close file explorer" in query and"alex"in query:
            speak("Closing")
            os.system("taskkill /f /im explorer.exe")

        elif "open calendar" in query and "alex" in query:
            speak("Opening")
            os.startfile("C:\\Program Files\\WindowsApps\\microsoft.windowscommunicationsapps_16005.14326.20858.0_x64__8wekyb3d8bbwe\\HxCalendarAppImm.exe")

        elif "close calendar" in query and"alex"in query:
            speak("Closing")
            os.system("taskkill /f /im HxCalendarAppImm.exe")

        elif "open excel" in query and "alex" in query:
            speak("Opening")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe")

        elif "close excel" in query and"alex"in query:
            speak("Closing")
            os.system("taskkill /f /im EXCEL.exe")

        elif "open screen keyboard" in query and "alex" in query:
            speak("Opening")
            os.startfile("C:\\Windows\\System32\\osk.exe")

        elif "close screen keyboard" in query and"alex"in query:
            speak("Closing")
            os.system("taskkill /f /im osk.exe")

        elif "open powerpoint" in query and "alex" in query:
            speak("Opening")
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

        elif "close powerpoint" in query and "alex" in query:
            speak("Closing")
            os.system("taskkill /f /im POWERPNT.EXE")

        elif "open chrome" in query and "alex" in query:
            speak("Opening")
            os.startfile(file1[3])

        elif "close chrome" in query and "alex" in query:
            speak("Closing")
            os.system("taskkill /f /im chrome.exe")


        elif "open skype" in query and "alex" in query:
            speak("Opening")
            os.startfile(file1[4])

        elif "close skype" in query and"alex"in query:
            speak("Closing")
            os.system("taskkill /f /im Skype.exe")

        elif "open zoom" in query and "alex" in query:
            speak("Opening")
            os.startfile(file1[5])

        elif "close zoom" in query and"alex"in query:
            speak("Closing")
            os.system("taskkill /f /im zoom.exe")

        elif "open music" in query:
            speak("executing")
            os.startfile("D:\\Music")

        elif "open document" in query:
            speak("executing")
            os.startfile("D:\\Documents")

        elif "open download" in query:
            speak("executing")
            os.startfile("C:\\Users\\khali\\Downloads")

        elif "open videos" in query:
            speak("executing")
            os.startfile("D:\\Videos")

        elif "open media" in query:
            speak("executing")
            os.startfile("C:\\Program Files\\Windows Media Player\\wmplayer.exe")




        elif "send mail" in query or "send email" in query:

            try:

                speak("are u confirm")

                confirm = command().lower()

                if confirm == "none":
                    confirm = command().lower()

                if "rahane do" in confirm or "rehane do" in confirm or "no" in confirm or "nahi" in confirm:
                    pass

                speak("what should i say")

                content = command()

                speak("are u confirm")

                confirm = command().lower()

                print(confirm)

                if confirm == "none":
                    confirm = command().lower()

                if "rahane do" in confirm or "rehane do" in confirm or "no" in confirm:

                    pass


                elif content == None:

                    speak("say it again")

                    content = command()

                elif content != "" and "rahane do" not in confirm:

                    speak("To whom sir ")

                    item = command().lower()

                    print(item)

                    s = item.split(" ")

                    print(s)

                    for i in s:

                        for item in di.keys():

                            if item == i:
                                to = i

                    print(to)

                    too = di[to]

                    print(too)

                    sendemail(content, too)

                    speak("email is send")

            except Exception as e:

                speak("sry sir i m not able to send your email")
        elif "change song" in query or "next song" in query or "change music" in query or "next music" in query and "alex" in query:
            playsongs()

        elif "who invented you" in query and"alex"in query:
            speak("Aryaman and Abdullah invented me.")

        elif "tell me something about yourself" in query and "alex" in query:
            speak("I am Alex an Artificial intelligence programme, developed by Aryaman and Abdullah as a their "
                  "Bachelors of technology project under Auxiliator:One's personal Artificial Assistant")
            speak("I am developed using python programming language and can perform multiple tasks, such as playing "
                  "music for you, opening your files etc.")
            speak("my task is to perform functions as per the user's voice commands. I am here to assist you.")
            print("1. Today's news alex\n")
            print("2. Tell me the time alex\n")
            print("3. Google search alex\n")
            speak("Here is a list of some functions i can perform for you. Give it a try !!!")

        elif "aj ki news" in query or "today's news" in query or "news sunao" in query and"alex"in query:
            url = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=657de6952ac3443e9d6ba9b27a126d13").text
            content = json.loads(url)
            con = content['articles']
            speak("Todays news is..")
            c = 1
            ran = ["Moving on to the next news", "Next news", "next is", "continuing on to the next news", "listen carefully"]
            for items in con:
                print(items['title'])
                speak(items['title'])
                speak(random.choice(ran))
                if c == 10:
                    break
                c += 1

        elif "open paint" in query and "alex" in query:
            speak("opening paint")
            os.startfile(file1[6])

        elif "close paint" in query and "alex" in query:
            speak("closing paint")
            os.system("taskkill /f /im CiscoCollabHost.exe")

        elif "say" in query and "alex" in query:
            query = query.replace("say", "")
            query = query.replace("alex", "")
            speak(query)
            print(query)

        elif "joke" in query and "alex" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "how are you" in query and "alex" in query:
            hru = ["Fine, and you?", "Good, how about yourself?", "Doing fine, and you?", "Good, how about you?"]
            speak(random.choice(hru))

        elif "whatsapp" in query and "alex" in query:
            try:
                speak("what is the msg sir")
                msg = command()
                b = 0
                while msg == "none":
                    speak("what is the message sir")
                    msg = command().lower()
                speak("send to whom")
                for items in contacts.keys():
                    print(items)
                whom = command().lower()
                while whom == "none":
                    speak("send to whom")
                    whom = command().lower()
                if whom == "leave it" or whom == "rehana do" or whom == "rahana do":
                    break
                else:
                    s = whom.split(" ")
                    print(s)
                    for i in s:
                        for items in contacts.keys():
                            if items == i:
                                reciever = contacts[items]
                                print(reciever)
                    hour = int(datetime.datetime.now().hour)
                    min = int(datetime.datetime.now().minute) + 2
                    kit.sendwhatmsg(reciever, msg, hour, min, 55)
            except Exception as e:
                    speak("this contact is not exist")

        elif "shut down" in query and"alex"in query:
            time = int(datetime.datetime.now().hour)
            speak("Are you confirm sir")
            msg = command().lower()
            while msg == "none":
                speak(" confirm your command ")
                msg = command().lower()
            if "yes" in msg:
                kit.shutdown(time)
            else:
                pass

        elif "enough" in query and "alex" in query:
            speak("sorry  for inconvenience sir.")

        elif "hey alex" in query:
            speak("hello sir..")

        elif "what are you doing" in query and "alex" in query:
            speak("waiting for your command sir..")

        elif "see you later" in query and "alex" in query:
            speak("Bye sir...take care and have a good day")
            ch = "n"

        elif "Sleep" in query or "let's have some rest" in query:
            speak("by what minutes shall i be back sir ")
            Qry = command().lower()
            Qry = Qry.replace("minutes", "")
            Qry = Qry.replace("minute", "")
            print(Qry)
            local_time = int(Qry)
            local_time = local_time * 60
            time.sleep(local_time)
            speak("Hey there! i m back at your service ")

        elif "stop" in query:
            speak("terminating the system now. we'll meet again soon!!!")
            print("terminating the system now. we'll meet again soon!!!")
            exit()


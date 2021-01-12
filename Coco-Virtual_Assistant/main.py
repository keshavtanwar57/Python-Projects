import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
from requests import get
import pyautogui,time




listener = sr.Recognizer()
engine = pyttsx3. init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('Hi. I am Coco, your personal assistant')
engine.say('What can I do for you?')
engine.runAndWait()


def spam():
    time.sleep(10)
    f = open("abc.txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'coco' in command:
                command = command.replace('Coco','')
    except:
        pass

    return command


def news():
    news_links = ['http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bbbd50febd70401080058f343bb3a44a',
                  'http://newsapi.org/v2/everything?q=bitcoin&from=2020-11-11&sortBy=publishedAt&apiKey=bbbd50febd70401080058f343bb3a44a',
                  'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bbbd50febd70401080058f343bb3a44a',
                  'http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=bbbd50febd70401080058f343bb3a44a',
                  'http://newsapi.org/v2/everything?q=apple&from=2020-12-10&to=2020-12-10&sortBy=popularity&apiKey=bbbd50febd70401080058f343bb3a44a',
                  'http://newsapi.org/v2/everything?domains=wsj.com&apiKey=bbbd50febd70401080058f343bb3a44a']

    main_url = random.choice(news_links)
    main_page = get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["First", "Second", "Third", "Four", "Five"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        talk(f"today's {day[i]} news is {head[i]}")
c = 0
def quit_fun(c):
    c = c + 1
    return c
def run_coco():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        song = command.replace('coco', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'who is' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open pycharm' in command:
        talk("opening PyCharm")
        pycharm = "D:\\Development\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"

    elif 'what is the time' in command:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        print(strTime)
        talk(f"The time is {strTime}")

    elif 'send a message' in command:
        x = datetime.datetime.now()
        talk("what is your message")
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            mssg = listener.recognize_google(voice)
        talk("opening whatsapp")
        pywhatkit.sendwhatmsg("+917248570886", mssg, x.hour,x.minute+2)

    elif 'news' in command:
        talk("Please wait fetching the latest news")
        news()
    elif 'i love you' in command:
        talk('hmm... well i love you too but as a friend')
    elif 'spam' in command:
        talk("Spaming Affu on whatsapp...")
        x = datetime.datetime.now()
        mssg = "My friend you are gone ha ha ha...."
        pywhatkit.sendwhatmsg("+919951826557", mssg, x.hour, x.minute + 1)
        spam()

    elif 'who created you' or 'when were you borned' in command:
        talk('I was created by Keshav Tanwar on 21 december of 2020 ')

    elif 'quit' in command:
        talk('Bye Sir, have a good day')
        c = quit_fun()


    else:
        talk('Could you please repeat')

while True:
    run_coco()
    if c > 0:
        break
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random as ran

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<9:
        speak('Good Morning!')

    elif hour>=9 and hour<17:
        speak('Good Afternoon!')
    elif hour >= 17 and hour < 19:
        speak('Good Evening!')
    else:
        speak('Good Night!')
    speak('I am shortcut assistant sir')

def weki(value):
    result = ""
    query = value
    speak("Searching Wikipedia")
    results = wikipedia.summary(query, sentences=5)
    speak("According to Wikipedia")
    result = results
    speak(results)

def YT():
    speak("Opening Youtube")
    webbrowser.get('chrome').open_new_tab("youtube.com")

def fb():
    speak("Opening facebook")
    webbrowser.get('chrome').open_new_tab("facebook.com")

def Gaana_web():
    speak("Opening gaana website")
    webbrowser.get('chrome').open_new_tab("gaana.com")

def google():
    speak("Opening google")
    webbrowser.get('chrome').open_new_tab("google.com")

def github_web():
    speak("Opening github.com")
    webbrowser.get('chrome').open_new_tab("github.com")

def stackOF_web():
    speak("Opening stackoverflow.com")
    webbrowser.get('chrome').open_new_tab("stackoverflow.com")

def zoom_web():
    speak("Opening zoom.com")
    print("Opening zoom.com")
    webbrowser.get('chrome').open_new_tab("zoom.com")

def play_music():
    song_no = ran.randrange(0,29)
    speak("Play music")
    music_dir = "D:\\MUSICON\\trending audio"
    songs = os.listdir(music_dir)
    for x in range(2, 8):
        songs.pop(x)
    os.startfile(os.path.join(music_dir, songs[song_no]))
    speak(songs[song_no])

def cur_time():
    speak("Current time and day")
    strTime = datetime.datetime.now().strftime("%H:%M:%S:%p")
    speak(f"Sir, the time is {strTime}")

def musicOn_web():
    speak("Opening your MusicOn website")
    musicon_web = "D:\\Musicon Website\\html\\mainpage.html"
    os.startfile(musicon_web)

def word():
    speak("Opening MS WORD")
    word = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.exe"
    os.startfile(word)

def ppt():
    speak("Opening MS POWERPOINT")
    ppt = "C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.exe"
    os.startfile(ppt)

def excel():
    speak("Opening MS EXCEL")
    excel = "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.exe"
    os.startfile(excel)

def publisher():
    speak("Opening MS Publisher")
    pub = "C:\\Program Files\\Microsoft Office\\Office16\\MSPUB.exe"
    os.startfile(pub)

def onenote():
    speak("Opening MS OneNote")
    onote = "C:\\Program Files\\Microsoft Office\\Office16\\ONENOTE.exe"
    os.startfile(onote)

def access():
    speak("Opening MS Access")
    acc = "C:\\Program Files\\Microsoft Office\\Office16\\MSACCESS.exe"
    os.startfile(acc)

def WA_app():
    speak("Opening whatsapp application")
    whatsapp = "C:\\Users\\DELL\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
    os.startfile(whatsapp)

def Zoom_app():
    speak("Opening zoom application")
    zoom = "C:\\Users\\DELL\\AppData\\Roaming\\Zoom\\bin_00\\Zoom.exe"
    os.startfile(zoom)

def team_app():
    speak("Opening TeamViewer application")
    zoom = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
    os.startfile(zoom)

def filmora_app():
    speak("Opening Wondershare Filmora application")
    zoom = "C:\\Program Files\\Wondershare\\Filmora\\Filmora.exe"
    os.startfile(zoom)

def skype_app():
    speak("Opening Skype application")
    zoom = "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"
    os.startfile(zoom)

def dev_app():
    speak("Opening dev c++")
    dev_c = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
    os.startfile(dev_c)

from main_module.common.ultils.commonUltils import *
import subprocess
import tkinter as tk
from main_module.conf.config_loader import *
from googlesearch import search
from main_module.common.static_var.static_value import *
from main_module.common.static_var.constants import *
from gtts import gTTS
import playsound
import datetime
from threading import Thread
import threading
import time

def printTerminal(self, mode, message):
    if mode == CMD.READ_YES:
        printMessage(self, message)
    if mode == CMD.READ_LISTEN_YES:
        printMessage(self, message)
        speak(message)
        
def printMessage(self, message):
    message=  '\n' + message + '\n'
    self.txt_terminal.insert(tk.END, message)
    self.txt_terminal.see(tk.END)
    self.txt_input.focus()
    self.update()
            
def exc_cmd(cmd):
    if not cmd:
       return
    print("executing :"+cmd)
    cmd_res = subprocess.getoutput(cmd) + "\n"
    return cmd_res


def getGgleSearchInPage(searchStr, inPage):
    print("gg searching :"+searchStr)
    search_results = search(searchStr, start = CSearch.DEFAULT_START_RESULT, stop = CSearch.DEFAULT_NUM_RESULT, pause=2)
    url = ''
    for res in search_results:
        print("checking url:" +res)
        if isLinkValid(res, [inPage]):
            url = res
            print("opening url:" +res)
            break
    return url

def getAllGgleSearchInPageArr(searchStr, inPageArr):
    print("gg searching :"+searchStr)
    search_results = search(searchStr, start = CSearch.DEFAULT_START_RESULT, stop = CSearch.DEFAULT_NUM_RESULT, pause=2)
    urlArr = []
    for res in search_results:
        print("checked url:" +res)
        if isLinkValid(res, inPageArr):
            urlArr.append(res)
            print("add url:" +res)
            break
    return urlArr

def getArrLinkFromSearch(searchStr):
    print("gg searching :"+searchStr)
    search_results = search(searchStr, start = CSearch.DEFAULT_START_RESULT, stop = CSearch.DEFAULT_NUM_RESULT, pause=2)
    urlArr = []
    for res in search_results:
        urlArr.append(res)
    return urlArr
    
def isLinkValid(url, arrPage):
    for page in arrPage:
        if page in url:
            return True
    return False

def getArrElementCmd(arr, indexArr):
    arrRes = []
    for cmd in arr:
        arrCmd = textToArray(cmd, CKey.CMD_SPLIT_LV_1) 
        arrRes.append(arrCmd[indexArr])
    arrRes = list(dict.fromkeys(arrRes))
    print('Arr Element of index: '+ str(indexArr))
    print(arrRes)
    return arrRes

def isSameTypeCmd(arrCmd):
    arrType = getArrElementCmd(arrCmd, 1)
    return len(arrType) <= 1

    # voice
def speak(text):
    CSysv = Loader.loadConfig()['CSys']
    CSys.USE_READ = Loader.getPropByKey(CSysv, 'USE_READ')
    
    if CSys.USE_READ == True:
        currThread =  threading.enumerate()
        while len(currThread) > 1:
            time.sleep(1)
            currThread =  threading.enumerate()
        t1 = threading.Thread(target=speakProcess, args=(text,))
        t1.setName('speaker')
        t1.start()
        
def speakProcess(text):
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    output = gTTS(text,lang="vi", slow=False)
    output.save(filename)
    playsound.playsound(filename, True)
    os.remove(filename)
    
#####################################
import speech_recognition as sr
import pyaudio
def listen():
    CSysv = Loader.loadConfig()['CSys']
    CSys.USE_RECOGN_VOICE = Loader.getPropByKey(CSysv, 'USE_RECOGN_VOICE')
    if CSys.USE_RECOGN_VOICE == True:
        t2 = threading.Thread(target=listenProcess)
        t2.setName('listener')
        t2.start()
        
def listenProcess():
    init_rec = sr.Recognizer()
    micro = sr.Microphone()
    print("Listener is listening...")
    with micro as source:
        print("ewqw")
        audio_data = init_rec.record(source, duration=5)
        print("Recognizing your text.............")
        text = init_rec.recognize_google(audio_data)
        print(text)
        
            
            
   
from bs4 import BeautifulSoup
import requests
import subprocess
import tkinter as tk
from conf.config import *
from modules.google_search.main import *
from main_module.ultils.fileUltils import *
botRes = Message.getBotResMessage()

def exc_cmd(cmd):
    if not cmd:
       return
    print("executing :"+cmd)
    cmd_res = subprocess.getoutput(cmd) + "\n"
    return cmd_res

def getContentFromLink(url, der):
    f = requests.get(url)
    html = f.text
    if isStrContainArr(VSearch.ARR_ACCESS_DENIED, html):
       print(html)
       return botRes['access-denied']
    soup = BeautifulSoup(html, "html.parser")
    results = soup.select(der)
    print('selector:'+ der)
    print(results)
    if len(results) >0:
        for content in soup.select(der):
            print(content.text)
            return content.text
    return botRes['cmd-not-found']

def printMessage(self, message):
    message=  '\n' + message + '\n'
    self.txt_terminal.insert(tk.END, message)
    self.txt_terminal.see(tk.END)
    
def isStrContainArr(arr, str):
    for item in arr:
         if item.strip() in str.strip():
             return True
    return False

def isArrContainStr(arr, str):
    for item in arr:
         if str.strip() in item.strip():
             return True
    return False

def isEqualArr(arr, str):
    for item in arr:
         if item.strip() == str.strip():
             return True
    return False
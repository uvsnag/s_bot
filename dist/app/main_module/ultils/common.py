from bs4 import BeautifulSoup
import requests
import subprocess
import tkinter as tk
from conf.config import *
from googlesearch import search
# from modules.google_search.main import *
# from main_module.ultils.fileUltils import *

# botRes = Message.getBotResMessage()

def exc_cmd(cmd):
    if not cmd:
       return
    print("executing :"+cmd)
    cmd_res = subprocess.getoutput(cmd) + "\n"
    return cmd_res

def getContentFromLink(botRes, url, der, iSeArr):
    f = requests.get(url)
    html = f.text
    if isStrContainArr(VSearch.ARR_ACCESS_DENIED, html):
       print(html)
       return botRes['access-denied']
    soup = BeautifulSoup(html, "html.parser")
    results = soup.select(der)
    print('selector:'+ der)
    print("len of arr result: "+str(len(results)))
    if len(results) > 0:
        reStr = ''
        for i in iSeArr:
            reStr += results[int(i)].text
        print(reStr)
        return reStr
    return botRes[CommandConstants.CMD_NOT_FOUND]

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
         if isContainTrim(str, item):
             return True
    return False

def isEqualArr(arr, str):
    for item in arr:
         if isEqualTrim(item, str):
             return True
    return False

def textToArray(content, split):
    deterChar = '`'
    content = content.replace(split, deterChar)
    arr = content.split(deterChar)
    return arr

def textToArray(content, split):
    deterChar = '`'
    content = content.replace(split, deterChar)
    arr = content.split(deterChar)
    return arr

def ggleSearch(searchStr, inPage):
    print("gg searching :"+searchStr)
    search_results = search(searchStr, start=CSearch.DEFAULT_START_RESULT, stop = CSearch.DEFAULT_NUM_RESULT, pause=2)
    url = ''
    for res in search_results:
        print("checked url:" +res)
        if isLinkValid(res, [inPage]):
            url = res
            print("opening url:" +res)
            break
    return url
    
def isLinkValid(url, arrPage):
    for page in arrPage:
        if page in url:
            return True
    return False

def isEqualTrim(a, b):
    if a == '' or b == '':
        return False
    return a.strip().upper() == b.strip().upper()

def isContainTrim(a, b):
    if a == '' or b == '':
        return False
    return a.strip().upper() in b.strip().upper()

    
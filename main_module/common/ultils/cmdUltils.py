
from main_module.common.ultils.commonUltils import *
import subprocess
import tkinter as tk
from main_module.conf.config_loader import *
from googlesearch import search
from main_module.common.static_var.static_value import *
from main_module.common.static_var.constants import *

def printTerminal(self,arrCmd, message):
    if arrCmd[1] == CMD.READ_YES:
        printMessage(self, message)
        
def printMessage(self, message):
    message=  '\n' + message + '\n'
    self.txt_terminal.insert(tk.END, message)
    self.txt_terminal.see(tk.END)
    self.txt_input.focus()
            
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
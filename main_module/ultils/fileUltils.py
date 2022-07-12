import configparser
from conf.config import *
import os

# import tkinter as tk
# from main_module.ultils.common import *


def getCurrUrlFolder():
    directory = os.getcwd()
    return directory

rootUrl = getCurrUrlFolder()+"\main_module\message\\" + CSys.LANG + "\\"

class Message:
    def getBotResMessage():
        url = rootUrl + "sys.message"
        return getMessageObject(url, "bot-res")
    
    def getDataMessage():
        url = rootUrl + "data.ini"
        return readFileIntoArr(url)
    
def deterCommand(cmd, arr):
    result=""
    for item in arr:
        if getValueMess(item).strip() == cmd.strip():
            result = getKeyMess(item)
    print('key determined: '+result)
    return result 
            
def getAllCmdWKey(key, arr):
    arrRes = []
    for item in arr:
        if getKeyMess(item).strip() == key.strip():
            arrRes.append(item)
    return arrRes 
            
                
def getMessageObject(url, objName):
    config_obj = configparser.ConfigParser()
    config_obj.read(url)
    obj = config_obj[objName]
    print('object:'+objName+ ' has been loaded!') 
    return obj        
    
def readFileIntoArr(url):
    file = open(url, "r")
    content = file.read()
    arrMess = textToArray(content, CKey.KEY_NEWLINE)
    return arrMess

def textToArray(content, split):
    deterChar = '`'
    content = content.replace(split, deterChar)
    arr = content.split(deterChar)
    return arr

def getKeyMess(cmd):
    indexOfSep = cmd.find(CKey.SEPR_MESS)
    key = cmd[0:indexOfSep]
    return key.strip()

def getValueMess(cmd):
    indexOfSep = cmd.find(CKey.SEPR_MESS)
    lastIndex = len(cmd)
    value = cmd[indexOfSep+1:lastIndex]
    return value.strip()




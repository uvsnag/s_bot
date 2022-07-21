import configparser
from main_module.conf.config_loader import *

from main_module.ultils.commonUltils import *
from main_module.common.static_value import *
import codecs

class Message:
    def getBotResMessage():
        rootUrl = getCurrUrlFolder() + CSys.PATH_BOT_MESSAGE + CSys.APP_LANG + "\\"    
        url = rootUrl + "sys.message"
        return getMessageObject(url, "bot-res")
    
    def getDataMessage():
        arr = getArrAllModule(CSys.PATH_MESSAGE)
        return arr
    
def getArrAllModule(urlFile):
    arr = []
    for item in CSys.PATH_MODULE_ARR:
            url = getCurrUrlFolder() +item + urlFile
            arr = arr + readFileIntoArr(url)
    return arr

def deterCommand(cmd, arr):
    result=""
    for item in arr:
        if isContainTrim(cmd, getValueMess(item)):
            key = getKeyMess(item)
            if not isEqualArr(CSys.ARR_CMD_NOT_CHECK_CASE_IN, key):
                result = key
    print('key determined mode in: '+result)
    return result 

def deterCommandEquals(cmd, arr):
    result=""
    for item in arr:
        if isEqualTrim(cmd, getValueMess(item)):
            result = getKeyMess(item)
    print('key determined mode equal: '+result)
    return result 
            
def getAllCmdWKey(key, arr):
    arrRes = []
    for item in arr:
        if getKeyMess(item).strip() == key.strip():
            arrRes.append(getValueMess(item))
    return arrRes 
            
                
def getMessageObject(url, objName):
    config_obj = configparser.ConfigParser()
    config_obj.read(url, encoding = CSys.APP_ENCODE)
    obj = config_obj[objName]
    # print('object:'+objName+ ' has been loaded!') 
    return obj        
    
def readFileIntoArr(url):
    file = open(url, "r", encoding = CSys.APP_ENCODE)
    content = file.read()
    arrMess = textToArray(content, CKey.KEY_NEWLINE)
    return arrMess


def getKeyMess(cmd):
    indexOfSep = cmd.find(CKey.SEPR_MESS)
    key = cmd[0:indexOfSep]
    return key.strip()

def getValueMess(cmd):
    indexOfSep = cmd.find(CKey.SEPR_MESS)
    lastIndex = len(cmd)
    value = cmd[indexOfSep+1:lastIndex]
    return value.strip()


# write file

def writeFile(urlFile, line, content):
    MODE = 'a' #append
    with open(urlFile, MODE) as the_file:
        the_file.write('\n')
        the_file.write(content)
from conf.config import *
from main_module.ultils.fileUltils import *
from main_module.ultils.common import *

botRes = Message.getBotResMessage()

def process(self, key, cusResq):
    arrCmd =  getAllCmdWKey(key, getArrAllModule(CSys.PATH_CMD))
    if isSameTypeCmd(arrCmd):
        process_internet_same_type(self, arrCmd, cusResq)
    else:
        process_internet_other_type(self, arrCmd, cusResq)
    
    
def process_internet_same_type(self, arrCmd, cusResq):
    cmd_type = textToArray(arrCmd[0], CKey.CMD_SPLIT_LV_1)[0]
    arrUrlCmd = getArrElementCmd(arrCmd, 2)
    if StaticVar.CURRENT_INDEX_ARRLINK >= len(arrUrlCmd):
        printMessage(self, botRes['nothing-more'])
        return
    cmd_link = arrUrlCmd[StaticVar.CURRENT_INDEX_ARRLINK]
    print('Getting: '+cmd_link)
    if cmd_type == CMD.SLINK:
        url = cmd_link
    elif cmd_type == CMD.SEARCH:
        url = getGgleSearchInPage(cusResq + " " + cmd_link, cmd_link)
        StaticVar.CURRENT_SEARCH_STR = cusResq
        
    html = getContentFromLink(botRes, url)
    resStr = getContentForSelector(html, arrCmd)
    printMessage(self, resStr)
    
    
def process_internet_other_type(self, arrCmd, cusResq):
    printMessage(self, 'this function is not dev yet!')
    var_result = ''
    for item in arrCmd:
        arrCmd_Detail = textToArray(item, CKey.CMD_SPLIT_LV_1)
        cmd_type = arrCmd_Detail[0]
        cmd_url = arrCmd_Detail[2]
        html = getContentFromLink(botRes, cmd_url)
        var_result = getContentForSelector(html, arrCmd_Detail)
        ##
    
def cmd_process(self, arrCmd):
    cmd_value = arrCmd[2]
    res = exc_cmd(cmd_value)
    printTerminal(self, arrCmd, res)
        
def printTerminal(self,arrCmd, message):
    if arrCmd[1] == CMD.READ_YES:
        printMessage(self, message)
        
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
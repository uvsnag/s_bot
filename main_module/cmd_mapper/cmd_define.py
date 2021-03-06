from main_module.conf.config_loader import *
from main_module.ultils.fileUltils import *
from main_module.ultils.commonUltils import *
from main_module.model.command import *

botRes = Message.getBotResMessage()

def process(self, key, cusResq):
    process_internet(self, key, cusResq)
    
def process_internet(self, key, cusResq):
    arrCmd =  getAllCmdWKey(key, getArrAllModule(CSys.PATH_CMD)) 
    if StaticVar.CURRENT_INDEX_ARRLINK >= len(arrCmd):
        printMessage(self, botRes['nothing-more'])
        return
    curr_cmd = arrCmd[StaticVar.CURRENT_INDEX_ARRLINK]
    arr_cmd_detail = textToArray(curr_cmd, CKey.CMD_SPLIT_LV_1)
    cmd_type = arr_cmd_detail[0]
    cmd_is_show_result = arr_cmd_detail[1]
    cmd_link = arr_cmd_detail[2]
    cmd_selector = arr_cmd_detail[3]
    arr_cmd_selector = textToArray(cmd_selector, CKey.CMD_SPLIT_LV_2)
    if cmd_type == CMD.SLINK:
        url = cmd_link
    elif cmd_type == CMD.SEARCH:
        StaticVar.CURRENT_SEARCH_STR = cusResq
        url = getGgleSearchInPage(cusResq + " " + cmd_link, cmd_link)
    html = getContentFromLink(botRes, url)
    for sel in arr_cmd_selector:
        resStr = getContentForSelector(html, sel, cmd_is_show_result)
        printMessage(self, resStr)
    
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


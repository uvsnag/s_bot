from conf.config import *
from main_module.ultils.fileUltils import *
from main_module.ultils.common import *

botRes = Message.getBotResMessage()

def process(self, key, cusResq):
    arrCmd = getArrAllModule(CSys.PATH_CMD)
    arr =  getAllCmdWKey(key, arrCmd)
    print('list cmd:')
    print(arr)
    for item in arr:
        exc(self, item, cusResq)
    
def exc(self, cmd, cusResq):
    cmd = getValueMess(cmd)
    arrCmd = textToArray(cmd, CKey.SEPR_CMD_MAPPER) 
    if len(arrCmd) <= 1:
        print("Cmd is not valid")
        return
    cmd_key = arrCmd[0]
    if cmd_key == CMD.CMD:
        cmd_process(self, arrCmd)
    elif cmd_key == CMD.SLINK:
        slink_process(self, arrCmd)
    elif cmd_key == CMD.SEARCH:
        ggs_process(self, arrCmd, cusResq)
        
def cmd_process(self, arrCmd):
    cmd_value = arrCmd[2]
    res = exc_cmd(cmd_value)
    printTerminal(self, arrCmd, res)
        
def slink_process(self, arrCmd):
    cmd_link = arrCmd[2]
    getContentFromUrl(self, arrCmd, cmd_link)
    
def ggs_process(self, arrCmd, cusResq):
    cmd_link = arrCmd[2]
    
    url = ggleSearch(cusResq + " "+cmd_link, cmd_link)
    getContentFromUrl(self, arrCmd, url)
        
def printTerminal(self,arrCmd, message):
    if arrCmd[1] == CMD.READ_YES:
        printMessage(self, message)
        
def getContentFromUrl(self, arrCmd, url):
    iSeArr = [0]
    if len(arrCmd)>4:
        strIndex = arrCmd[4]
        iSeArr = textToArray(strIndex, CMD.SPLIT_INDEX)
    cmd_selector = arrCmd[3]
    res = getContentFromLink(botRes, url, cmd_selector, iSeArr)
    printTerminal(self, arrCmd, res)
        
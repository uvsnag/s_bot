from conf.config import *
from main_module.ultils.fileUltils import *
from main_module.ultils.common import *
botRes = Message.getBotResMessage()

def process(self, key):
    
    url = getCurrUrlFolder()+"\main_module\cmd_mapper\cmd_mapper.ini"
    arr =  getAllCmdWKey(key, readFileIntoArr(url))
    print('list cmd:')
    print(arr)
    for item in arr:
        exc(self, item)
    
def exc(self, cmd):
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
        
def cmd_process(self, arrCmd):
    cmd_value = arrCmd[2]
    res = exc_cmd(cmd_value)
    printTerminal(self, arrCmd, res)
        
def slink_process(self, arrCmd):
    cmd_link = arrCmd[2]
    cmd_selector = arrCmd[3]
    res = getContentFromLink(cmd_link, cmd_selector)
    printTerminal(self, arrCmd, res)
        
def printTerminal(self,arrCmd, message):
    if arrCmd[1] == CMD.READ_YES:
        printMessage(self, message)
        
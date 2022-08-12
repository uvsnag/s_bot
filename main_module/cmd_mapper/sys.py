from main_module.conf.config_loader import *
from main_module.common.ultils.fileUltils import *
from main_module.common.ultils.commonUltils import *
from main_module.common.ultils.cmdUltils import *
from main_module.model.command import *


botRes = Message.getBotResMessage()


def is_add_message_process(self, cusResq, key_equals, key):
    if StaticVar.PREV_KEY == CommandConstants.ADD_MESSAGE or  StaticVar.PREV_KEY == CommandConstants.ADD_MULT_MESSAGE:
        if key_equals == CommandConstants.DONE:
            add_message_auto(self, True, key_equals)
            return True
        if StaticVar.QUESING_MODE == ValStatic.QUESING_MODE_ADD_MESSAGE_KEY:
            if StaticVar.ANS == False:
                MessageObj.key = ""
                printMessage(self, botRes['enter-key'])
            else:
                printMessage(self, botRes['enter-message'])
            clearQues()
            return True
        add_message(self, cusResq) 
        return True   
    return False


def is_add_command_process(self, key_equals, key, cusResq):
    if StaticVar.PREV_KEY == CommandConstants.ADD_COMMAND_NEW or StaticVar.PREV_KEY == CommandConstants.ADD_COMMAND_EXIST:
        if key_equals == CommandConstants.DONE or (StaticVar.QUESING_MODE == ValStatic.QUESING_MODE_ADD_SELECTOR and StaticVar.ANS == False) :
            add_command_auto(self)
            StaticVar.QUESING_MODE == ValStatic.QUESING_MODE_NONE
        elif StaticVar.PREV_KEY == CommandConstants.ADD_COMMAND_NEW: #ADD_COMMAND_NEW
            if CommandObj.key == "":
                add_command(self, cusResq)
            else:
                if not key == CommandConstants.CANCEL:
                    add_command(self, cusResq)
        elif StaticVar.PREV_KEY == CommandConstants.ADD_COMMAND_EXIST: #ADD_COMMAND_EXIST
            if not key == CommandConstants.CANCEL:
                add_command(self, cusResq)
        return True
    
    return False
    
def add_command(self, value = None):
    if (not value == None) and (not value == ""):
        if CommandObj.key == "":
            CommandObj.key = value
            printMessage(self, botRes['enter-type'])
        elif CommandObj.type == "":
            CommandObj.type = value
            printMessage(self, botRes['enter-show-flag'])
        elif CommandObj.isShow == "":
            CommandObj.isShow = value
            printMessage(self, botRes['enter-link'])
        elif CommandObj.link == "":
            CommandObj.link = value
            printMessage(self, botRes['enter-selector'])
        else:
            if CommandObj.selector == "":
                CommandObj.selector = CommandObj.selector + value
                printMessage(self, botRes['enter-selector-index'])
                CommandObj.isDone1Selector = False
            else:
                if CommandObj.isDone1Selector == False: 
                    CommandObj.selector = CommandObj.selector + CKey.CMD_SPLIT_LV_3 + value
                    StaticVar.QUESING_MODE = ValStatic.QUESING_MODE_ADD_SELECTOR
                    CommandObj.isDone1Selector = True
                    printMessage(self, botRes['ques-selector-more'])
                else:
                    if StaticVar.QUESING_MODE == ValStatic.QUESING_MODE_ADD_SELECTOR and StaticVar.ANS == True:
                        clearQues()
                        printMessage(self, botRes['enter-selector'])
                        # CommandObj.isDone1Selector = False
                        
                    elif StaticVar.QUESING_MODE == ValStatic.QUESING_MODE_NONE:
                        CommandObj.selector = CommandObj.selector + CKey.CMD_SPLIT_LV_2 + value
                        printMessage(self, botRes['enter-selector-index'])
                        CommandObj.isDone1Selector = False
            
def add_message(self, value = None):
    if (not value == None) and (not value == ""):
        if MessageObj.key == "":
            MessageObj.key = value
            printMessage(self, botRes['enter-message'])
        elif MessageObj.message == "":
            MessageObj.message = value
            add_message_auto(self, False)
            
                        
def add_command_auto(self):
    clearQues()
    str = add_set_command_value()
    urlFile = getCurrUrlFolder() + CSys.PATH_BOT_GEN_CMD_MAPPER
    writeFile(urlFile, 1, str)
    clearAddCMD()
    printMessage(self, botRes['done'])
    StaticVar.PREV_KEY = ""
    
def add_message_auto(self, isEnd, key_equals = None):
    clearQues()
    if  not key_equals == CommandConstants.DONE:
        str =  MessageObj.key+ " " + CKey.SEPR_MESS + " " + MessageObj.message 
        urlFile = getCurrUrlFolder() + CSys.PATH_BOT_GEN_MESSAGE
        writeFile(urlFile, 1, str)
    if StaticVar.PREV_KEY == CommandConstants.ADD_MULT_MESSAGE and isEnd == False:
        MessageObj.message = "" 
        printMessage(self, botRes['enter-message'])
        return
    clearMessageObj()
    printMessage(self, botRes['done'])
    StaticVar.PREV_KEY = ""
    
                

def add_set_command_value():
    res = CommandObj.key+ " " + CKey.SEPR_MESS + " " + CommandObj.type 
    if not CommandObj.isShow == "":           
        res = res + CKey.CMD_SPLIT_LV_1 + CommandObj.isShow
    if not CommandObj.link == "":           
        res = res + CKey.CMD_SPLIT_LV_1 + CommandObj.link
    if not CommandObj.selector == "":           
        res = res + CKey.CMD_SPLIT_LV_1 + CommandObj.selector
    return res
 

def clearAddCMD():
    CommandObj.key = ""
    CommandObj.isShow = ""
    CommandObj.link = ""
    CommandObj.selector = ""
   
    
def clearMessageObj():
    MessageObj.key = ""
    MessageObj.message = ""
    
def clearQues():
    StaticVar.QUESING_MODE = ValStatic.QUESING_MODE_NONE
    StaticVar.ANS = ""
    

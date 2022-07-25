from main_module.conf.config_loader import *
from main_module.common.ultils.fileUltils import *
from main_module.common.ultils.commonUltils import *
from main_module.common.ultils.cmdUltils import *
from main_module.model.command import *

botRes = Message.getBotResMessage()

def cmd_process(self, arrCmd, cusResq):
    for cmd in arrCmd:
        arr_cmd_detail = textToArray(cmd, CKey.CMD_SPLIT_LV_1)
        cmd_content = arr_cmd_detail[2]
        res = exc_cmd(cmd_content)
        printTerminal(self, arrCmd, res)
        
    
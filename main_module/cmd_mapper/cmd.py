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
        arrVar = getArrVarValue(arr_cmd_detail[3])
        cmdStr=str(cmd_content).format(*arrVar)
        res = exc_cmd(cmdStr)
        print(cmdStr)
        printTerminal(self, arr_cmd_detail, res)
        
        
def getArrVarValue(varListStr):
    arrVar = textToArray(varListStr, CKey.CMD_SPLIT_LV_2)
    tempArr = []
    for var in arrVar:
        if str(var).startswith(SysValue.V_APPDIR):
            var = var[len(SysValue.V_APPDIR): len(var)]
            tempArr.append(getCurrUrlFolder() + var)
        else:
            tempArr.append(var)
    print(arrVar)
    print(tempArr)
    return tempArr
            
    
    
        
    
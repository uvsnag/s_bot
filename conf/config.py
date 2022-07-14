    
# VALUE

from tkinter import CURRENT


class VSys:
    VIE = "vie"
    ENG = "eng"
    
    
# CONFIG

class CKey:
    KEY_EXC = "<Return>"
    KEY_NEWLINE = "\n"
    SEPR_MESS = "="
    
    CMD_SPLIT_LV_1 = "'~'"
    CMD_SPLIT_LV_2 = "'^'"
    CMD_SPLIT_LV_3 = "'*'"
    
class CMD:
    CMD = "cmd"
    SEARCH = "ggs"
    SLINK = "slink"
    
    READ_NO = "0"
    READ_YES = "1"
    SPLIT_INDEX = ","
    SPLIT_LINK = ","
    
class CSys:
    APP_NAME = "s-bot"
    APP_LANG = VSys.VIE
    APP_FIRST_MESSAGE = 'hello'
    APP_ENCODE = 'UTF-8'
    
    PATH_MODULE_ARR =  ["\main_module", 
                        "\modules\google_search"
                        ]
    PATH_MESSAGE = "\message\\" + APP_LANG + "\data.ini"
    PATH_CMD = "\cmd_mapper\cmd_mapper.ini"
    CHECK_ACCENT_VIETNAMESE = False 
    
class VSearch:
    ARR_ACCESS_DENIED = ['Access Denied', "You don't have permission to access"]
    
class CSearch:
    DEFAULT_START_RESULT = 0
    DEFAULT_NUM_RESULT = 20
    DEFAULT_CHOOSE_LINK = 1

    
# VALUE

class VSys:
    VIE = "vie"
    ENG = "eng"
    
    
# CONFIG

class CKey:
    KEY_EXC = "<Return>"
    KEY_NEWLINE = "\n"
    SEPR_MESS = "="
    SEPR_CMD_MAPPER = "|~|"
    
class CMD:
    CMD = "cmd"
    SEARCH = "ggs"
    SLINK = "slink"
    
    READ_NO = "0"
    READ_YES = "1"
    SPLIT_INDEX = ","
    
class CSys:
    LANG = VSys.VIE
    PATH_MODULE_ARR =  ["\main_module", 
                        "\modules\google_search"
                        ]
    PATH_MESSAGE = "\message\\" + LANG + "\data.ini"
    PATH_CMD = "\cmd_mapper\cmd_mapper.ini"
    CHECK_ACCENT_VIETNAMESE = False 
    
class VSearch:
    ARR_ACCESS_DENIED = ['Access Denied', "You don't have permission to access"]
    
class CSearch:
    DEFAULT_START_RESULT = 0
    DEFAULT_NUM_RESULT = 20
    DEFAULT_CHOOSE_LINK = 1
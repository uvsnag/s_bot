    
import os
import configparser

class Loader:
    def loadConfig():
        URL_CONFIG_FILE = os.getcwd() + '\modules\conf.conf'
        config_obj = configparser.ConfigParser()
        config_obj.read(URL_CONFIG_FILE, encoding = 'UTF-8')
        return config_obj
    
    def getPropByKey(obj, key):
        value = obj[key].strip()
        firstChar = value[0]
        lastChar = value[len(value)-1]
        if firstChar == lastChar == "'" or firstChar == lastChar == '"':
            value =str(value[1:len(value)-1])
        elif value == 'False' or value == 'True':
            value = value == 'True'
        elif firstChar == '[' and lastChar == "]":
            strArr =str(value[1:len(value)-1])
            arr = strArr.split(',')
            value =[]
            for it in arr:
                it = it.strip()
                value.append(it[1:len(it)-1]) 
        else:
            value = int(value)
        # print(value)
        # print(type(value))
        return value
    
# CONFIG

class CKey:
    CKey = Loader.loadConfig()['CKey']
    KEY_EXC = '<Return>'
    KEY_NEWLINE = '\n'
    SEPR_MESS = Loader.getPropByKey(CKey, 'SEPR_MESS')
    
    CMD_SPLIT_LV_1 = Loader.getPropByKey(CKey, 'CMD_SPLIT_LV_1')
    CMD_SPLIT_LV_2 = Loader.getPropByKey(CKey, 'CMD_SPLIT_LV_2')
    CMD_SPLIT_LV_3 = Loader.getPropByKey(CKey, 'CMD_SPLIT_LV_3')
    
class CMD:
    CMDObj = Loader.loadConfig()['CMD']
    CMD =  Loader.getPropByKey(CMDObj, 'CMD')
    SEARCH = Loader.getPropByKey(CMDObj, 'SEARCH')
    SLINK = Loader.getPropByKey(CMDObj, 'SLINK')
    
    READ_NO = Loader.getPropByKey(CMDObj, 'READ_NO')
    READ_YES = Loader.getPropByKey(CMDObj, 'READ_YES')
    SPLIT_INDEX = Loader.getPropByKey(CMDObj, 'SPLIT_INDEX')
    SPLIT_LINK = Loader.getPropByKey(CMDObj, 'SPLIT_LINK')
    
class CSys:
    CSys = Loader.loadConfig()['CSys']
    
    APP_NAME = Loader.getPropByKey(CSys, 'APP_NAME')
    APP_LANG = Loader.getPropByKey(CSys, 'APP_LANG')
    APP_FIRST_MESSAGE = Loader.getPropByKey(CSys, 'APP_FIRST_MESSAGE')
    APP_ENCODE = Loader.getPropByKey(CSys, 'APP_ENCODE')
    
    PATH_MODULE_ARR =  Loader.getPropByKey(CSys, 'PATH_MODULE_ARR')
    PATH_BOT_MESSAGE = Loader.getPropByKey(CSys, 'PATH_BOT_MESSAGE')
    PATH_MESSAGE = "\message\\" + APP_LANG + "\data.ini"
    PATH_CMD = Loader.getPropByKey(CSys, 'PATH_CMD')
    PATH_BOT_GEN_CMD_MAPPER = Loader.getPropByKey(CSys, 'PATH_BOT_GEN_CMD_MAPPER')
    PATH_BOT_GEN_MESSAGE = "\modules\\"+"bot_gen\message\\" + APP_LANG + "\data.ini"
    CHECK_ACCENT_VIETNAMESE = Loader.getPropByKey(CSys, 'CHECK_ACCENT_VIETNAMESE') 
    
    ARR_CMD_NOT_CHECK_CASE_IN = ['ans-yes', "ans-no"]
    
class VSearch:
    VSearch = Loader.loadConfig()['VSearch']
    ARR_ACCESS_DENIED = Loader.getPropByKey(VSearch, 'ARR_ACCESS_DENIED')
    
class CSearch:
    CSearch = Loader.loadConfig()['CSearch']
    DEFAULT_START_RESULT = Loader.getPropByKey(CSearch, 'DEFAULT_START_RESULT')
    DEFAULT_NUM_RESULT = Loader.getPropByKey(CSearch, 'DEFAULT_NUM_RESULT')
    DEFAULT_CHOOSE_LINK = Loader.getPropByKey(CSearch, 'DEFAULT_CHOOSE_LINK')
    

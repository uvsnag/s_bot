    
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
    
    def reloadConfig():
        CSysv = Loader.loadConfig()['CSys']
        CSys.APP_NAME = Loader.getPropByKey(CSysv, 'APP_NAME')
        CSys.APP_LANG = Loader.getPropByKey(CSysv, 'APP_LANG')
        CSys.APP_FIRST_MESSAGE = Loader.getPropByKey(CSysv, 'APP_FIRST_MESSAGE')
        CSys.APP_ENCODE = Loader.getPropByKey(CSysv, 'APP_ENCODE')
        CSys.USE_READ = Loader.getPropByKey(CSysv, 'USE_READ')
        CSys.PATH_MODULE_ARR =  Loader.getPropByKey(CSysv, 'PATH_MODULE_ARR')
        CSys.PATH_BOT_MESSAGE = Loader.getPropByKey(CSysv, 'PATH_BOT_MESSAGE')
        CSys.PATH_CMD = Loader.getPropByKey(CSysv, 'PATH_CMD')
        CSys.PATH_BOT_GEN_CMD_MAPPER = Loader.getPropByKey(CSysv, 'PATH_BOT_GEN_CMD_MAPPER')
        CSys.CHECK_ACCENT_VIETNAMESE = Loader.getPropByKey(CSysv, 'CHECK_ACCENT_VIETNAMESE') 
        CSys.PATH_MESSAGE = str(Loader.getPropByKey(CSysv, 'PATH_MESSAGE')).format(CSys.APP_LANG)
        CSys.PATH_BOT_GEN_MESSAGE = str(Loader.getPropByKey(CSysv, 'PATH_BOT_GEN_MESSAGE')).format(CSys.APP_LANG)
        CSys.PATH_CMD_OPEN = Loader.getPropByKey(CSysv, 'PATH_CMD_OPEN')
        CSys.ARR_CMD_NOT_CHECK_CASE_IN = Loader.getPropByKey(CSysv, 'ARR_CMD_NOT_CHECK_CASE_IN')
        CSys.MAX_SAVE_COMMAND = Loader.getPropByKey(CSysv, 'MAX_SAVE_COMMAND')
        VSearchv = Loader.loadConfig()['VSearch']
        VSearch.ARR_LEAGUE_TODAY = Loader.getPropByKey(VSearchv, 'ARR_LEAGUE_TODAY')
        VSearch.ARR_ACCESS_DENIED = Loader.getPropByKey(VSearchv, 'ARR_ACCESS_DENIED')
        CSearchv = Loader.loadConfig()['CSearch']
        CSearch.DEFAULT_START_RESULT = Loader.getPropByKey(CSearchv, 'DEFAULT_START_RESULT')
        CSearch.DEFAULT_NUM_RESULT = Loader.getPropByKey(CSearchv, 'DEFAULT_NUM_RESULT')
        CSearch.DEFAULT_CHOOSE_LINK = Loader.getPropByKey(CSearchv, 'DEFAULT_CHOOSE_LINK')
        CSearch.DEFAULT_NUM_NEWS = Loader.getPropByKey(CSearchv, 'DEFAULT_NUM_NEWS')
   
# CONFIG

class CSys:
    CSys = Loader.loadConfig()['CSys']
    
    APP_NAME = Loader.getPropByKey(CSys, 'APP_NAME')
    APP_LANG = Loader.getPropByKey(CSys, 'APP_LANG')
    APP_FIRST_MESSAGE = Loader.getPropByKey(CSys, 'APP_FIRST_MESSAGE')
    APP_ENCODE = Loader.getPropByKey(CSys, 'APP_ENCODE')
    USE_READ = Loader.getPropByKey(CSys, 'USE_READ')
    USE_RECOGN_VOICE = Loader.getPropByKey(CSys, 'USE_RECOGN_VOICE')
    
    PATH_MODULE_ARR =  Loader.getPropByKey(CSys, 'PATH_MODULE_ARR')
    PATH_BOT_MESSAGE = Loader.getPropByKey(CSys, 'PATH_BOT_MESSAGE')
    PATH_CMD = Loader.getPropByKey(CSys, 'PATH_CMD')
    PATH_BOT_GEN_CMD_MAPPER = Loader.getPropByKey(CSys, 'PATH_BOT_GEN_CMD_MAPPER')
    CHECK_ACCENT_VIETNAMESE = Loader.getPropByKey(CSys, 'CHECK_ACCENT_VIETNAMESE') 
    
    
    PATH_MESSAGE = str(Loader.getPropByKey(CSys, 'PATH_MESSAGE')).format(APP_LANG)
    PATH_BOT_GEN_MESSAGE = str(Loader.getPropByKey(CSys, 'PATH_BOT_GEN_MESSAGE')).format(APP_LANG)
    PATH_CMD_OPEN = Loader.getPropByKey(CSys, 'PATH_CMD_OPEN')
    ARR_CMD_NOT_CHECK_CASE_IN = Loader.getPropByKey(CSys, 'ARR_CMD_NOT_CHECK_CASE_IN')
    MAX_SAVE_COMMAND = Loader.getPropByKey(CSys, 'MAX_SAVE_COMMAND')
    
class VSearch:
    VSearch = Loader.loadConfig()['VSearch']
    ARR_LEAGUE_TODAY = Loader.getPropByKey(VSearch, 'ARR_LEAGUE_TODAY')
    ARR_ACCESS_DENIED = Loader.getPropByKey(VSearch, 'ARR_ACCESS_DENIED')
    
class CSearch:
    CSearch = Loader.loadConfig()['CSearch']
    DEFAULT_START_RESULT = Loader.getPropByKey(CSearch, 'DEFAULT_START_RESULT')
    DEFAULT_NUM_RESULT = Loader.getPropByKey(CSearch, 'DEFAULT_NUM_RESULT')
    DEFAULT_CHOOSE_LINK = Loader.getPropByKey(CSearch, 'DEFAULT_CHOOSE_LINK')
    DEFAULT_NUM_NEWS = Loader.getPropByKey(CSearch, 'DEFAULT_NUM_NEWS')
    

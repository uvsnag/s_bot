class ValStatic:
    QUESING_MODE_NONE = 0
    QUESING_MODE_ADD_SELECTOR = 1
    QUESING_MODE_ADD_MESSAGE_KEY = 2
    
# value can be changed
class StaticVar:
    CURRENT_INDEX_ARRLINK = 0
    PREV_KEY = ""
    CURRENT_SEARCH_STR = ""
    IS_CHANGE_COMMAND = False
    QUESING_MODE = ValStatic.QUESING_MODE_NONE
    ANS = ""
    
    LIST_LINK_SEARCH = []
    LIST_ELE_GET_CONTENT = ['#content', 'article', '.content', '.contents']
    
    LIST_COMMAND_OLD = []
    MAX_SAVE_COMMAND = 50
    INDEX_LIST_COMMAND_OLD = 0
    COMMAND_OLD_FLAG = True
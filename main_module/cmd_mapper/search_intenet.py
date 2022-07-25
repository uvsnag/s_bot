from main_module.conf.config_loader import *
from main_module.common.ultils.fileUltils import *
from main_module.common.ultils.commonUltils import *
from main_module.common.ultils.cmdUltils import *
from main_module.model.command import *
import requests
from bs4 import BeautifulSoup

botRes = Message.getBotResMessage()

# def process(self, key, cusResq):
#     process_internet(self, key, cusResq)
    
def process_internet(self, arrCmd, cusResq):
    # arrCmd =  getAllCmdWKey(key, getArrAllModule(CSys.PATH_CMD)) 
    if StaticVar.CURRENT_INDEX_ARRLINK >= len(arrCmd):
        printMessage(self, botRes['nothing-more'])
        return
    curr_cmd = arrCmd[StaticVar.CURRENT_INDEX_ARRLINK]
    arr_cmd_detail = textToArray(curr_cmd, CKey.CMD_SPLIT_LV_1)
    cmd_type = arr_cmd_detail[0]
    cmd_is_show_result = arr_cmd_detail[1]
    cmd_link = arr_cmd_detail[2]
    cmd_selector = arr_cmd_detail[3]
    arr_cmd_selector = textToArray(cmd_selector, CKey.CMD_SPLIT_LV_2)
    if cmd_type == CMD.SLINK:
        url = cmd_link
    elif cmd_type == CMD.SEARCH:
        StaticVar.CURRENT_SEARCH_STR = cusResq
        url = getGgleSearchInPage(cusResq + " " + cmd_link, cmd_link)
    html = getContentFromLink(botRes, url)
    for sel in arr_cmd_selector:
        resStr = getContentForSelector(html, sel, cmd_is_show_result)
        printMessage(self, resStr)
    

def getContentFromLink(botRes, url):
    f = requests.get(url)
    html = f.text
    if isStrContainArr(VSearch.ARR_ACCESS_DENIED, html):
       print(html)
       return botRes['access-denied']
    # print(html)
    return html

def getContentForSelector(html, seleStr, cmd_is_show_result):
    #arrCmdMatch ->  #mw-content-text .mw-parser-output > p'*'0,1,2,3
    resStr = ''
    soup = BeautifulSoup(html, "html.parser")
    arr_sele = textToArray(seleStr, CKey.CMD_SPLIT_LV_3)
    sel_poiter = arr_sele[0]
    sel_index_arr = [0]
    if len(arr_sele)>1:
        sel_index_arr = textToArray(arr_sele[1], CMD.SPLIT_INDEX)
    print('searching content with selector:' + sel_poiter)
    results = soup.select(sel_poiter)
    if len(results) > 0:
        for i in sel_index_arr:
            if int(i) < len(results):
                if cmd_is_show_result == CMD.READ_YES:
                    resStr = resStr + results[int(i)].text +'\n'
    return resStr
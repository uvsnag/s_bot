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
    return html

def getContentForSelector(html, seleStr, cmd_is_show_result, newLine = '\n'):
    #arrCmdMatch ->  #mw-content-text .mw-parser-output > p'*'0,1,2,3
    resStr = ''
    soup = BeautifulSoup(html, "html.parser")
    arr_sele = textToArray(seleStr, CKey.CMD_SPLIT_LV_3)
    sel_poiter = arr_sele[0]
    sel_index_arr = [0]
    if len(arr_sele)>1:
        strIndex = arr_sele[1]
        if strIndex == CMD.SELECTOR_IND_ALL:
            strIndex = genStrIndex(CSearch.DEFAULT_NUM_NEWS)
        sel_index_arr = textToArray(strIndex, CMD.SPLIT_INDEX)
    print('searching content with selector:' + sel_poiter)
    results = soup.select(sel_poiter)
    if len(results) > 0:
        for i in sel_index_arr:
            if int(i) < len(results):
                if cmd_is_show_result == CMD.READ_YES or cmd_is_show_result == CMD.READ_LISTEN_YES:
                    resStr = resStr + results[int(i)].text.strip() + newLine
    return resStr


def searchGetContent(self, cusResq):
    if len(StaticVar.LIST_LINK_SEARCH) == 0:
        searchStr = cusResq[5: len(cusResq)]
        StaticVar.LIST_LINK_SEARCH = getArrLinkFromSearch(searchStr)
        print('list link:')
        print(StaticVar.LIST_LINK_SEARCH)
    if StaticVar.CURRENT_INDEX_ARRLINK >= len(StaticVar.LIST_LINK_SEARCH):
        printMessage(self, botRes['nothing-more'])
        return
    print('curr link:')
    print(StaticVar.LIST_LINK_SEARCH[StaticVar.CURRENT_INDEX_ARRLINK])
    html = getContentFromLink(botRes, StaticVar.LIST_LINK_SEARCH[StaticVar.CURRENT_INDEX_ARRLINK])
    resStr = getContent(html)
    printMessage(self, str(resStr))
    
def getContent(html):
    soup = BeautifulSoup(html, "html.parser")
    # soup = soup.select('#content')
    soup = getSoupHtmlWArrEle(soup)
    soup = BeautifulSoup(str(soup), "html.parser")
    soup = remove_tags(soup)
    # soup = '\n'.join(soup.stripped_strings)
    return soup
    
def remove_tags(soup):
    for data in soup(['style', 'script', 'form', 'img', 'input', 'select', 'link']):
        # Remove tags
        data.decompose()
    # return data by retrieving the tag content
    # return '\n'.join(soup.stripped_strings)
    return soup

def getSoupHtmlWArrEle(soup):
    for ele in StaticVar.LIST_ELE_GET_CONTENT:
        soup = soup.select(ele)
        if len(soup) >0:
            print(soup)
            return soup
    return ""


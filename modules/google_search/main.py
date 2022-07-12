import requests
from googlesearch import search
from modules.google_search.conf.config import *
from main_module.ultils.fileUltils import *
from main_module.ultils.common import *
from bs4 import BeautifulSoup
import json

def googleSearch(self, botRes, searchStr, numOfPage = CSearch.DEFAULT_NUM_RESULT):
    print("searching :"+searchStr)
    search_results = search(searchStr, start=CSearch.DEFAULT_START_RESULT, stop = numOfPage, pause=2)
    url = ''
    for res in search_results:
        print("checked url:" +res)
        if isLinkValid(res):
            url = res
            print("opening url:" +res)
            break
    if url == '':
        printMessage(self, botRes['cmd-not-found'])
        return
    getContentOfUrl_Request(url)   
        
        
def getContentOfUrl_Request(url):
    f = requests.get(url)
    html = f.text
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script"]):
        if 'window.SA = ' in script.text:
            jsonStr = script.text.split('window.SA = ')[1]
            jsonStr = jsonStr.rsplit(';',1)[0]
            jsonObj = json.loads(jsonStr)

    title = jsonObj['pageConfig']['Data']['article']['title']
    print (title)
    
def isLinkValid(url):
    if CRESULT.TYPE_RES == VSearch.TYPE_TXT:
        for media in VSearch.ARR_MEDIA:
            if media in url:
                return False
    return True

    
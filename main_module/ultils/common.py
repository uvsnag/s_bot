# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import subprocess
import tkinter as tk
from conf.config import *
from googlesearch import search
import re
# from modules.google_search.main import *
# from main_module.ultils.fileUltils import *

# botRes = Message.getBotResMessage()

def exc_cmd(cmd):
    if not cmd:
       return
    print("executing :"+cmd)
    cmd_res = subprocess.getoutput(cmd) + "\n"
    return cmd_res

def getContentFromLink(botRes, url, der, iSeArr):
    f = requests.get(url)
    html = f.text
    if isStrContainArr(VSearch.ARR_ACCESS_DENIED, html):
       print(html)
       return botRes['access-denied']
    soup = BeautifulSoup(html, "html.parser")
    results = soup.select(der)
    print('selector:'+ der)
    print("num of selector detected: "+str(len(results)))
    if len(results) > 0:
        reStr = ''
        
        lLoop = iSeArr
        if len(results) < len(iSeArr):
            lLoop = results
            
        for i in lLoop:
            reStr += results[int(i)].text
        print("Result is recieved.")
        return reStr
    return botRes['cmd-not-found']

def printMessage(self, message):
    message=  '\n' + message + '\n'
    self.txt_terminal.insert(tk.END, message)
    self.txt_terminal.see(tk.END)
    
def isStrContainArr(arr, str):
    for item in arr:
         if item.strip() in str.strip():
             return True
    return False

def isArrContainStr(arr, str):
    for item in arr:
         if isContainTrim(str, item):
             return True
    return False

def isEqualArr(arr, str):
    for item in arr:
         if isEqualTrim(item, str):
             return True
    return False

def textToArray(content, split):
    deterChar = '`'
    content = content.replace(split, deterChar)
    arr = content.split(deterChar)
    return arr

def textToArray(content, split):
    deterChar = '`'
    content = content.replace(split, deterChar)
    arr = content.split(deterChar)
    return arr

def ggleSearch(searchStr, inPage):
    print("gg searching :"+searchStr)
    search_results = search(searchStr, start=CSearch.DEFAULT_START_RESULT, stop = CSearch.DEFAULT_NUM_RESULT, pause=2)
    url = ''
    for res in search_results:
        print("checked url:" +res)
        if isLinkValid(res, [inPage]):
            url = res
            print("opening url:" +res)
            break
    return url
    
def isLinkValid(url, arrPage):
    for page in arrPage:
        if page in url:
            return True
    return False

def isEqualTrim(a, b):
    result = False
    if a == '' or b == '':
        return False
    if CSys.CHECK_ACCENT_VIETNAMESE :
        result = a.strip().upper() == b.strip().upper()
    else:
        result = no_accent_vietnamese(a.strip().upper()) == no_accent_vietnamese(b.strip().upper())
    return result

def isContainTrim(a, b):
    result = False
    if a == '' or b == '':
        return False
    if CSys.CHECK_ACCENT_VIETNAMESE :
        result = a.strip().upper() in b.strip().upper()
    else:
        result = no_accent_vietnamese(a.strip().upper()) in no_accent_vietnamese(b.strip().upper())
    return result

def no_accent_vietnamese(str):
    arr_a=["à","á","ạ","ả",'ã','â','ầ','ấ','ậ','ẩ','ẫ','ă','ằ','ắ','ặ','ẳ','ẵ']
    arr_e=['è','é','ẹ','ẻ','ẽ','ê','ề','ế','ệ','ể','ễ']
    arr_o =['ò''ó''ọ''ỏ''õ''ô''ồ''ố''ộ''ổ''ỗ''ơ''ờ''ớ''ợ''ở''ỡ']
    arr_i =['ì','í','ị','ỉ','ĩ']
    arr_u=['ù','ú','ụ','ủ','ũ','ư','ừ','ứ','ự','ử','ữ']
    arr_u=['ỳ','ý','ỵ','ỷ','ỹ']
    arr_d=['đ']
    
    arr_a_L=["À","Á","Ạ","Ả",'Ã','Â','Ầ','Ấ','Ậ','Ẩ','Ẫ','Ă','Ằ','Ắ','Ặ','Ẳ','Ẵ']
    arr_e_L=['È','É','Ẹ','Ẻ','Ẽ','Ê','Ề','Ế','Ệ','Ể','Ễ']
    arr_o_L =['Ò''Ó''Ọ''Ỏ''Õ''Ô''Ồ''Ố''Ộ''Ổ''Ỗ''Ơ''Ờ''Ớ''Ợ''Ở''Ỡ']
    arr_i_L =['Ì','Í','Ị','Ỉ','Ĩ']
    arr_u_L=['Ù','Ú','Ụ','Ủ','Ũ','Ư','Ừ','Ứ','Ự','Ử','Ữ']
    arr_u_L=['Ỳ','Ý','Ỵ','Ỷ','Ỹ']
    arr_d_L=['Đ']
    
    str = replaceStrWArr(arr_a, 'a', str)
    str = replaceStrWArr(arr_e, 'e', str)
    str = replaceStrWArr(arr_o, 'o', str)
    str = replaceStrWArr(arr_i, 'i', str)
    str = replaceStrWArr(arr_u, 'u', str)
    str = replaceStrWArr(arr_d, 'd', str)
    str = replaceStrWArr(arr_u, 'a', str)
    
    str = replaceStrWArr(arr_a_L, 'A', str)
    str = replaceStrWArr(arr_e_L, 'E', str)
    str = replaceStrWArr(arr_o_L, 'O', str)
    str = replaceStrWArr(arr_i_L, 'I', str)
    str = replaceStrWArr(arr_u_L, 'U', str)
    str = replaceStrWArr(arr_d_L, 'D', str)
    str = replaceStrWArr(arr_u_L, 'A', str)
    
    print("no_accent_vietnamese: "+str)
    return str

def replaceStrWArr(arr, char,  str):
    for item in arr:
       str=str.replace(item, char) 
    return str

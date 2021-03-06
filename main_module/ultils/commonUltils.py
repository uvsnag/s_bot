# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import subprocess
import tkinter as tk
from main_module.conf.config_loader import *
from googlesearch import search
from main_module.common.static_value import *
from main_module.common.constants import *
import os

def exc_cmd(cmd):
    if not cmd:
       return
    print("executing :"+cmd)
    cmd_res = subprocess.getoutput(cmd) + "\n"
    return cmd_res

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
    
def printMessage(self, message):
    message=  '\n' + message + '\n'
    self.txt_terminal.insert(tk.END, message)
    self.txt_terminal.see(tk.END)
    
def isStrContainArr(arr, str):
    for item in arr:
         if isContainTrim(str, item):
             return True
    return False


def isArrContainStr(arr, str):
    for item in arr:
         if isContainTrim(item, str):
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

def getGgleSearchInPage(searchStr, inPage):
    print("gg searching :"+searchStr)
    search_results = search(searchStr, start = CSearch.DEFAULT_START_RESULT, stop = CSearch.DEFAULT_NUM_RESULT, pause=2)
    url = ''
    for res in search_results:
        print("checking url:" +res)
        if isLinkValid(res, [inPage]):
            url = res
            print("opening url:" +res)
            break
    return url
def getAllGgleSearchInPageArr(searchStr, inPageArr):
    print("gg searching :"+searchStr)
    search_results = search(searchStr, start = CSearch.DEFAULT_START_RESULT, stop = CSearch.DEFAULT_NUM_RESULT, pause=2)
    urlArr = []
    for res in search_results:
        print("checked url:" +res)
        if isLinkValid(res, inPageArr):
            urlArr.append(res)
            print("add url:" +res)
            break
    return urlArr
    
def isLinkValid(url, arrPage):
    for page in arrPage:
        if page in url:
            return True
    return False

def isEqualTrim(a, b, isCheckAcc = CSys.CHECK_ACCENT_VIETNAMESE):
    result = False
    if a == '' or b == '':
        return False
    if isCheckAcc :
        result = a.strip().upper() == b.strip().upper()
    else:
        result = no_accent_vietnamese(a.strip().upper()) == no_accent_vietnamese(b.strip().upper())
    return result

def isContainTrim(b, a, isCheckAcc = CSys.CHECK_ACCENT_VIETNAMESE):
    result = False
    if a == '' or b == '':
        return False
    if isCheckAcc :
        result = a.strip().upper() in b.strip().upper()
    else:
        result = no_accent_vietnamese(a.strip().upper()) in no_accent_vietnamese(b.strip().upper())
    return result

def no_accent_vietnamese(str):
    arr_a=["??","??","???","???",'??','??','???','???','???','???','???','??','???','???','???','???','???']
    arr_e=['??','??','???','???','???','??','???','???','???','???','???']
    arr_o =['??','??','???','???','??','??','???','???','???','???','???','??','???','???','???','???','???']
    arr_i =['??','??','???','???','??']
    arr_u=['??','??','???','???','??','??','???','???','???','???','???']
    arr_u=['???','??','???','???','???']
    arr_d=['??']
    
    arr_a_L=["??","??","???","???",'??','??','???','???','???','???','???','??','???','???','???','???','???']
    arr_e_L=['??','??','???','???','???','??','???','???','???','???','???']
    arr_o_L =['??','??','???','???','??','??','???','???','???','???','???','??','???','???','???','???','???']
    arr_i_L =['??','??','???','???','??']
    arr_u_L=['??','??','???','???','??','??','???','???','???','???','???']
    arr_u_L=['???','??','???','???','???']
    arr_d_L=['??']
    # print("no_accent_vietnamese start: "+str)
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
    
    # print("no_accent_vietnamese/ end: "+str)
    return str

def replaceStrWArr(arr, char,  str):
    for item in arr:
       str=str.replace(item, char) 
    return str

def getCurrUrlFolder():
    directory = os.getcwd()
    return directory


    
# -*- coding: utf-8 -*-

# from bs4 import BeautifulSoup
# import requests
# import subprocess
# import tkinter as tk
from main_module.conf.config_loader import *
from googlesearch import search
from main_module.common.static_var.static_value import *
from main_module.common.static_var.constants import *
import os

    
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

# def textToArray(content, split):
#     deterChar = '`'
#     content = content.replace(split, deterChar)
#     arr = content.split(deterChar)
#     return arr



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
    arr_a=["à","á","ạ","ả",'ã','â','ầ','ấ','ậ','ẩ','ẫ','ă','ằ','ắ','ặ','ẳ','ẵ']
    arr_e=['è','é','ẹ','ẻ','ẽ','ê','ề','ế','ệ','ể','ễ']
    arr_o =['ò','ó','ọ','ỏ','õ','ô','ồ','ố','ộ','ổ','ỗ','ơ','ờ','ớ','ợ','ở','ỡ']
    arr_i =['ì','í','ị','ỉ','ĩ']
    arr_u=['ù','ú','ụ','ủ','ũ','ư','ừ','ứ','ự','ử','ữ']
    arr_u=['ỳ','ý','ỵ','ỷ','ỹ']
    arr_d=['đ']
    
    arr_a_L=["À","Á","Ạ","Ả",'Ã','Â','Ầ','Ấ','Ậ','Ẩ','Ẫ','Ă','Ằ','Ắ','Ặ','Ẳ','Ẵ']
    arr_e_L=['È','É','Ẹ','Ẻ','Ẽ','Ê','Ề','Ế','Ệ','Ể','Ễ']
    arr_o_L =['Ò','Ó','Ọ','Ỏ','Õ','Ô','Ồ','Ố','Ộ','Ổ','Ỗ','Ơ','Ờ','Ớ','Ợ','Ở','Ỡ']
    arr_i_L =['Ì','Í','Ị','Ỉ','Ĩ']
    arr_u_L=['Ù','Ú','Ụ','Ủ','Ũ','Ư','Ừ','Ứ','Ự','Ử','Ữ']
    arr_u_L=['Ỳ','Ý','Ỵ','Ỷ','Ỹ']
    arr_d_L=['Đ']
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

def formatStrWArrValue(str, arr):
    return str.format(*arr)

def genStrIndex(limitNum, split = ','):
    flag = False
    resStr = ''
    i = 0
    while i < limitNum:
        if flag == False:
            resStr = resStr + str(i)
            flag = True
        else:
            resStr = resStr + split + str(i)
        i=i+1
    print('selector index gen:')
    print(resStr)
    return resStr

    
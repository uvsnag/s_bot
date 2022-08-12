from main_module.conf.config_loader import *
from main_module.common.ultils.fileUltils import *
from main_module.common.ultils.commonUltils import *
from main_module.common.ultils.cmdUltils import *
from main_module.model.command import *
from main_module.cmd_mapper.search_intenet import *



def getNewsGlobal(self):
    arrCmd =  getAllCmdWKey('get-news', getArrAllModule(CSys.PATH_CMD)) 
    for curr_cmd in arrCmd:
        arr_cmd_detail = textToArray(curr_cmd, CKey.CMD_SPLIT_LV_1)
        cmd_is_show_result = arr_cmd_detail[1]
        cmd_link = arr_cmd_detail[2]
        cmd_selector = arr_cmd_detail[3]
        
        f = requests.get(cmd_link)
        html = f.text
        arr_cmd_selector = textToArray(cmd_selector, CKey.CMD_SPLIT_LV_2)
        for sel in arr_cmd_selector:
            resStr = getContentForSelector(html, sel, cmd_is_show_result, '\n\n')
            printTerminal(self, cmd_is_show_result, resStr)
            
        

def getScheduleFootball(self):
    printMessage(self, "Lịch thi đấu")
    arrCmd =  getAllCmdWKey('schedule-football', getArrAllModule(CSys.PATH_CMD)) 
    old_link = ""
    old_Html = ""
    for curr_cmd in arrCmd:
        html = None
        arr_cmd_detail = textToArray(curr_cmd, CKey.CMD_SPLIT_LV_1)
        cmd_is_show_result = arr_cmd_detail[1]
        cmd_link = arr_cmd_detail[2]
        cmd_selector = arr_cmd_detail[3]
        if old_link == cmd_link:
            html = old_Html
        else:
            print("opened link:")
            print(cmd_link)
            f = requests.get(cmd_link)
            html = f.text
            old_Html = html
            old_link = cmd_link
        arr_cmd_selector = textToArray(cmd_selector, CKey.CMD_SPLIT_LV_2)
        for sel in arr_cmd_selector:
            resStr = getContentForSelector(html, sel, cmd_is_show_result, '')
            if 1 == 1:
                resStr = resStr.replace('\n', '-')
            else:
                resStr = resStr.replace('\n', ' ')
                resStr = resStr.replace(':', ' giờ ')
                resStr = resStr.replace('-', ' tháng ')
            printMessage(self, resStr)
        

def getScheduleFootballToday(self):
    printMessage(self, '===================')
    printMessage(self, "Lịch thi đấu hôm nay")
    arrCmd =  getAllCmdWKey('schedule-football-today', getArrAllModule(CSys.PATH_CMD)) 
    
    arr_cmd_detail = textToArray(arrCmd[0], CKey.CMD_SPLIT_LV_1)
    cmd_is_show_result = arr_cmd_detail[1]
    cmd_link = arr_cmd_detail[2]
    cmd_selector = arr_cmd_detail[3]
    f = requests.get(cmd_link)
    html = f.text
    soup = BeautifulSoup(html, "html.parser")
    arr_cmd_selector = textToArray(cmd_selector, CKey.CMD_SPLIT_LV_2)
    results = soup.select(arr_cmd_selector[0])
    if len(results) > 0:
         for item in results:
             soup2 = BeautifulSoup(str(item), "html.parser")
             
             if isStrContainArr(VSearch.ARR_LEAGUE_TODAY, str(soup2.select(arr_cmd_selector[1]))):  
                 printMessage(self, '===================')
                 printMessage(self, str(soup2.select(arr_cmd_selector[1])[0].text.strip()))
                 
                 items = soup2.select(arr_cmd_selector[2])
                 for item2 in items:
                     printMessage(self, str(item2.text.strip()))



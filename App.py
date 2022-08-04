# from this import d
import tkinter as tk
from tkinter import scrolledtext
from main_module.conf.config_loader import *
from main_module.common.ultils.fileUltils import *
from main_module.common.ultils.commonUltils import *
from main_module.cmd_mapper.cmd import *
from main_module.cmd_mapper.sys import *
from main_module.cmd_mapper.search_intenet import *
from main_module.common.static_var.static_value import *
from main_module.common.static_var.constants import *


botRes = Message.getBotResMessage()
data = Message.getDataMessage()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.txt_terminal = scrolledtext.ScrolledText(height=25, width=85)
        # self.txt_terminal.bind(CKey.KEY_EXC, self.on_execute)
        self.txt_terminal.pack()
        self.txt_terminal.place(x=30, y=40)
        
        self.txt_input = tk.Entry(width=113)
        self.contents_input1 = tk.StringVar()
        self.txt_input["textvariable"] = self.contents_input1
        self.txt_input.bind(CKey.KEY_EXC, self.on_execute)
        self.txt_input.bind('<Up>', self.showOldCommand)
        self.txt_input.bind('<Down>', self.showOldCommand)
        self.txt_input.pack()
        self.txt_input.place(x=30, y=450)
        
        printMessage(self, botRes[CSys.APP_FIRST_MESSAGE])
        self.txt_input.focus()
    def on_execute(self, event = None):
        cusResq = self.getMessageFromCus()
        StaticVar.LIST_COMMAND_OLD.append(cusResq)
        StaticVar.INDEX_LIST_COMMAND_OLD = len(StaticVar.LIST_COMMAND_OLD)
        StaticVar.COMMAND_OLD_FLAG = True
        
        key = deterCommand(cusResq, data)
        key_equals = deterCommandEquals(cusResq, data)
        print('prev key:'+ StaticVar.PREV_KEY)
        self.check_ans(key_equals)
        
        if (not key == CommandConstants.NEXT_RESULT):
            StaticVar.CURRENT_INDEX_ARRLINK = 0
            StaticVar.LIST_LINK_SEARCH = []
        # ADD_MESAGE
        if is_add_message_process(self, cusResq, key_equals, key) == True:
            return
        # ADD_COMMAND
        if is_add_command_process(self, key_equals, key, cusResq) == True:
            return
        #  
        if not key or key == '':
            printMessage(self, botRes[CommandConstants.CMD_NOT_FOUND])
            return
        if key_equals == "":
            self.exc_with_key(key, cusResq)
            print('exc in mode: IN')
        else:
            self.exc_with_key(key_equals, cusResq)
            print('exc in mode: EQUALS')
            
         
    
    def exc_with_key(self, key, cusResq):
        match key:
            case CommandConstants.ADD_COMMAND_EXIST:
                if StaticVar.PREV_KEY == "":
                    printMessage(self, botRes['where-to-add'])
                    return 
                add_command(self, StaticVar.PREV_KEY)
                StaticVar.PREV_KEY = key
            case CommandConstants.ADD_COMMAND_NEW:
                printMessage(self, botRes['enter-key'])
                StaticVar.PREV_KEY = key
            case CommandConstants.ADD_MESSAGE:
                self.caseAddMessage( key)
            case CommandConstants.ADD_MULT_MESSAGE:
                self.caseAddMessage(key)
            case CommandConstants.NEXT_RESULT:
                StaticVar.CURRENT_INDEX_ARRLINK = StaticVar.CURRENT_INDEX_ARRLINK + 1
                if StaticVar.PREV_KEY == "":
                    printMessage(self, "???")
                    return 
                elif StaticVar.PREV_KEY == CommandConstants.SEARCH_GET_CONTENT:
                    searchGetContent(self, cusResq)
                    return
                else:
                    self.process(StaticVar.PREV_KEY, StaticVar.CURRENT_SEARCH_STR)
            case CommandConstants.SEARCH_GET_CONTENT:
                searchGetContent(self, cusResq)
                StaticVar.PREV_KEY = key
            case _:
                self.searchGG(key, cusResq)
        
    def searchGG(self, key, cusResq):
        # StaticVar.CURRENT_INDEX_ARRLINK = 0
        StaticVar.CURRENT_SEARCH_STR = ''
        self.process(key, cusResq)
        StaticVar.PREV_KEY = key   
        
    def caseAddMessage(self, key):
        if not StaticVar.PREV_KEY == "":
            MessageObj.key = StaticVar.PREV_KEY
            StaticVar.QUESING_MODE = ValStatic.QUESING_MODE_ADD_MESSAGE_KEY
            printMessage(self, botRes['ques-add-curr-key'].format(key))
        else:
            printMessage(self, botRes['enter-key'])
        StaticVar.PREV_KEY = key
       
    def check_ans(self, key_equals):
         if (not StaticVar.QUESING_MODE == ValStatic.QUESING_MODE_NONE) and StaticVar.ANS == "":
            if key_equals == CommandConstants.ANS_YES:
                StaticVar.ANS = True
            if key_equals == CommandConstants.ANS_NO:
                StaticVar.ANS = False
   
    def process(self, key, cusResq):
        arrCmd =  getAllCmdWKey(key, getArrAllModule(CSys.PATH_CMD)) 
        first_cmd = arrCmd[0]
        arr_cmd_detail = textToArray(first_cmd, CKey.CMD_SPLIT_LV_1)
        cmd_type = arr_cmd_detail[0]
        if cmd_type == CMD.CMD:
            cmd_process(self, arrCmd, cusResq)
        else:
            process_internet(self, arrCmd, cusResq)
    
    
    def getMessageFromCus(self):
        txtcmd = self.txt_input.get().strip()
        printMessage(self, txtcmd)
        self.txt_input.delete(0, tk.END)
        self.txt_input.focus()
        # self.txt_terminal.insert(tk.END, "PID not found or not a number : {}".format(txtcmd))
        return txtcmd
        # pos = self.txt_terminal.index('end-1c linestart')
        # pos = float(pos)
        # line = self.txt_terminal.get(pos, tk.END)
        # print('received CMD: '+line.strip()+".")
        # return line.strip()

    def showOldCommand(self, event = None):
        if event.keysym == 'Up':
            StaticVar.INDEX_LIST_COMMAND_OLD = StaticVar.INDEX_LIST_COMMAND_OLD - 1
        if event.keysym == 'Down':
            StaticVar.INDEX_LIST_COMMAND_OLD = StaticVar.INDEX_LIST_COMMAND_OLD + 1
            
        if StaticVar.INDEX_LIST_COMMAND_OLD < 0:
            StaticVar.INDEX_LIST_COMMAND_OLD = 0
        if StaticVar.INDEX_LIST_COMMAND_OLD >= len(StaticVar.LIST_COMMAND_OLD):
            StaticVar.INDEX_LIST_COMMAND_OLD = len(StaticVar.LIST_COMMAND_OLD) -1
        
        if StaticVar.COMMAND_OLD_FLAG == True and event.keysym == 'Up':
            print("List old command:")
            print(StaticVar.LIST_COMMAND_OLD)
            txtcmd = self.txt_input.get().strip()
            if len(txtcmd):
                StaticVar.LIST_COMMAND_OLD.append(txtcmd)
            StaticVar.COMMAND_OLD_FLAG = False
            
        cmd = StaticVar.LIST_COMMAND_OLD[StaticVar.INDEX_LIST_COMMAND_OLD]
        self.txt_input.delete(0, tk.END)
        self.txt_input.insert(tk.END, cmd)
        self.txt_input.focus()
        
root = tk.Tk()
app = Application(master=root)
app.master.title(CSys.APP_NAME)
app.master.minsize(750, 500)
app.mainloop()

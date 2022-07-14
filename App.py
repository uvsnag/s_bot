from this import d
import tkinter as tk
from tkinter import scrolledtext


from conf.config import *
from main_module.ultils.fileUltils import *
from main_module.ultils.common import *
from main_module.cmd_mapper.cmd_define import *
from common.static_value import *
from common.constants import *

#TODO import all in folder
# from modules.google_search.main import *

botRes = Message.getBotResMessage()
data = Message.getDataMessage()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.txt_terminal = scrolledtext.ScrolledText(height=25, width=85)
        self.txt_terminal.bind(CKey.KEY_EXC, self.on_execute)
        self.txt_terminal.pack()
        self.txt_terminal.place(x=30, y=40)
        printMessage(self, botRes[CSys.APP_FIRST_MESSAGE])
        
    def on_execute(self, event = None):
        cusResq = self.getLastRow()
        key = deterCommand(cusResq, data)
        if not key or key == '':
            printMessage(self, botRes[CommandConstants.CMD_NOT_FOUND])
        else:
            if key == CommandConstants.NEXT_RESULT:
                StaticVar.CURRENT_INDEX_ARRLINK = StaticVar.CURRENT_INDEX_ARRLINK + 1
                if StaticVar.CURRENT_KEY == "":
                    return 
                process(self, StaticVar.CURRENT_KEY, StaticVar.CURRENT_SEARCH_STR)
            else:
                StaticVar.CURRENT_INDEX_ARRLINK = 0
                StaticVar.CURRENT_SEARCH_STR = ''
                StaticVar.CURRENT_KEY = key
                process(self, key, cusResq)
        
    # txt_terminal
    def getLastRow(self):
        pos = self.txt_terminal.index('end-1c linestart')
        pos = float(pos)
        line = self.txt_terminal.get(pos, tk.END)
        print('received CMD: '+line.strip()+".")
        return line.strip()

root = tk.Tk()
app = Application(master=root)
app.master.title(CSys.APP_NAME)
app.master.minsize(750, 500)
app.mainloop()

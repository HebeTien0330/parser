'''
:@Author: tangchengqin
:@Date: 2024/5/16 15:10:17
:@LastEditors: tangchengqin
:@LastEditTime: 2024/5/18 14:17:06
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
import os
import datetime

class Logger:

    __isinstance = None

    def __init__(self, path):
        self.path = path
        self.init()

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:
            return cls.__isinstance
        cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

    def init(self):
        print(self.path, os.path.exists(self.path))
        if os.path.exists(self.path):
            return
        os.makedirs(self.path)

    def logfile(self, src, text):
        logout = f"[{datetime.datetime.now()}]: {text}\n"
        with open(f"{self.path}/{src}.log", 'a') as file:
            print(logout, end="")
            file.write(logout)


def initLogger(logPath):
    if "g_Logger" not in globals():
        global g_Logger
        g_Logger = Logger(logPath)

def getLogger():
    return g_Logger

def logfile(src, text):
    g_Logger = getLogger()
    g_Logger.logfile(src, text)

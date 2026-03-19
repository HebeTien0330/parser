from utils.logger import logfile, LogLevel
from utils.box import Box
from core.config import ConfigManager
from core.parser import Parser
from importlib import import_module
import json
import shutil
import os

class ParserTemplate(Parser):

    def __init__(self):
        Parser.__init__(self)
        self.clearExistFiles()

    def doParse(self):
        self.tidy()
        clazzPath = Box.get(ConfigManager).get("Clazz")
        if not clazzPath:
            logfile(LogLevel.ERROR, "no clazz path")
            return
        writerList = os.listdir(clazzPath)
        for fileName in writerList:
            if fileName == "__init__.py" or fileName[-3:] != ".py":
                continue            
            target = import_module(f"project.clazz.{fileName[:-3]}")
            if not target:
                logfile(LogLevel.ERROR, "error writer file path")
                continue
            if not hasattr(target, "Writer"):
                logfile(LogLevel.ERROR, f"file {fileName} no writer")
                continue
            Writer = getattr(target, "Writer")
            Writer().write()

    def tidy(self):
        path = Box.get(ConfigManager).get("MiddleFile")
        for fileName in os.listdir(path):
            if fileName[-5:] != ".json":
                continue
            with open(path + "\\" + fileName, "r", encoding="utf-8") as file1:
                jsonObj = json.loads(file1.read())
                jsonObj = sorted(jsonObj.items(), key = lambda x:int(x[0]) if isinstance(x[0], int) else x[0])
                jsonObj = dict(jsonObj)
                with open(path + "\\" + fileName, "w", encoding="utf-8") as file2:
                    file2.write(json.dumps(jsonObj, indent=4, ensure_ascii=False))

    def clearExistFiles(self):
        path = Box.get(ConfigManager).get("MiddleFile")
        shutil.rmtree(path)
        os.mkdir(path)

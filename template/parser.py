import sys
sys.path.append("../")
from tools import Parser, logfile
from importlib import import_module
import os
import shutil
import json

class ParserTemplate(Parser):

    def __init__(self):
        Parser.__init__(self)
        self.clearExistFiles()

    def doParser(self):
        self.tidy()
        # your parser script
        writerList = os.listdir(".\\clazz")
        for fileName in writerList:
            if fileName == "__init__.py" or fileName[-3:] != ".py":
                continue            
            target = import_module(f"project.clazz.{fileName[:-3]}")
            if not target:
                logfile("parser", "error writer file path")
                continue
            if not hasattr(target, "Writer"):
                logfile("parser", f"file {fileName} no writer")
                continue
            Writer = getattr(target, "Writer")
            Writer(self.conf).write()

    def tidy(self):
        path = ".\\data\middleware"
        for fileName in os.listdir(path):
            if fileName[-5:] != ".json":
                continue
            with open(path + "\\" + fileName, "r", encoding="utf-8") as file1:
                jsonObj = json.loads(file1.read())
                jsonObj = sorted(jsonObj.items(), key = lambda x:int(x[0]))
                jsonObj = dict(jsonObj)
                with open(path + "\\" + fileName, "w", encoding="utf-8") as file2:
                    file2.write(json.dumps(jsonObj, indent=4, ensure_ascii=False))

    def clearExistFiles(self):
        path = ".\\data\middleware"
        shutil.rmtree(path)
        os.mkdir(path)


if __name__ == "__main__":
    parser = ParserTemplate()
    parser.parser()

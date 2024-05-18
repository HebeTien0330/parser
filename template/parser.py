import sys
sys.path.append("../")
from tools import Parser, logfile
from importlib import import_module
import os

class ParserTemplate(Parser):

    def __init__(self):
        Parser.__init__(self)

    def doParser(self):
        # your parser script
        writerList = os.listdir(".\\clazz")
        for fileName in writerList:
            if fileName == "__init__.py" or fileName[-3:] != ".py":
                continue            
            target = import_module(f"example.clazz.{fileName[:-3]}")
            if not target:
                logfile("error writer file path")
                return
            if not hasattr(target, "Writer"):
                logfile(f"file {fileName} no writer")
                return
            Writer = getattr(target, "Writer")
            Writer(self.conf).write()

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
            target = import_module(f"project.clazz.{fileName[:-3]}")
            if not target:
                logfile("parser", "error writer file path")
                return
            if not hasattr(target, "Writer"):
                logfile("parser", f"file {fileName} no writer")
                return
            Writer = getattr(target, "Writer")
            Writer(self.conf).write()


if __name__ == "__main__":
    parser = ParserTemplate()
    parser.parser()

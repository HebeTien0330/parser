import sys
import os
import shutil

class ParserTool:

    def __init__(self, path, name):
        self.path = path
        self.name = name

    def build(self):
        targetDir = f"{self.path}\\{self.name}"
        if os.path.isdir(targetDir):
            raise "target path already exist!"
        os.mkdir(targetDir)
        open(f"{targetDir}\\__init__.py", "w", encoding="utf-8").close()
        shutil.copy(".\\template\\config.json", f"{targetDir}\\config.json")
        shutil.copy(".\\template\\parser.py", f"{targetDir}\\{self.name}Parser.py")
        os.mkdir(f"{targetDir}\\data")
        os.mkdir(f"{targetDir}\\data\\excel")
        os.mkdir(f"{targetDir}\\data\\middleward")
        os.mkdir(f"{targetDir}\\data\\resource")
        os.mkdir(f"{targetDir}\\clazz")
        shutil.copy(".\\template\\writer.py", f"{targetDir}\\clazz\\{self.name}Writer.py")


if __name__ == "__main__":
    path = "./"
    name = "dafault"
    if sys.argv:
        path, name = sys.argv[1], sys.argv[2]
    ParserTool(path, name).build()

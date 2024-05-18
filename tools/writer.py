'''
:@Author: tangchengqin
:@Date: 2024/5/18 11:10:33
:@LastEditors: tangchengqin
:@LastEditTime: 2024/5/18 15:53:37
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
import os
import json

"""
目标文件生成器
由中间文件生成目标文件
可以生成json文件或任意语言的脚本，具体看使用者的配置
使用者可以继承该类，通过重载doWrite方法实现具体生成逻辑
"""
class BaseWriter:
    
    def __init__(self, conf):
        self.conf = conf
        self.createOutputDir()
        self.fileName = None

    def createOutputDir(self):
        dirPath = self.conf["basePath"] + self.conf["output"]
        if not os.path.isdir(dirPath):
            os.mkdir(dirPath)

    def getOutputName(self):
        return self.conf["basePath"] + self.conf["output"] + f"\\{self.fileName}.json"

    def write(self):
        middleWareDir = self.conf["basePath"] + self.conf["middleWare"]
        filePath = f"{middleWareDir}\\{self.fileName}.json"
        with open(filePath, "r", encoding="utf-8") as file:
            jsonObj = json.loads(file.read())
            self.doWrite(jsonObj)

    def doWrite(self, jsonObj):
        raise Exception("doWrite is waiting to be overrided")

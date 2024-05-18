'''
:@Author: tangchengqin
:@Date: 2024/5/15 11:57:02
:@LastEditors: tangchengqin
:@LastEditTime: 2024/5/18 14:56:44
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''

from .reader import ExcelReader
from .middleWriter import middlewareWriter
import json

"""
解析器
负责调用读取器、生成器，并负责分配目标文件的提交、分发
"""
class Parser:

    def __init__(self):
        self.conf = self.loadConf()

    def loadConf(self):
        with open("./config.json") as file:
            conf = json.loads(file.read())
            return conf

    def parser(self):
        middleWriter = middlewareWriter(self.conf)
        for fileName, workBook in ExcelReader(self.conf):
            middleWriter.bindWorkBook(workBook)
            middleWriter.writeMiddleware()
        self.doParser()

    # 具体实现重载该方法
    def doParser(self):
        pass

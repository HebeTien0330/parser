'''
:@Author: tangchengqin
:@Date: 2024/5/15 11:53:30
:@LastEditors: tangchengqin
:@LastEditTime: 2024/5/16 16:34:25
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
from .logger import initLogger
import xlrd
import os

"""
Excel读取器
用于读取config设置的路径下的Excel文件
生成workbook对象，并以迭代器的方式返回
"""
class ExcelReader:

    def __init__(self, conf):
        self.conf = conf
        self.fileList = self.loadExcel()
        self._pointer = 0
        initLogger(self.conf["basePath"] + self.conf["log"])

    def __iter__(self):
        while self._pointer < len(self.fileList):
            fileName = self.fileList[self._pointer]
            filePath = f"{self.conf['basePath']}{self.conf['excelPath']}\\{fileName}"
            workBook = xlrd.open_workbook(filePath)
            yield fileName, workBook
            self._pointer += 1

    def loadExcel(self):
        excelPath = self.conf["basePath"] + self.conf["excelPath"]
        fileList = os.listdir(excelPath)
        return fileList

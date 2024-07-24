'''
:@Author: tangchengqin
:@Date: 2024/5/15 11:53:00
:@LastEditors: tangchengqin
:@LastEditTime: 2024/7/24 11:16:47
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
from .logger import logfile
from copy import deepcopy
import re
import json
import os

"""
中间件生成器
生成Excel文件 -> json文件/脚本 的中间文件
格式为json
"""
class MiddlewareWriter:

    def __init__(self, conf):
        self.conf = conf
        self.workBook = None

    # 绑定要操作的workBook
    def bindWorkBook(self, workBook, fileName):
        self.workBook = workBook
        self.fileName = fileName

    # 写入中间件
    def writeMiddleware(self):
        sheetNames = self.workBook.sheet_names()
        for sheetName in sheetNames:
            names = sheetName.split("|")
            if len(names) != 2:
                logfile("middleware", f"incorrect sheet name {sheetName} in {self.fileName}")
                continue
            logfile("middleware", f"parsering {sheetName} in {self.fileName}")
            sheet = self.workBook.sheet_by_name(sheetName)
            name = names[0]
            jsonObj = self.tarnslate2Json(sheet)
            if not jsonObj:
                continue
            dirPath = self.conf["basePath"] + self.conf["middleWare"]
            if os.path.exists(f"{dirPath}\\{name}.json"):
                existFile = open(f"{dirPath}\\{name}.json", "r", encoding="utf-8")
                existObj = json.load(existFile)
                jsonObj = eval(jsonObj)
                jsonObj = json.dumps({**existObj, **jsonObj}, indent=4, ensure_ascii=False)
                existFile.close()
            with open(f"{dirPath}\\{name}.json", "w", encoding="utf-8") as file:
                file.write(f"{jsonObj}")

    def tarnslate2Json(self, sheet):
        self.keys = sheet.row_values(1)
        self.types = sheet.row_values(2)
        stack = self.recursionGenStructure(deepcopy(self.keys))
        final = {}
        for row in range(sheet.nrows):
            if row in [0, 1, 2]:        # 跳过前三行
                continue
            values = sheet.row_values(row)
            if not values[0] or values[0] == "否":       # 过滤掉export为否的行
                continue
            dataMap = dict(zip(self.keys, values))
            jsonObj = self.fillWithData(deepcopy(stack), dataMap)
            final = self.merge(final, jsonObj)
        return json.dumps(final, indent=4, ensure_ascii=False)
            

    def recursionGenStructure(self, keys, stack = None):      # 递归生成数据结构
        if not len(keys):
            return stack
        if not stack:
            stack = []        # 数据结构栈
        key = keys.pop(0)
        if key == "export":
            return self.recursionGenStructure(keys, stack)
        reObj = re.match("^#+", key)
        if not reObj:
            keys.insert(0, key)
            stack.append(keys)
            return self.recursionGenStructure([], stack)
        stack.append(key)
        return self.recursionGenStructure(keys, stack)

    def getType(self, key):
        idx = self.keys.index(key)
        return self.types[idx]

    def fillWithData(self, stack, dataMap):
        ret = {}
        while stack:
            e = stack.pop()
            if type(e) == list:
                for key in e:
                    value = dataMap[key]
                    keyType = self.getType(key)
                    if key == "" or value == "":
                        continue
                    elif keyType == "int":
                        data = int(value)
                    elif keyType == "float":
                        data = float(value)
                    elif keyType == "str":
                        data = str(value)
                    else:
                        try:
                            data = eval(int(value))
                        except:
                            try:
                                data = eval(str(value))
                            except:
                                data = str(value)
                    ret[key] = data
            else:
                try:
                    ret = { int(dataMap[e]): ret }
                except:
                    ret = { str(dataMap[e]): ret }
        return ret

    def merge(self, final, jsonObj):
        for key, value in jsonObj.items():
            if key not in final:
                final[key] = value
                continue
            final[key] = self.merge(final[key], value)
        return final

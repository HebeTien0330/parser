'''
:@Author: tangchengqin
:@Date: 2024/5/18 14:57:31
:@LastEditors: tangchengqin
:@LastEditTime: 2024/5/18 14:57:31
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
from tools import BaseWriter
import json

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "const"

    def doWrite(self, jsonObj):
        outputPath = self.getOutputName()
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            output = {}
            for key, values in jsonObj.items():
                output[key] = values["value"]
            output = json.dumps(output, indent=4)
            outputFile.write(output)

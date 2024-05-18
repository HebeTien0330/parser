'''
:@Author: tangchengqin
:@Date: 2024/5/18 16:28:09
:@LastEditors: tangchengqin
:@LastEditTime: 2024/5/18 16:29:45
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
from tools import BaseWriter
import json

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "test"

    def doWrite(self, jsonObj):
        outputPath = self.getOutputName()
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            output = json.dumps(jsonObj, indent=4)
            outputFile.write(output)

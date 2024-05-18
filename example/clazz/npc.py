'''
:@Author: tangchengqin
:@Date: 2024/5/18 16:09:10
:@LastEditors: tangchengqin
:@LastEditTime: 2024/5/18 16:27:52
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
from tools import BaseWriter

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "npc"
    
    def getOutputName(self):
        return self.conf["basePath"] + self.conf["output"] + f"\\{self.fileName}.ts"

    def doWrite(self, jsonObj):
        output = self.getOutputName()
        script = ""
        with open(output, "w", encoding="utf-8") as outputFile:
            for npcId, info in jsonObj.items():
                script += self.createTypeScript(npcId, info)
            outputFile.write(script)
        
    def createTypeScript(self, npcId, info):
        return """
export class Npc%s {

    data: any;

    constructor() {
        this.data = {
            name: "%s",
            gender: %d,
            birthday: "%s",
            resourece: "%s",
        }
    }

    init() {
        // NOTE: do somethine when init
    }

    afterInit() {
        // NOTE: callback after init
    }

    action() {
        //NOTE: action of npc
    }

}

""" % (npcId, info["name"], info["gender"], info['birthday'], info["resource"])

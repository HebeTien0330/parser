from tools import BaseWriter

class WriterTemplete(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "const"

    def doWrite(self, jsonObj, outputPath):
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            # your writer script
            pass

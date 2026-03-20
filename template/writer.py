from core.writer import BaseWriter

class WriterTemplete(BaseWriter):

    def __init__(self):
        BaseWriter.__init__(self)
        self.filename = "const"

    def doWrite(self, jsonObj, outputPath):
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            # your writer script
            pass

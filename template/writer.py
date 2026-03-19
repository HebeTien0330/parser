from core.writer import BaseWriter
from core.config import ConfigManager
from utils.box import Box

class WriterTemplete(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "const"

    def doWrite(self, jsonObj):
        outputPath = Box.get(ConfigManager).get("Output")
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            # your writer script
            pass

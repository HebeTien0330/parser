from tools import BaseWriter

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "item"

    def doWrite(self, jsonObj):
        outputPath = self.getOutputName()
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            baseTarget = """
package tables

type Item struct {
    Id int
    Name string
    Desc string
    Icon string
    Bag int
    Class int
    Quality int   
}

"""
            outputFile.write(baseTarget)
            for id, info in jsonObj.items():
                id = int(id)
                name = info["name"]
                desc = info["desc"]
                icon = info["icon"]
                bag = info["bag"]
                class_ = info["class"]
                quality = info["quality"]
                target = """
type Item_%d struct {
    Item
}

func (slf *Item_%d) OnInit() {
    slf.Id = %d
    slf.Name = "%s"
    slf.Desc = "%s"
    slf.Icon = "%s"
    slf.Bag = %d
    slf.Class = %d
    slf.Quality = %d
}

""" % (id, id, id, name, desc, icon, bag, class_, quality)
                outputFile.write(target)

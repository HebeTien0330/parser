from tools import BaseWriter

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "bag"

    def doWrite(self, jsonObj):
        outputPath = self.getOutputName()
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            baseTarget = """
package tables

type BagConfig struct {
    Id int
    Name string
    Desc string
    Initial int
    Extend int
    Cost []int
}

// ======================================================================

type BagIns interface {
    GetConfig() BagConfig
}

// 用于创建BagIns实例
type BagFactory func() BagIns

// 存储BagIns的创建函数
var bagMap = map[int]BagFactory{}

// 用于注册BagIns的创建函数
func RegisterBag(id int, factory BagFactory) {
	bagMap[id] = factory
}

// 根据ID创建BagIns实例      
func NewBag(id int) BagIns {
	if factory, ok := bagMap[id]; ok {
		return factory()
	}
	return nil
}

// ======================================================================
"""
            outputFile.write(baseTarget)
            defineTarget = ""
            target = ""
            for idx, info in jsonObj.items():
                idx = int(idx)
                name = info.get("name", "")
                desc = info.get("desc", "")
                initial = info.get("initial", 0)
                extend = info.get("extend", 0)
                cost = info.get("cost", [])
                defineTarget += """
type Bag_%d struct { BagConfig }

func (slf *Bag_%d) GetConfig() BagConfig {
    return slf.BagConfig
}
""" % (idx, idx)

                target += """
    RegisterBag(%d, func() BagIns {
        return &Bag_%d{
            BagConfig: BagConfig {
                Id: %d,
                Name: "%s",
                Desc: "%s",
                Initial: %d,
                Extend: %d,
                Cost: []int{%d, %d},
            },
        }
    })
""" % (idx, idx, idx, name, desc, initial, extend, cost[0], cost[1])
            
            outputFile.write(defineTarget)
            outputFile.write("""
func init() {\t%s}
""" % target)

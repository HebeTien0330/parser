from tools import BaseWriter

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "hero"

    def doWrite(self, jsonObj, outputPath):
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            baseTarget = """
package tables

type HeroConfig struct {
    Id int
    Name string
    Desc string
    Atk int
    Def int
    HpMax int
    Spd int
}

// ======================================================================

type HeroIns interface {
    GetConfig() HeroConfig
}

// 用于创建HeroIns实例
type HeroFactory func() HeroIns

// 存储HeroIns的创建函数
var heroMap = map[int]HeroFactory{}

// 用于注册HeroIns的创建函数
func RegisterHero(id int, factory HeroFactory) {
	heroMap[id] = factory
}

// 根据ID创建HeroIns实例      
func NewHero(id int) HeroIns {
	if factory, ok := heroMap[id]; ok {
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
                atk = info.get("atk", 0)
                defe = info.get("def", 0)
                hpMax = info.get("hpMax", 0)
                spd = info.get("spd", 0)
                defineTarget += """
type Hero_%d struct { HeroConfig }

func (slf *Hero_%d) GetConfig() HeroConfig {
    return slf.HeroConfig
}
""" % (idx, idx)

                target += """
    RegisterHero(%d, func() HeroIns {
        return &Hero_%d{
            HeroConfig: HeroConfig {
                Id: %d,
                Name: "%s",
                Desc: "%s",
                Atk: %d,
                Def: %d,
                HpMax: %d,
                Spd: %d,
            },
        }
    })
""" % (idx, idx, idx, name, desc, atk, defe, hpMax, spd)
            
            outputFile.write(defineTarget)
            outputFile.write("""
func init() {\t%s}
""" % target)

from tools import BaseWriter

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "skill"

    def doWrite(self, jsonObj):
        outputPath = self.getOutputName()
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            baseTarget = """
package tables

type SkillConfig struct {
    Id int
    Name string
    Desc string
    Influence string
    Effect []int
    Stats int
}

// ======================================================================

type SkillIns interface {
    GetConfig() SkillConfig
}

// 用于创建SkillIns实例
type SkillFactory func() SkillIns

// 存储SkillIns的创建函数
var skillMap = map[int]SkillFactory{}

// 用于注册SkillIns的创建函数
func RegisterSkill(id int, factory SkillFactory) {
	skillMap[id] = factory
}

// 根据ID创建SkillIns实例      
func NewSkill(id int) SkillIns {
	if factory, ok := skillMap[id]; ok {
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
                influence = info.get("influence", 0)
                effect = info.get("effect", [])
                stats = info.get("stats", 0)
                defineTarget += """
type Skill_%d struct { SkillConfig }

func (slf *Skill_%d) GetConfig() SkillConfig {
    return slf.SkillConfig
}
""" % (idx, idx)

                target += """
    RegisterSkill(%d, func() SkillIns {
        return &Skill_%d{
            SkillConfig: SkillConfig {
                Id: %d,
                Name: "%s",
                Desc: "%s",
                Influence: "%s",
                Effect: []int{%s},
                Stats: %d,
            },
        }
    })
""" % (idx, idx, idx, name, desc, influence, *tuple(effect), stats)
            
            outputFile.write(defineTarget)
            outputFile.write("""
func init() {\t%s}
""" % target)


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

type Skill_1001 struct { SkillConfig }

func (slf *Skill_1001) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1002 struct { SkillConfig }

func (slf *Skill_1002) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1003 struct { SkillConfig }

func (slf *Skill_1003) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1004 struct { SkillConfig }

func (slf *Skill_1004) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1005 struct { SkillConfig }

func (slf *Skill_1005) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1006 struct { SkillConfig }

func (slf *Skill_1006) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1007 struct { SkillConfig }

func (slf *Skill_1007) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1008 struct { SkillConfig }

func (slf *Skill_1008) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1009 struct { SkillConfig }

func (slf *Skill_1009) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1010 struct { SkillConfig }

func (slf *Skill_1010) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1011 struct { SkillConfig }

func (slf *Skill_1011) GetConfig() SkillConfig {
    return slf.SkillConfig
}

type Skill_1012 struct { SkillConfig }

func (slf *Skill_1012) GetConfig() SkillConfig {
    return slf.SkillConfig
}

func init() {	
    RegisterSkill(1001, func() SkillIns {
        return &Skill_1001{
            SkillConfig: SkillConfig {
                Id: 1001,
                Name: "制空权",
                Desc: "激活后，你将获得短暂的加速，并使周围的敌人陷入迷茫，降低他们的视野，使其难以定位你。",
                Influence: "减少敌人视野范围，增加自身移动速度，持续5秒。",
                Effect: []int{1001},
                Stats: 1,
            },
        }
    })

    RegisterSkill(1002, func() SkillIns {
        return &Skill_1002{
            SkillConfig: SkillConfig {
                Id: 1002,
                Name: "涂料地图",
                Desc: "在地面上标记一个区域，任何踏入此区域的敌人都会受到减速效果和持续伤害，适合控制战场和分割敌方队伍。",
                Influence: "标记一片区域，对进入该区域的敌人造成减速和持续伤害。",
                Effect: []int{1002},
                Stats: 1,
            },
        }
    })

    RegisterSkill(1003, func() SkillIns {
        return &Skill_1003{
            SkillConfig: SkillConfig {
                Id: 1003,
                Name: "隐身",
                Desc: "消失在敌人视线之外，可用于潜行接近目标或逃离危险。使用时需谨慎，任何动作都会暴露位置。",
                Influence: "进入隐身状态，持续10秒，移动或攻击时隐身效果解除。",
                Effect: []int{1003},
                Stats: 2,
            },
        }
    })

    RegisterSkill(1004, func() SkillIns {
        return &Skill_1004{
            SkillConfig: SkillConfig {
                Id: 1004,
                Name: "治愈之泉",
                Desc: "召唤一股治愈之力，为附近的队友提供持续的生命恢复，是团战中不可或缺的支援技能。",
                Influence: "为周围友军恢复生命值，持续治疗5秒。",
                Effect: []int{1004},
                Stats: 2,
            },
        }
    })

    RegisterSkill(1005, func() SkillIns {
        return &Skill_1005{
            SkillConfig: SkillConfig {
                Id: 1005,
                Name: "冰霜新星",
                Desc: "释放一圈冰冷的能量，冻结周围的敌人，使其无法移动，为队友创造进攻或撤退的机会。",
                Influence: "对周围敌人造成伤害并冰冻他们，持续2秒。",
                Effect: []int{1005},
                Stats: 3,
            },
        }
    })

    RegisterSkill(1006, func() SkillIns {
        return &Skill_1006{
            SkillConfig: SkillConfig {
                Id: 1006,
                Name: "魔法护盾",
                Desc: "形成一个魔法屏障，吸收一定量的伤害。当护盾破裂时，会对周围敌人施加反击。",
                Influence: "创建一个吸收伤害的护盾，持续5秒，护盾消失时对周围敌人造成魔法伤害",
                Effect: []int{1006},
                Stats: 3,
            },
        }
    })

    RegisterSkill(1007, func() SkillIns {
        return &Skill_1007{
            SkillConfig: SkillConfig {
                Id: 1007,
                Name: "风暴召唤",
                Desc: "聚集天空中的能量，在目标区域召唤连续的雷电打击，造成大量范围伤害。",
                Influence: "在指定区域召唤雷电风暴，对敌人造成多段伤害。",
                Effect: []int{1007},
                Stats: 4,
            },
        }
    })

    RegisterSkill(1008, func() SkillIns {
        return &Skill_1008{
            SkillConfig: SkillConfig {
                Id: 1008,
                Name: "瞬移",
                Desc: "立即传送至地图上可见的目标点，用于快速支援或逃脱，是战术机动的重要手段。",
                Influence: "瞬间传送到地图上的指定位置。",
                Effect: []int{1008},
                Stats: 4,
            },
        }
    })

    RegisterSkill(1009, func() SkillIns {
        return &Skill_1009{
            SkillConfig: SkillConfig {
                Id: 1009,
                Name: "时间扭曲",
                Desc: "扭曲时空，使敌人陷入缓慢，而你的队友则如风驰电掣般迅速，改变战斗节奏。",
                Influence: "减缓周围敌人的行动速度，同时加快友军的动作速度，持续5秒。",
                Effect: []int{1009},
                Stats: 5,
            },
        }
    })

    RegisterSkill(1010, func() SkillIns {
        return &Skill_1010{
            SkillConfig: SkillConfig {
                Id: 1010,
                Name: "幻影分身",
                Desc: "释放一个与你外观相同的幻影，可以分散敌人的火力，同时在消失时给予敌人意外的伤害。",
                Influence: "创造一个自己的幻影，吸引敌人的注意，持续时间结束或被击破时爆炸造成范围伤害。",
                Effect: []int{1010},
                Stats: 5,
            },
        }
    })

    RegisterSkill(1011, func() SkillIns {
        return &Skill_1011{
            SkillConfig: SkillConfig {
                Id: 1011,
                Name: "能量汲取",
                Desc: "直接从敌人身上抽取生命力，不仅削弱对手，还能增强自己，是生存和战斗的双重保障。",
                Influence: "吸收敌人的能量，转化为自身生命值或能量值，持续3秒。",
                Effect: []int{1011},
                Stats: 5,
            },
        }
    })

    RegisterSkill(1012, func() SkillIns {
        return &Skill_1012{
            SkillConfig: SkillConfig {
                Id: 1012,
                Name: "黑暗领域",
                Desc: "创建一个黑暗区域，降低敌人命中率，同时提高区域内友军的闪避率，持续10秒。",
                Influence: "在战场上铺开一片黑暗，使敌人射击变得困难，而你的队伍则更加灵活难捉。",
                Effect: []int{1012},
                Stats: 5,
            },
        }
    })
}

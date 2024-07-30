
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

type Hero_600001 struct { HeroConfig }

func (slf *Hero_600001) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600002 struct { HeroConfig }

func (slf *Hero_600002) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600003 struct { HeroConfig }

func (slf *Hero_600003) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600004 struct { HeroConfig }

func (slf *Hero_600004) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600005 struct { HeroConfig }

func (slf *Hero_600005) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600006 struct { HeroConfig }

func (slf *Hero_600006) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600007 struct { HeroConfig }

func (slf *Hero_600007) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600008 struct { HeroConfig }

func (slf *Hero_600008) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600009 struct { HeroConfig }

func (slf *Hero_600009) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600010 struct { HeroConfig }

func (slf *Hero_600010) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600011 struct { HeroConfig }

func (slf *Hero_600011) GetConfig() HeroConfig {
    return slf.HeroConfig
}

type Hero_600012 struct { HeroConfig }

func (slf *Hero_600012) GetConfig() HeroConfig {
    return slf.HeroConfig
}

func init() {	
    RegisterHero(600001, func() HeroIns {
        return &Hero_600001{
            HeroConfig: HeroConfig {
                Id: 600001,
                Name: "狌",
                Desc: "兽类，形状像猿猴但有白耳朵，据说吃了它的肉可以让人跑得更快。",
                Atk: 300,
                Def: 300,
                HpMax: 3000,
                Spd: 10,
            },
        }
    })

    RegisterHero(600002, func() HeroIns {
        return &Hero_600002{
            HeroConfig: HeroConfig {
                Id: 600002,
                Name: "鹿蜀",
                Desc: "形状像马，有白色的头，身上的花纹像老虎，尾巴是红色的，叫声像唱歌，佩戴它的皮毛可以带来子孙繁衍。",
                Atk: 300,
                Def: 300,
                HpMax: 3000,
                Spd: 10,
            },
        }
    })

    RegisterHero(600003, func() HeroIns {
        return &Hero_600003{
            HeroConfig: HeroConfig {
                Id: 600003,
                Name: "旋龟",
                Desc: "形状像乌龟但有鸟的头。",
                Atk: 400,
                Def: 400,
                HpMax: 4000,
                Spd: 20,
            },
        }
    })

    RegisterHero(600004, func() HeroIns {
        return &Hero_600004{
            HeroConfig: HeroConfig {
                Id: 600004,
                Name: "钦丕",
                Desc: "鸟类，能变成大鹗，有黑色的羽毛和红色的喙，脚像虎爪，叫声像晨鹄，出现预示战争。",
                Atk: 400,
                Def: 400,
                HpMax: 4000,
                Spd: 20,
            },
        }
    })

    RegisterHero(600005, func() HeroIns {
        return &Hero_600005{
            HeroConfig: HeroConfig {
                Id: 600005,
                Name: "文鳐鱼",
                Desc: "鱼类，形状像鲤鱼，有鸟的翅膀，身体呈青色。",
                Atk: 500,
                Def: 500,
                HpMax: 5000,
                Spd: 30,
            },
        }
    })

    RegisterHero(600006, func() HeroIns {
        return &Hero_600006{
            HeroConfig: HeroConfig {
                Id: 600006,
                Name: "九尾狐",
                Desc: "拥有九条尾巴的狐狸，能够变化成人形。",
                Atk: 500,
                Def: 500,
                HpMax: 5000,
                Spd: 30,
            },
        }
    })

    RegisterHero(600007, func() HeroIns {
        return &Hero_600007{
            HeroConfig: HeroConfig {
                Id: 600007,
                Name: "穷奇",
                Desc: "形状像虎，长有一对翅膀，喜欢吃人。",
                Atk: 600,
                Def: 600,
                HpMax: 6000,
                Spd: 40,
            },
        }
    })

    RegisterHero(600008, func() HeroIns {
        return &Hero_600008{
            HeroConfig: HeroConfig {
                Id: 600008,
                Name: "梼杌",
                Desc: "传说中的四大凶兽之一，样子像熊，非常凶残。",
                Atk: 600,
                Def: 600,
                HpMax: 6000,
                Spd: 40,
            },
        }
    })

    RegisterHero(600009, func() HeroIns {
        return &Hero_600009{
            HeroConfig: HeroConfig {
                Id: 600009,
                Name: "混沌",
                Desc: "没有七窍的怪物，后来被开窍而死。",
                Atk: 700,
                Def: 700,
                HpMax: 7000,
                Spd: 50,
            },
        }
    })

    RegisterHero(600010, func() HeroIns {
        return &Hero_600010{
            HeroConfig: HeroConfig {
                Id: 600010,
                Name: "烛龙",
                Desc: "能够控制日夜更替的神兽，眼睛像火炬一样明亮。",
                Atk: 700,
                Def: 700,
                HpMax: 7000,
                Spd: 50,
            },
        }
    })

    RegisterHero(600011, func() HeroIns {
        return &Hero_600011{
            HeroConfig: HeroConfig {
                Id: 600011,
                Name: "相柳",
                Desc: "有九个头的蛇，被禹王所杀",
                Atk: 800,
                Def: 800,
                HpMax: 8000,
                Spd: 60,
            },
        }
    })

    RegisterHero(600012, func() HeroIns {
        return &Hero_600012{
            HeroConfig: HeroConfig {
                Id: 600012,
                Name: "精卫",
                Desc: "原是炎帝的女儿，死后化为鸟，不断填海。",
                Atk: 800,
                Def: 800,
                HpMax: 8000,
                Spd: 60,
            },
        }
    })
}

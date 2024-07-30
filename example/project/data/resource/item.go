
package tables

type ItemConfig struct {
    Id int
    Name string
    Desc string
    Icon string
    Bag int
    Class int
    Quality int
    MaxStack int
}

// 道具获得回调
func (slf *ItemConfig) OnAcquire (player interface{}, count int){

}

// 道具使用回调
func (slf *ItemConfig) OnUse (player interface{}, count int){

}

// 道具消耗回调
func (slf *ItemConfig) OnConsume (player interface{}, count int){

}

// ======================================================================

type ItemIns interface {
    GetConfig() ItemConfig
    OnAcquire (player interface{}, count int)
    OnUse (player interface{}, count int)
    OnConsume (player interface{}, count int)
}

// 用于创建ItemIns实例
type ItemFactory func() ItemIns

// 存储ItemIns的创建函数
var itemMap = map[int]ItemFactory{}

// 用于注册ItemIns的创建函数
func RegisterItem(id int, factory ItemFactory) {
	itemMap[id] = factory
}

// 根据ID创建ItemIns实例      
func NewItem(id int) ItemIns {
	if factory, ok := itemMap[id]; ok {
		return factory()
	}
	return nil
}

// ======================================================================

type Item_600001 struct { ItemConfig }

func (slf *Item_600001) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600002 struct { ItemConfig }

func (slf *Item_600002) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600003 struct { ItemConfig }

func (slf *Item_600003) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600004 struct { ItemConfig }

func (slf *Item_600004) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600005 struct { ItemConfig }

func (slf *Item_600005) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600006 struct { ItemConfig }

func (slf *Item_600006) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600007 struct { ItemConfig }

func (slf *Item_600007) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600008 struct { ItemConfig }

func (slf *Item_600008) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600009 struct { ItemConfig }

func (slf *Item_600009) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600010 struct { ItemConfig }

func (slf *Item_600010) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600011 struct { ItemConfig }

func (slf *Item_600011) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_600012 struct { ItemConfig }

func (slf *Item_600012) GetConfig() ItemConfig {
    return slf.ItemConfig
}

type Item_1 struct { ItemConfig }

func (slf *Item_1) GetConfig() ItemConfig {
    return slf.ItemConfig
}

// 道具使用回调
func (slf *Item_1) OnUse (player interface{}, count int) {
    println("ItemIns_1 count OnUse Callback")
}

type Item_2 struct { ItemConfig }

func (slf *Item_2) GetConfig() ItemConfig {
    return slf.ItemConfig
}

func init() {	
    RegisterItem(600001, func() ItemIns {
        return &Item_600001{
            ItemConfig: ItemConfig {
                Id: 600001,
                Name: "狌",
                Desc: "兽类，形状像猿猴但有白耳朵，据说吃了它的肉可以让人跑得更快。",
                Icon: "Hero_600001.png",
                Bag: 3,
                Class: 9,
                Quality: 1,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600002, func() ItemIns {
        return &Item_600002{
            ItemConfig: ItemConfig {
                Id: 600002,
                Name: "鹿蜀",
                Desc: "形状像马，有白色的头，身上的花纹像老虎，尾巴是红色的，叫声像唱歌，佩戴它的皮毛可以带来子孙繁衍。",
                Icon: "Hero_600002.png",
                Bag: 3,
                Class: 9,
                Quality: 1,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600003, func() ItemIns {
        return &Item_600003{
            ItemConfig: ItemConfig {
                Id: 600003,
                Name: "旋龟",
                Desc: "形状像乌龟但有鸟的头。",
                Icon: "Hero_600003.png",
                Bag: 3,
                Class: 9,
                Quality: 2,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600004, func() ItemIns {
        return &Item_600004{
            ItemConfig: ItemConfig {
                Id: 600004,
                Name: "钦丕 ",
                Desc: "鸟类，能变成大鹗，有黑色的羽毛和红色的喙，脚像虎爪，叫声像晨鹄，出现预示战争。",
                Icon: "Hero_600004.png",
                Bag: 3,
                Class: 9,
                Quality: 2,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600005, func() ItemIns {
        return &Item_600005{
            ItemConfig: ItemConfig {
                Id: 600005,
                Name: "文鳐鱼",
                Desc: " 鱼类，形状像鲤鱼，有鸟的翅膀，身体呈青色。",
                Icon: "Hero_600005.png",
                Bag: 3,
                Class: 9,
                Quality: 3,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600006, func() ItemIns {
        return &Item_600006{
            ItemConfig: ItemConfig {
                Id: 600006,
                Name: "九尾狐",
                Desc: "拥有九条尾巴的狐狸，能够变化成人形。",
                Icon: "Hero_600006.png",
                Bag: 3,
                Class: 9,
                Quality: 3,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600007, func() ItemIns {
        return &Item_600007{
            ItemConfig: ItemConfig {
                Id: 600007,
                Name: "穷奇",
                Desc: "形状像虎，长有一对翅膀，喜欢吃人。",
                Icon: "Hero_600007.png",
                Bag: 3,
                Class: 9,
                Quality: 4,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600008, func() ItemIns {
        return &Item_600008{
            ItemConfig: ItemConfig {
                Id: 600008,
                Name: "梼杌",
                Desc: " 传说中的四大凶兽之一，样子像熊，非常凶残。",
                Icon: "Hero_600008.png",
                Bag: 3,
                Class: 9,
                Quality: 4,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600009, func() ItemIns {
        return &Item_600009{
            ItemConfig: ItemConfig {
                Id: 600009,
                Name: "混沌",
                Desc: "没有七窍的怪物，后来被开窍而死。",
                Icon: "Hero_600009.png",
                Bag: 3,
                Class: 9,
                Quality: 5,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600010, func() ItemIns {
        return &Item_600010{
            ItemConfig: ItemConfig {
                Id: 600010,
                Name: "烛龙",
                Desc: "能够控制日夜更替的神兽，眼睛像火炬一样明亮。",
                Icon: "Hero_600010.png",
                Bag: 3,
                Class: 9,
                Quality: 5,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600011, func() ItemIns {
        return &Item_600011{
            ItemConfig: ItemConfig {
                Id: 600011,
                Name: "相柳",
                Desc: "有九个头的蛇，被禹王所杀",
                Icon: "Hero_600011.png",
                Bag: 3,
                Class: 9,
                Quality: 6,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(600012, func() ItemIns {
        return &Item_600012{
            ItemConfig: ItemConfig {
                Id: 600012,
                Name: "精卫",
                Desc: "原是炎帝的女儿，死后化为鸟，不断填海。",
                Icon: "Hero_600012.png",
                Bag: 3,
                Class: 9,
                Quality: 6,
                MaxStack: 99,
            },
        }
    })

    RegisterItem(1, func() ItemIns {
        return &Item_1{
            ItemConfig: ItemConfig {
                Id: 1,
                Name: "铜币",
                Desc: "游戏内的基础货币",
                Icon: "coin.png",
                Bag: 1,
                Class: 1,
                Quality: 1,
                MaxStack: -1,
            },
        }
    })

    RegisterItem(2, func() ItemIns {
        return &Item_2{
            ItemConfig: ItemConfig {
                Id: 2,
                Name: "元宝",
                Desc: "游戏内的进阶货币",
                Icon: "diamond.png",
                Bag: 1,
                Class: 2,
                Quality: 1,
                MaxStack: -1,
            },
        }
    })
}


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

type Bag_1 struct { BagConfig }

func (slf *Bag_1) GetConfig() BagConfig {
    return slf.BagConfig
}

type Bag_2 struct { BagConfig }

func (slf *Bag_2) GetConfig() BagConfig {
    return slf.BagConfig
}

type Bag_3 struct { BagConfig }

func (slf *Bag_3) GetConfig() BagConfig {
    return slf.BagConfig
}

func init() {	
    RegisterBag(1, func() BagIns {
        return &Bag_1{
            BagConfig: BagConfig {
                Id: 1,
                Name: "普通背包",
                Desc: "用于存放游戏内普通道具",
                Initial: 300,
                Extend: 100,
                Cost: []int{1, 100000},
            },
        }
    })

    RegisterBag(2, func() BagIns {
        return &Bag_2{
            BagConfig: BagConfig {
                Id: 2,
                Name: "装备背包",
                Desc: "用于存放游戏内装备",
                Initial: 200,
                Extend: 50,
                Cost: []int{2, 500},
            },
        }
    })

    RegisterBag(3, func() BagIns {
        return &Bag_3{
            BagConfig: BagConfig {
                Id: 3,
                Name: "英雄背包",
                Desc: "用于存放游戏内英雄",
                Initial: 200,
                Extend: 50,
                Cost: []int{2, 1000},
            },
        }
    })
}

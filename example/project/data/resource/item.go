
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


type Item_1 struct {
    Item
}

func (slf *Item_1) OnInit() {
    slf.Id = 1
    slf.Name = "铜币"
    slf.Desc = "游戏内的基础货币"
    slf.Icon = "coin.png"
    slf.Bag = 1
    slf.Class = 1
    slf.Quality = 1
}


type Item_2 struct {
    Item
}

func (slf *Item_2) OnInit() {
    slf.Id = 2
    slf.Name = "元宝"
    slf.Desc = "游戏内的进阶货币"
    slf.Icon = "diamond.png"
    slf.Bag = 1
    slf.Class = 2
    slf.Quality = 1
}


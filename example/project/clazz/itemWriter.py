'''
:@Author: tangchengqin
:@Date: 2024/7/25 18:30:16
:@LastEditors: tangchengqin
:@LastEditTime: 2024/7/25 18:30:16
:Description: 
:Copyright: Copyright (©)}) 2024 Clarify. All rights reserved.
'''
from tools import BaseWriter
from plugin.useCallBack import callback as useCallBack

class Writer(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "item"

    def doWrite(self, jsonObj, outputPath):
        define = """
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
"""

        with open(outputPath, "w", encoding="utf-8") as outputFile:
            baseTarget = define
            target = ""
            defineTarget = ""
            outputFile.write(baseTarget)
            for idx, info in jsonObj.items():
                idx = int(idx)
                name = info.get("name", "")
                desc = info.get("desc", "")
                icon = info.get("icon", "")
                bag = info.get("bag", -1)
                class_ = info.get("class", -1)
                quality = info.get("quality", -1)
                maxStack = info.get("maxStack", -1)
                target += """
    RegisterItem(%d, func() ItemIns {
        return &Item_%d{
            ItemConfig: ItemConfig {
                Id: %d,
                Name: "%s",
                Desc: "%s",
                Icon: "%s",
                Bag: %d,
                Class: %d,
                Quality: %d,
                MaxStack: %d,
            },
        }
    })
""" % (idx, idx, idx, name, desc, icon, bag, class_, quality, maxStack)
                # outputFile.write(target)

                defineTarget += """
type Item_%d struct { ItemConfig }

func (slf *Item_%d) GetConfig() ItemConfig {
    return slf.ItemConfig
}
""" % (idx, idx)
                if info.get("onUse"):
                    cid = info.get("onUse")
                    callback = useCallBack.get(cid)
                    if not callback:
                        continue
                    defineTarget += """
// 道具使用回调
func (slf *Item_%d) OnUse (player interface{}, count int) {
    %s
}
""" % (idx, callback(idx))
            
            outputFile.write(defineTarget)
            outputFile.write("""
func init() {\t%s}
""" % target)

# 游戏导表工具
### 简介
    可以将Excel表格解析成json文件或其他你需要的脚本
    版本要求：Python3.8或以上
    安装依赖库：pip install xlrd

### 运行原理
#### 文件目录结构
    ├─example                   项目根目录
    │  ├─clazz                  用户需要具体实现的writer
    │  └─data                   存放输入输出数据的目录
    │      ├─excel              需要解析的Excel表格
    │      ├─log                日志
    │      ├─middleward         生成的中间文件
    │      └─resource           最终输出结果

#### 执行顺序
    1、通过xlrd读取Excel表格，解析每一行数据
    2、根据配置的不同等级键值生成中间json文件，存放在./data/resourece中
    3、根据用户实现的parser和writer生成目标json或脚本

### 使用方法：
    1、执行 python .\parserTool.py param1 param2，其中param1为目标路径，param2为项目名
    例：python .\parserTool.py . test
    在当前目录下生成test项目，其中包含了config、parser和writer的模板
    ├─test
    │  ├─clazz
    │  └─data
    │      ├─excel
    │      ├─middleward
    │      └─resource

    2、根据实际项目填写config参数
```json
{
    "basePath": "xxx",
    "excelPath": "xxx",
    "middleWare": "xxx",
    "output": "xxx",
    "log": "xxx"
}
```

    3、编写clazz中的writer类，每个Excel表格对应一个的类
```python
from tools import BaseWriter
import json

class WriterTemplete(BaseWriter):

    def __init__(self, conf):
        BaseWriter.__init__(self, conf)
        self.fileName = "const"

    def doWrite(self, jsonObj):
        outputPath = self.getOutputName()
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            # your writer script
            pass
```

    4、执行项目根目录的xxxParser.py进行导表，可在config设置中的对应output路径下看到导表结果

### 自定义
    如果需要对不同项目定义不同的输出路径、导表逻辑，自定义template中的模板即可
    具体参考example文件夹

### TODO:
    1、增加导表错误提示，帮助定位问题
    2、对于数据量过大的Excel表格，支持在Excel中分子表
    3、支持中间文件分发到不同服务器进行导表，适用于多项目开发

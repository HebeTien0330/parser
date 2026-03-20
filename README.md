# parser

一个基于 Excel 的配置导出工具。

核心流程：读取 Excel → 生成中间 JSON（`data/middle`）→ 由自定义 Writer 生成目标文件（默认输出到 `data/output`）。

## 功能概览

- 批量读取配置目录下的 Excel 文件
- 将工作表按约定结构转换为 JSON 中间文件
- 支持通过继承 `BaseWriter` 自定义导出逻辑（JSON / 脚本 / 其他格式）
- 提供模板工程一键生成脚本（`build.py`）

## 目录结构

```text
.
├── build.py                # 生成导表模板项目
├── core/                   # 核心流程（读取/中间件/写出）
├── template/               # 模板 parser / writer / config
├── utils/                  # 日志、依赖注入容器
└── data/
    ├── excel/              # 放置待解析 Excel
    ├── middle/             # 中间 JSON
    └── log/                # 日志
```

## 环境要求

- Python 3.9+
- 依赖：
  - `openpyxl`

安装依赖：

```bash
pip install openpyxl
```

## 快速开始

### 1、生成一个模板项目

在仓库根目录执行：

```bash
python build.py
```

默认会在当前目录创建 `test/`，包含：

- `core/`、`utils/`
- `parser.py`
- `clazz/`（放置你的 Writer）
- `config/config.json`
- `data/excel`、`data/middle`、`data/log`

### 2、准备配置

编辑 `config/config.json`（模板默认如下）：

```json
{
  "ExcelPath": "./data/excel/",
  "MiddleFile": "./data/middle/",
  "Output": "./data/output/",
  "Clazz": "./clazz/"
}
```

### 3、放置 Excel 文件

把需要导出的 `.xlsx` 文件放到配置中ExcelPath对应的路径下。

### 4、编写 Writer

在 `clazz/` 下新建一个 Python 文件（例如 `my_writer.py`），并定义 `Writer` 类。

最小示例：

```python
from core.writer import BaseWriter
import json

class Writer(BaseWriter):
    def __init__(self):
        super().__init__()
        self.filename = "const"  # 对应读取 data/middle/const.json

    def doWrite(self, jsonObj, outputPath):
        with open(outputPath, "w", encoding="utf-8") as outputFile:
            outputFile.write(json.dumps(jsonObj, ensure_ascii=False, indent=4))
```

### 5、执行解析

在模板项目根目录运行：

```bash
python parser.py
```

执行后会：

1. 读取 `data/excel/` 下的 Excel
2. 生成中间文件到 `data/middle/`
3. 自动加载 `clazz/` 下每个包含 `Writer` 类的文件并执行导出

## Excel 约定

`MiddleWriter` 对工作表有以下约定：

- 工作表名称格式：`<中间文件名>|<任意后缀>`
  - 示例：`const|server`
  - 生成中间文件：`data/middle/const.json`
- 第 2 行：字段名（key）
- 第 3 行：字段类型（`int` / `float` / `str` / `bool` 等）
- 从第 4 行开始：数据行
- 第 1 列通常为 `export`，当值为空或“否”时该行会被跳过
- 以 `#` 开头的 key 表示层级结构键（用于构建嵌套 JSON）

## 常见问题

- `no clazz path`
  - 检查 `config/config.json` 的 `Clazz` 路径是否存在且正确。

- `ExcelPath is None` 或读不到文件
  - 检查 `ExcelPath` 路径与 Excel 文件是否存在。

- 没有生成输出文件
  - 确认 `clazz/` 下的脚本包含名为 `Writer` 的类。
  - 确认 `Writer.filename` 对应的中间文件名存在（如 `const` → `const.json`）。

## 开发说明

- 容器初始化在 `core/__init__.py` 中完成：`ConfigManager`、`ExcelReader` 会注册到 `Box`。
- 解析主入口在模板 `parser.py`：继承 `core.parser.Parser`，默认实现 `ParserTemplate`。
- 自定义导出请继承 `core.writer.BaseWriter` 并实现 `doWrite`。

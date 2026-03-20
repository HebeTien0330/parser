import shutil
import os

class Builder:

    def __init__(self, path, name):
        self.path = path
        self.name = name

    def build(self):
        targetPath = os.path.join(self.path, self.name)
        if os.path.exists(targetPath):
            raise Exception(f"{targetPath} already exists")
        os.mkdir(targetPath)
        # 复制核心文件和导表模板
        shutil.copytree("./core", os.path.join(targetPath, "core"))
        os.mkdir(os.path.join(targetPath, "data"))
        os.mkdir(os.path.join(targetPath, "data", "excel"))
        os.mkdir(os.path.join(targetPath, "data", "log"))
        os.mkdir(os.path.join(targetPath, "data", "middle"))
        os.mkdir(os.path.join(targetPath, "clazz"))
        shutil.copy("./template/__init__.py", os.path.join(targetPath, "clazz", "__init__.py"))
        shutil.copy("./template/writer.py", os.path.join(targetPath, "clazz", "writer.py"))
        shutil.copy("./template/parser.py", os.path.join(targetPath, "parser.py"))
        shutil.copytree("./template/config", os.path.join(targetPath, "config"))


if __name__ == "__main__":
    builder = Builder("./", "test")
    builder.build()

@echo off
chcp 65001 >nul
echo "开始导表..."
cd project
python -B exampleParser.py
echo "导表完成"
PAUSE

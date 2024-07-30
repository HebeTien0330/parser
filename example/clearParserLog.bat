@echo off
setlocal EnableDelayedExpansion

REM 设置需要清理的目录路径
set "targetDir=%cd%\project\data\log"

REM 检查目录是否存在
if not exist "%targetDir%" (
    echo Directory does not exist.
    exit /b 1
)

REM 显示警告并请求确认
echo WARNING: This will delete all files in directory %targetDir%
echo Press 'Y' to continue, any other key to cancel.
set /p confirm=Confirm (Y/N): 
if /i "%confirm%" NEQ "Y" (
    echo Operation canceled.
    exit /b 0
)

REM 删除目录下的所有文件
for %%f in ("%targetDir%\*") do (
        del /q "%%f"
        echo "delete file %%f"
)

echo All files in %targetDir% have been deleted.
pause
exit /b 0

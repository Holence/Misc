@echo off
chcp 65001
echo.
set /p MD_NAME=markdown文件路径：
echo.
pandoc -s "./%MD_NAME:~0,-3%.md" -o "./%MD_NAME:~0,-3%.epub"
echo.
echo Done
echo.
pause
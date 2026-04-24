@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo 正在安裝套件...
pip install -r requirements.txt pyinstaller
echo 開始打包 Windows 執行檔...
pyinstaller --onefile --distpath "%USERPROFILE%\Desktop" --name WordToPDF_Windows main.py
echo 打包完成！請到 桌面 查看 WordToPDF_Windows.exe
pause

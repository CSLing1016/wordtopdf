#!/bin/bash
cd "$(dirname "$0")"
echo "正在安裝套件..."
pip3 install -r requirements.txt pyinstaller
echo "開始打包 Mac 執行檔..."
pyinstaller --onefile --distpath ~/Desktop --name WordToPDF_Mac main.py
echo "打包完成！請到 桌面 查看 WordToPDF_Mac 執行檔"
echo "處理完成，按 Enter 鍵結束..."
read

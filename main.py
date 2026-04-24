import os
import shutil
import platform
from pathlib import Path
from docx2pdf import convert

def create_folders(base_path):
    """建立必要的資料夾結構"""
    word_dir = base_path / "WORD"
    pdf_dir = base_path / "PDF"
    word_bk_dir = word_dir / "BK"
    pdf_bk_dir = pdf_dir / "BK"
    
    for folder in [word_dir, pdf_dir, word_bk_dir, pdf_bk_dir]:
        folder.mkdir(parents=True, exist_ok=True)
    
    return word_dir, pdf_dir, word_bk_dir, pdf_bk_dir

def convert_word_to_pdf():
    # 取得桌面路徑
    desktop = Path.home() / "Desktop"
    word_dir, pdf_dir, word_bk_dir, pdf_bk_dir = create_folders(desktop)
    
    # 轉 PDF 前先將 PDF 資料夾中的檔案移至 BK
    for pdf_file in pdf_dir.glob("*.pdf"):
        try:
            shutil.move(str(pdf_file), str(pdf_bk_dir / pdf_file.name))
        except Exception as e:
            print(f"移動既有 PDF {pdf_file.name} 到 BK 時出錯: {e}")
            
    print(f"正在掃描資料夾: {word_dir}")
    
    # 遍歷 WORD 資料夾中的 .docx 檔案
    files = [f for f in word_dir.glob("*.docx") if not f.name.startswith("~$")]
    
    if not files:
        print("找不到可轉換的 Word 檔案。")
        return

    for word_file in files:
        try:
            print(f"正在轉換: {word_file.name}...")
            
            # 設定輸出的 PDF 路徑
            pdf_path = pdf_dir / f"{word_file.stem}.pdf"
            
            # 執行轉換 (macOS/Windows 通用)
            convert(str(word_file), str(pdf_path))
            
            # 轉換成功後移動到 BK 資料夾
            shutil.move(str(word_file), str(word_bk_dir / word_file.name))
            print(f"成功！檔案已移至 BK 備份。")
            
        except Exception as e:
            print(f"轉換 {word_file.name} 時出錯: {e}")

if __name__ == "__main__":
    convert_word_to_pdf()
    input("\n處理完成，按 Enter 鍵結束...")
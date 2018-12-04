# tesseract

- 2018/12/04
- Windows 10
- [tesseract-ocr](https://github.com/tesseract-ocr/tesseract)
- [tesseract-ocr CLI](https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage#simplest-invocation-to-ocr-an-image)
- [Tesseract OCR (還沒看)](http://superhbin.pixnet.net/blog/post/28743913-%E3%80%90google%E5%B0%8B%E5%AF%B6%E3%80%9101.tesseract-ocr)

## Install

- tesseract-ocr-setup-3.02.02.exe

## Usage

Original Dir:

    ocr_wording.png

Script:
```powershell
# 最簡單用法: tesseract imagename outputbase
> tesseract ocrwording.png wording
```

Resulting Dir:

    ocr_wording.png
    wording.txt

# Other

- Default Language:                 English
- Default Page Segmentation Mode :  3
- Default Output :                  text

改變語言的話, 則使用 `-l xxx` (三個字的語言切換, ex: `eng`)

多語言則使用 `-l eng+deu` (英文+德文)

但是[語言擴充](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files) 得到這邊下載, 指定英文以外的語言的話, 需要額外指名 `--tessdata-dir /path-to-lang.traineddata`, 例如: `tesseract --tessdata-dir . ocrwording.png -l eng+deu`, 則需要把 `deu.traineddata` 放到目前目錄底下.





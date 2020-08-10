# 發布擴充功能

- 2018/08/01
- [Python Package User Guide](https://packaging.python.org/tutorials/)
- [Python Package Project Structure](https://packaging.python.org/tutorials/packaging-projects/)
- 總之為了底下能夠順利進行, 先執行 `pip install twine setuptools wheel` 就對了




# 零碎關鍵字詞

- Distribution   : 一個打算把它發行出去的 Python 專案
    - 他通常會被封裝成 `xx.whl` 或 `xx.tar.gz`
- pure(純粹)      : 程式碼發行版(Distribution) 完全使用 Python 來寫. 反之則為 nonpure, 底層會依賴 C 實作的腳本 or 其他
- universal(通用) : 當 Distribution 是 pure, 且可適用於 v2 && v3, 若無需 2to3 的轉換, 則此 Distribution 為 universal
- distutils      : (標準函式庫) 用來封裝 && 發布 Python 程式 && 擴充功能, 但不要用它
- setuptools     : (第三方套件) 承上, 使用這個來代替上面那個爛東西.
- sdist          : 
- wheels         : (第三方套件) 先把它理解成跟 setuptools 差不多的東西.
- eggs           : (不要鳥他) 這個是 wheels 的前身
- twine          : (第三方套件) 用來上傳套件到 Python Repository
- setup.py       : 如果要讓 Python 套件發行出去, 需要定義這個東西. 這裡面包含了三個部分:
    - Distribution 的 Metadata
    - 存在於 Distribution 裡頭的其他檔案資訊
    - 依賴性的資訊



# 搭建私有 pypi server

1. 建立空專案 demo_privatepypi, 裡頭建立 packages 資料夾
2. 專案裡頭建立 python 虛擬環境, 並安裝 `pip install pypiserver`
3. 運行 `pypi-server -p 8999 ./packages &`

因為以上建立的 pypi server 不安全, 所以下面啟用驗證

1. `create .htpasswd`
2. `htpasswd -b -m -c .htpasswd myuser mypassword`
3. `pypi-server -p 8999 -P ./.htpasswd ./packages &`

後續要使用的話...

- 會有信任問題 `pip install --extra-index-url http://localhost:8999/ PACKAGE`
- `pip install --extra-index-url http://localhost:8999/ --trusted-host localhost PACKAGE`



# 打包套件

```bash
$# ls
dist/  # 裡面是空的, 等下建置套件時, 就會有東西了
README.rst
setup.py  # 裡面定義了 待發布套件 的 定義 && 建置方式 && 說明
garbage-tools/  # 裏頭就是等下我要開發的套件
    main.py
    __init__.py

### Step1. 在本地建置 wheel 檔
$# python setup.py bdist_wheel

### 上傳套件到 PyPI-Server
$# twine upload -r pypi dist/*
```



# 必要檔案解說

### setup.py

```py
from setuptools import setup, find_packages

with open("README.rst", "r") as ff:
    long_description = ff.read()

setup(
    name="garbage-pytools",  # 可隨意打, 等下建置之後, 套件的名稱
    version="0.1.0",
    author="Tony Chou",
    author_email="cool21540125@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cool21540125/garbage-pytools",  # 定義套件位置
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
```

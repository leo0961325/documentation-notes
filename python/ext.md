


打包套件

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
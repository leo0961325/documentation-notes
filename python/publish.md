# 發布擴充功能

- 2018/08/01

- python standard library 內含 `distutils` (用來封裝 && 發布 python 程式 && 擴充功能)
  - 但別用他!! 請使用 `setuptools` 和 `wheels`


`wheels` 前身為 `eggs`


# 搭建私有 pypi server

1. 建立空專案 demo_privatepypi, 裡頭建立 packages 資料夾
2. 專案裡頭建立 python 虛擬環境, 並安裝 `pip install pypiserver`
3. 運行 `pypi-server -p 8999 ./packages &`

因為以上建立的 pypi server 不安全, 所以下面啟用驗證

1. `create .htpasswd`
2. `htpasswd -b -m -c .htpasswd terrence mypassword`
3. `pypi-server -p 8999 -P ./.htpasswd ./packages &`

後續要使用的話...

- 會有信任問題 `pip install --extra-index-url http://localhost:8999/ PACKAGE`
- `pip install --extra-index-url http://localhost:8999/ --trusted-host localhost PACKAGE`

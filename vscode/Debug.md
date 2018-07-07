# [Debugging](https://code.visualstudio.com/docs/editor/debugging)

- [Debugging Python](https://code.visualstudio.com/docs/python/debugging)
- 2018/07/07
- Windows 10 
- Python 3.6.1 :: Anaconda 4.4.0 (64-bit)
- VSCode 1.24.1



# 變數

- `${workspaceFolder}` : 此專案的 根目錄, 即 `proj/`
- `${file}` : Editor 內要執行的程式碼 的 檔案名稱
- 


# 專案架構

啟用 dubug 之後, 專案目錄底下會多出了 `.vscode/launch.json`
```py
proj/
    .vscode/
        launch.json
        settings.json

    venv/
        etc/
        include/
        Lib/
        Scripts/        # 虛擬環境直譯器在這~

    proj/
        manage.py       # Django 啟動文件

        main_proj/
            __init__.py
            settings.py
            urls.py
            views.py
            wsgi.py
        
        app/
            __init__.py
            admin.py
            apps.py
            models.py
            tests.py
            views.py
```
專案 `Python 虛擬環境` 即為 `"python.pythonPath": "${workspaceFolder}/venv/bin/python"`, 放在 `.vscode/settings.json`



# launch.json

最最基本的組態設定包, 就長得像下面那樣~
```js
{
    "name": "Python: Current File",     // Debug 組態名稱
    "type": "python",                   // Debug 使用的程式語言
    "request": "launch",                // launch 或 attach
    "program": "${file}",               // 執行的目標
    "pythonPath": "${config:python.pythonPath}",    // 虛擬環境直譯器 指向 settings.json
    "args": ["runserver", "--noreload", "--nothreading"],
    "stopOnEntry": true,                // 預設為 false, 若為 true, 執行Debug模式時, 會在程式第一行停下來
    "console": "none",                  // 參考下面 console 設定方式
    "cwd": "",                          // 不好說, 看下面 cwd 說明
    "debugOptions": "",     // 不懂... 略
    "env": "",              // 不懂... 略
    "envFile": "",          // 不懂... 略
}
```


### console 設定方式

value                   | output displayed
----------------------- | -------------------------------------
"none"                  | VS Code debug console
"integratedTerminal"    | (預設) 使用 VS Code 整合式 Terminal
"externalTerminal"      | 分離式的 console window


### args - Debug 時候的額外 參數

ex: `python manage.py runserver --host 0.0.0.0`, 

則設定為 `["runserver", "--host", "0.0.0.0"]` (應該吧! 不確定參數要不要分開)


### cwd 說明

`cwd` 就是 debugger 的 `current working directory`, 也就是 相對於要 debug 的程式碼 的 base folder (乾~ 很不白話)

例如: 專案根目錄 為 `proj/`, 專案架構如下
```
proj/
    py_code/app.py
    data/salaries.csv
```
現在要對 `app.py` 作 debug, salaries.csv 的相對路徑會因為 `cwd` 而有所不同

cwd                             | 相對於 data file 的路徑
------------------------------- | --------------------------
Omitted or ${workspaceFolder}   | data/salaries.csv
${workspaceFolder}/py_code      | ../data/salaries.csv
${workspaceFolder}/data         | salaries.csv


### program 專案啟動文件

```js
// program : 也可以設定專案的啟動文件
"program": "${workspaceFolder}/proj/manage.py"
```


### pythonPath 用來 debug 的 Python 直譯器位置

```js
// 關於 pythonPath, 也可以使用特定的字詞, 來規範不同平台使用的 直譯器
"osx": {    // Mac平台
    "pythonPath": "^\"\\${env:SPARK_HOME}/bin/spark-submit\""
},
"windows": {
    "pythonPath": "^\"\\${env:SPARK_HOME}/bin/spark-submit.cmd\""
},
"linux": {
    "pythonPath": "^\"\\${env:SPARK_HOME}/bin/spark-submit\""
},
// Note: 上面的「\"」, 為 路徑內含有「 」的必要附加設定
// 迷之音: Windows 哪時候有 pyspark了...??
```


### debugOptions

### env

### envFile

可設定 「含有 環境變數 的檔案」 的路徑 (好像是這樣....)



# Remote debugging (有點猛)

可在 host, 執行 沒有安裝 VS Code 的 remote 端的程式

## prerequest
1. 兩部電腦 : make sure that identical source code is available (看不懂..)
2. for Mac & Linux, `pip3 install ptvsd==3.0.0` ; for Windows `pip install ptvsd==3.0.0`
3. Remote : 開放 port 給 debugger 使用
4. Remote : = =...
5. 
6. 
7. 
8. 
9. 
10. 
11. 

乾~~ 我放棄了... 總共有 11個步驟 ㄇㄉ


## Debugging over SSH (to remote)

因為某些特定因素, 可能也得作加密連線, 來作遠端 debug... (內容 pass)


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


# settings.json (專案下的 .vscode/settings.json)
- 2018/07/11

```js
{
    // Windows + anaconda venv 設法 : 直接指向 虛擬環境 Python.exe
    "python.pythonPath": "${workspaceFolder}/venv/bin/python",   // 讓 launch.json 來指向

    // Linux   + anaconda venv 設法 : 指向 Python直譯器位置 && 設定虛擬環境
    "python.pythonPath": "/opt/anaconda3/bin/python",           // 讓 launch.json 來指向
    "python.venvPath": "/opt/anaconda3/envs/drf/",
}
```



# launch.json

最最基本的組態設定包, 就長得像下面那樣~
```js
{
    "name": "Python: Current File",     // Debug 組態名稱
    "type": "python",                   // Debug 使用的程式語言
    "request": "launch",                // launch 或 attach
    "program": "${file}",               // 執行的目標
    "pythonPath": "${config:python.pythonPath}",    // 指向 settings.json 虛擬環境直譯器 
    "args": ["runserver", "--noreload", "--nothreading"],
    "stopOnEntry": true,                // 預設為 false, 若為 true, 執行Debug模式時, 會在程式第一行停下來
    "console": "none",
    "cwd": "",
    "debugOptions": "",
    "env": "",
    "envFile": ""
}
```

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


### args - Debug 時候的額外 參數

ex: `python manage.py runserver --host 0.0.0.0`, 

則設定為 `["runserver", "--host", "0.0.0.0"]` (應該吧! 不確定參數要不要分開)


### console 設定方式

value                   | output displayed
----------------------- | -------------------------------------
"none"                  | VS Code debug console
"integratedTerminal"    | (預設) 使用 VS Code 整合式 Terminal
"externalTerminal"      | 分離式的 console window


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


### debugOptions

可用的選項有 `["RedirectOutput", "DebugStdLib", "Django", "Sudo", "Pyramid", "BreakOnSystemExitZero", "IgnoreDjangoTemplateWarnings"]`

- RedirectOutput : (預設) 讓 Debugger 印出所有 output 到 VS Code debug output window. 若捨略此設定, 所有 程式輸出 將不會出現. 但如果 console 為 `integratedTerminal` 或為 `externalTerminal` 時, 此選可省略.
- DebugStdLib : 會跑進去 StdLibrary 裡頭...(沒必要啦!!)
- Django : 啟用 debugging feature specific 到 Django
- Sudo : 得與 `"console": "externalTerminal"` 搭配使用, 則允許 debugging apps that require elevation
- Pyramid : 
- BreakOnSystemExitZero : (不明)
- IgnoreDjangoTemplateWarnings : (不明)


### env (看不太懂...)

原文 : Sets optional environment variables for the debugger process beyond system environment variables, which the debugger always inherits.


### envFile (看不太懂...)

原文 : Optional path to a file that contains environment variable definitions. See [Configuring Python environments - environment variable definitions file](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file).



# Remote debugging (有點猛)

可在 host, 執行 沒有安裝 VS Code 的 remote 端的程式

## prerequest
1. 兩部電腦 : make sure that identical source code is available (看不懂..)
2. Mac & Linux: `pip3 install ptvsd==3.0.0` ; Windows: `pip install ptvsd==3.0.0`
3. Remote : 開放 port 給 debugger 使用
4. Remote : 遠端電腦放這個
```py
import ptvsd

# Allow other computers to attach to ptvsd at this IP address and port, using the secret
ptvsd.enable_attach("my_secret", address = ('1.2.3.4', 3000))

# Pause the program until a remote debugger is attached
ptvsd.wait_for_attach()
```
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



# WorkSpace Setting

- [Using Pylint with Django](https://stackoverflow.com/questions/115977/using-pylint-with-django/31000713#31000713)
- [Python 的檢查及測試工具箱](https://medium.com/pyladies-taiwan/python-%E7%9A%84%E6%AA%A2%E6%9F%A5%E5%8F%8A%E6%B8%AC%E8%A9%A6%E5%B7%A5%E5%85%B7%E7%AE%B1-eda71af68c19)
- 2018/11/09

```sh
### 安裝 pylint
pip install pylint
# 之後可使用 「pylint file.py」 來測試 file.py 是否符合 PEP8
# 將來可使用 「pylint abc.py」, 來為該檔案進行 PEP8 配適度的評分

### Django 專用的 Pylint
pip install pylint-django
```

```js
// settings.json
{
    // Python - Windows
    "python.pythonPath": "${workspaceFolder}\\venv\\Scripts\\python.exe",

    // Python - Linux - Anaconda
    "python.pythonPath": "/opt/anaconda3/..."

    // Python - Linux - Virtualenvs
    "python.pythonPath": "/home/$USER/.virtualenvs/bin/<ENV>/"

    // Python - pylint
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",     // 讓 VSCode Python-Django 的 linter 正常一點...
        "--disable=missing-docstring",      // docstring
        "--disable=C0103",                  // Argument name snake_case naming style
        "--disable=C0301",                  // Line too Long
    ],
}
```

## for python

```js
{
    // 環境直譯器
    "python.pythonPath": "C:\\Users\\twtru\\OneDrive\\work\\venv\\venv_demo\\Scripts\\python.exe",

    // 自動啟動環境
    "python.terminal.activateEnvironment": true,

    // Linting
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true,
}
```

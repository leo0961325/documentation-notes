
# WorkSpace Setting

- [Using Pylint with Django](https://stackoverflow.com/questions/115977/using-pylint-with-django/31000713#31000713)
- 2018/11/09

```sh
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

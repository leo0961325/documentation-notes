# Debugger - Launch.json

- 2018/08 以前
- v1.24(應該吧)

## Python - file

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

```js
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}"
        }
    ]
}
```


## Python - Django

```js
// launch.json
{
  "version": "0.2.0",
  "configurations": [
    {   // 1. 正常 Run
      "name": "Django-Running",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/bis_emc/manage.py",
      "args": [
        "runserver"
      ],
      "debugOptions": [
        "Django",
      ],
    },
    {   // 2. Debug用
      "name": "Django-Debugging",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/bis_emc/manage.py",
      "args": [
        "runserver",
        "--no-color",
        "--noreload",
        "--nothreading",
      ],
      "console": "none",
      "debugOptions": [
        "Django",
        "BreakOnSystemExitZero",
        // "DebugStdLib",       // Debug Library
        "RedirectOutput",
        "IgnoreDjangoTemplateWarnings",
      ],
    }
  ]
}
```


## Python - Tornado

```js
// launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "tornado",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "pythonPath": "${config:python.pythonPath}"
        },
    ]
}
```


## go

```js
// launch.json
{
    "version": "0.2.0",
    "configurations": [
        {   // debug Current File
            "name": "qoo",
            "type": "go",
            "request": "launch",
            "mode": "debug",
            "program": "${file}",
            "showLog": true
        },
        {   // run web
            "name": "Run Web",
            "type": "go",
            "request": "launch",
            "mode": "debug",
            "port": 9090,
            "host": "127.0.0.1",
            "program": "${workspaceRoot}",
            "env": {},
            "args": [],
            "showLog": true
        }
    ]
}
```
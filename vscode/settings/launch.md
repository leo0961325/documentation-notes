# Debugger - Launch.json

- 2018/08 以前
- v1.24(應該吧)
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)


## Python - Flask

```js
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    // VSCode v1.27.2
    // IMPORTANT: 「DEBUG=False」 才可以真的進入 interactive debug 模式
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver",
                "--debug",
                "--no-reload",
            ],
            "stopOnEntry": false,
            "jinja": true,
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

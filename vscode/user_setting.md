# User settings.json


## User settings.json
```js
{
    // General
    "workbench.startupEditor": "none",
    "editor.minimap.enabled": false,
    "editor.mouseWheelZoom": true,
    "files.autoSave": "onFocusChange",

    // Material Icon Theme 3.5.1
    "workbench.iconTheme": "material-icon-theme",
    "material-icon-theme.showUpdateMessage": false,

    // Power Mode 2.2.0
    "powermode.presets": "flames",
    "powermode.enabled": true,
    "powermode.enableStatusBarComboCounter": false,
    "powermode.enableStatusBarComboTimer": false,

    // Terminal
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",

    // Tab Size
    "editor.tabSize": 2,
    "[markdown]": {
      "editor.tabSize": 4
    },
    "[json]": {
      "editor.tabSize": 4
    }
}
```



# User KeyBindings.json

```js
[
    {   // Toggle Mini Map
        "key": "ctrl+m",
        "command": "editor.action.toggleMinimap"
    },
    {   // IntelliSence
        "key": "ctrl+i",                "command": "editor.action.triggerSuggest",
        "when": "editorHasCompletionItemProvider && textInputFocus && !editorReadonly" 
    },
    {   // Current Line
        "key": "ctrl+l",                "command": "expandLineSelection",
        "when": "textInputFocus" 
    },
]
```



# Django Debugger - Project settings - settings.json

- [Using Pylint with Django](https://stackoverflow.com/questions/115977/using-pylint-with-django/31000713#31000713)

```sh
pip install pylint-django
```

```js
{
    "python.pythonPath": "${workspaceFolder}\\ve\\Scripts\\python.exe",
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django"      // 讓 VSCode Python-Django 的 linter 正常一點...
    ],
}
```



# Debugger - Launch.json

## Python - Django

```js
{

    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver",
                "--noreload",   // 如此才能 Debug阿@@
            ],
            "debugOptions": [
                "RedirectOutput",
                "Django"
            ],
            "pythonPath": "${config:python.pythonPath}"
        },
    ]
}
```


## Python - Tornado

```json
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



# go

```js
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
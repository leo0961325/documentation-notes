
# User Setting

```js
// settings.json
{
    // General
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
    "workbench.startupEditor": "none",
    "editor.minimap.enabled": false,
    "editor.mouseWheelZoom": true,
    "files.autoSave": "onWindowChange",
    "extensions.showRecommendationsOnlyOnDemand": true,
    "workbench.sideBar.location": "right",
    "editor.renderWhitespace": "all",
    "editor.detectIndentation": false,
    "editor.tabCompletion": true,

    // Tab Size
    "[html]":{
        "editor.tabSize": 2
    },

    // Markdown
    "markdown.preview.doubleClickToSwitchToEditor": false,
    "markdown.preview.fontFamily": "'Consolas', 'Droid Sans', 'sans-serif'",

    // Material Icon Theme
    "workbench.iconTheme": "material-icon-theme",

    // RestClient
    "rest-client.timeoutinmilliseconds": 2000,

    // Live Server
    "liveServer.settings.donotShowInfoMsg": true,

    // Power Mode
    "powermode.enabled": true,
    "powermode.presets": "flames",
    "powermode.enableStatusBarComboCounter": false,
    "powermode.enableStatusBarComboTimer": false,
}
```


# WorkSpace Setting

- [Using Pylint with Django](https://stackoverflow.com/questions/115977/using-pylint-with-django/31000713#31000713)

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



# KeyBindings

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


# Debugger - Launch.json


## Python

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


# .vscode/ 設定檔


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
}
```

## User keybindings.json
```js
// Place your key bindings in this file to overwrite the defaults
[
    {
        "key": "ctrl+m",
        "command": "editor.action.toggleMinimap"
    },
    {   
        "key": "ctrl+i",                "command": "editor.action.triggerSuggest",
        "when": "editorHasCompletionItemProvider && textInputFocus && !editorReadonly" 
    },
    { 
        "key": "ctrl+l",                "command": "expandLineSelection",
        "when": "textInputFocus" 
    },
]
```

## Django Debugger - Project settings
```js
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver",
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
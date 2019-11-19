
- 2018/11/09
- v1.27.2

```js
[
    {   // Toggle Mini Map
        "key": "ctrl+m",
        "command": "editor.action.toggleMinimap"
    },
    {   // IntelliSence
        "key": "ctrl+i",                
        "command": "editor.action.triggerSuggest",
        "when": "editorHasCompletionItemProvider && textInputFocus && !editorReadonly" 
    },
    {   // Current Line
        "key": "ctrl+l",                
        "command": "expandLineSelection",
        "when": "textInputFocus" 
    },
]
```
# [VSCode 套件 - Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
- 2018/07/07
- VSCode版本 1.24.1
- 套件版本 0.9.3



# 熱鍵
- `Ctrl+Alt+n` 執行
- `Ctrl+Alt+m` 中斷執行
- `Ctrl+Alt+j` 選擇語言來執行
- `Ctrl+Alt+k` 執行自訂指令 (不知道為啥... 某些 ?? 情況, 會無法使用)



# 組態
```json
{
    "code-runner.executorMap": {
        "javascript": "node",
        "python": "python",
        "html": "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"",
        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
    }
}
```
像是可以指定 `html` run 起來的時候, 以 chrome開啟



# 客製化參數
- `$workspaceRoot` : VS Code 開啟的 資料夾路徑
- `$dir` : 要執行的程式碼 的 資料夾
- `$dirWithoutTrailingSlash` : (同上), 但沒有 trailing slash
- `$fullFileName` : 要執行的程式碼 的 full file name
- `$fileName` : 要執行的程式碼 的 file name
- `$fileNameWithoutExt` : 要執行的程式碼 的 base name
- `$driveLetter` : 要執行的程式碼 的 drive letter
- `$pythonPath` : Python直譯器路徑



# 寫法注意事項
- 反斜線使用 `\\`
- **路徑內有空白鍵** 的話, 使用 `\"` 把 `路徑前後包起來`, ex: `"\"C:\Program Files\xxx\""`



# 組態說明

### `Ctrl+Alt+k` 執行的東西 (不知道為啥... 某些 ?? 情況, 會無法使用)
```json
{ "code-runner.customCommand": "echo Hello" }
```

### 清除前次執行
```json
{ "code-runner.clearPreviousOutput": true }
```

### 執行此檔案前, 自動存檔
```json
{ "code-runner.saveFileBeforeRun": true }
```

### 將執行程式的環境, 導向 Terminal!! 可以解決編碼問題 && 提供 REPL, `但是 一個專案只能同時存在一支執行中的程式`
```json
{ "code-runner.runInTerminal": true }
```

### 我不想回饋使用資訊
```json
{ "code-runner.enableAppInsights": false }
```

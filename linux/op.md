# 操作相關

- 2018/08/18



# Hotkey

使用 Bash 時, 可以使用下列熱鍵, 加速操作:

- `Alt  + .` : 把前一個指令最後一個字列出來
- `Ctrl + ←` : 往左一個單字片段
- `Ctrl + →` : 往右一個單字片段
- `Ctrl + r` : Command history 搜尋
- `Ctrl + u` : 刪除游標左邊
- `Ctrl + k` : 刪除游標右邊
- `Ctrl + w` : 刪除最近一個單字片段



# Brace Expression

```sh
# 善用 {} 來有智慧的操作
$ touch file{1..6}.txt
$ ls
file1.txt  file2.txt  file3.txt  file4.txt  file5.txt  file6.txt
# 但是使用 {} 之後的輸入, 就無法使用 tab 了
```



# Command Subsitution

- $(command)
- \`command\` : 比較老舊的方式, 不建議使用 ; 無法使用巢狀效果 「\`」唸 `導引號`

```sh
$ touch $(date +%F).log
$ ls
2018-08-18.log
```

- ${variable} : 建議作法
- $variable : 不嚴謹

```sh
$ x=200

# 變數和後文連在一起, 就悲劇了
$ echo x=$xK
x=

# 成功
$ echo x=${x}k
x=200k
```

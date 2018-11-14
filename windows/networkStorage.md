# 網路磁碟

- [Windows掛載、刪除網路磁碟net use指令](http://dannysun-unknown.blogspot.com/2017/10/windowsnet-use.html)
- 2018/11/08



```powershell
> net use
狀態   本機    遠端                         網路
-------------------------------------------------------------------------------
OK       R:    \\pomeswrd\87.documentation  Microsoft Windows Network
OK       S:    \\pomeswrd\96.softwares      Microsoft Windows Network
命令已經成功完成。
# 表示, 目前把 網路磁碟分別掛載到 Windows10 本地端的 R, S 槽

# 卸載 R 槽
> net use R: /delete
```



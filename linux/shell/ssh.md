# ssh 相關


## ssh tunnel 跳板訪問吧...

- 2018/09/29

在 localhost`A` 透過 `C` 訪問 `B`

- A: 169.254.10.30
- B: 169.254.10.10 (先安裝 `httpd`)
- C: 169.254.10.20

```sh
# 透過 tony@169.254.10.20 訪問 169.254.10.10:80, 並將結果回傳到本地的 8088 port (在A電腦執行)
$ ssl -L 8088:169.254.10.10:80 tony@169.254.10.20

# 瀏覽器~~ 「localhost:8088」 就看到網頁了~~
# 但是不知道為什麼　curl會出現
# curl: (7) Failed to connect to localhost port 8088: Connection refused
```

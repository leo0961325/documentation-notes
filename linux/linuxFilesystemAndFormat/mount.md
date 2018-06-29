# mount 掛載
- 2018/06/28

## 掛載重要基本概念

- `掛載點` 為 `目錄`
- `單一檔案系統` 不要重複掛載到 `不同的掛載點(目錄)`
- `單一目錄` 不要重複掛載到 `多個檔案系統`
- `要被掛載東西的目錄` 裏頭應該是 `空的` ((不然掛載後, 裡面的東西會`被隱藏`))  <- 卸載的時候, 會再出現





# swap 相關


## 使用檔案建置 swap

```sh
$ cd /tmp 
$ dd if=/dev/zero of=/tmp/swap bs=1M count=64
64+0 records in
64+0 records out
67108864 bytes (67 MB) copied, 0.0271058 s, 2.5 GB/s
# 使用 dd 這個指令, 新增一個 64MB 的檔案在 /tmp 底下

$ ll -h
總計 64M
-rw-rw-r--. 1 tony tony 64M  6月 28 21:57 swap

# 慎用!! 因為指令稍有錯誤, 可能導致檔案系統掛掉!!!!!
$ mkswap /tmp/swap
設定 swapspace 版本 1, 大小 = 65532 KiB
無標籤，UUID=a8e9102c-f7b0-47cd-a7b2-3d3b31d60d1a

# 因為一開始
$ swapon /tmp/swap
swapon: /tmp/swap：不安全的權限 0664, 建議使用 0600。
swapon: /tmp/swap: insecure file owner 1000, 0 (root) suggested.
swapon: /tmp/swap：swapon 失敗: 此項操作並不被允許
```
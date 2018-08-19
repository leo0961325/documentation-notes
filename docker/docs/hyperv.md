# VM Ware 與 Docker on Win10 相衝問題

- 20p18/02/10

裝完 VM Ware跑得好好的, 某天裝了 Docker後, vm就開不了了...

- [教學解法](https://www.youtube.com/watch?v=CGpv2Dvzyeg)
- `如果做了之後, 將來想再啟動 Docker時, 不知道該怎麼做...orz`


### Part1

1. 執行 gpedit.msc
2. 電腦設定/系統管理範本 > 系統 > Device Guard > 開啟虛擬化型安全性 > 點2下
3. 將它改為「已停用」


### Part2

1. 進入新增移除程式
2. 點選左邊的「開啟或關閉Windows功能」
3. 找到 「Hyper-V」後, 將他的打勾拿掉
4. (不要重新啟動)


### Part3

1. (系統管理員身分)執行 命令提示字元
2. 把下面這包貼上, 跑完後會出現 「success」的字樣

```sh
bcdedit /create {0cb3b571-2f2e-4343-a879-d86a476d7215} /d "DebugTool" /application osloader
bcdedit /set {0cb3b571-2f2e-4343-a879-d86a476d7215} path "\EFI\Microsoft\Boot\SecConfig.efi"
bcdedit /set {bootmgr} bootsequence {0cb3b571-2f2e-4343-a879-d86a476d7215}
bcdedit /set {0cb3b571-2f2e-4343-a879-d86a476d7215} loadoptions DISABLE-LSA-ISO,DISABLE-
```
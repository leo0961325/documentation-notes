# redis 安裝在 Windows10
- 2018/05/14
- [看我看我](https://github.com/MicrosoftArchive/redis/releases)
- [選我選我](https://dotblogs.com.tw/supershowwei/2015/12/23/124549)

安裝完後, 資料夾底下
```cmd
> dir
 磁碟區 D 中的磁碟是 Data
 磁碟區序號:  OOOO-XXXX

 D:\Program Files\Redis 的目錄

2018/05/14  下午 08:41    <DIR>          .
2018/05/14  下午 08:41    <DIR>          ..
2016/07/01  下午 04:27             1,024 EventLog.dll
2016/07/01  下午 04:07            12,509 Redis on Windows Release Notes.docx
2016/07/01  下午 04:07            16,727 Redis on Windows.docx
2016/07/01  下午 04:28           409,088 redis-benchmark.exe
2016/07/01  下午 04:28         4,370,432 redis-benchmark.pdb
2016/07/01  下午 04:28           257,024 redis-check-aof.exe
2016/07/01  下午 04:28         3,518,464 redis-check-aof.pdb
2016/07/01  下午 04:28           499,712 redis-cli.exe
2016/07/01  下午 04:28         4,526,080 redis-cli.pdb
2016/07/01  下午 04:28         1,666,560 redis-server.exe
2016/07/01  下午 04:28         7,081,984 redis-server.pdb
2018/05/07  上午 11:28            48,208 redis.windows-service.conf
2018/05/07  上午 11:38            48,256 redis.windows.conf
2018/05/14  上午 09:10               824 server_log.txt
2016/07/01  上午 09:17            14,265 Windows Service Documentation.docx
              15 個檔案      22,471,157 位元組
               2 個目錄  454,883,938,304 位元組可用
```

啟動服務後~~~
```powershell
services.msc  # 啟動 Redis服務
```

查看 redis組態資訊
```powershell
> redis-cli.exe -h 127.0.0.1 -p 6379 info

#((約有 70~80個 組態資訊 在此省略))
```

進入 redis-cli
```powershell
> redis-cli.exe -h 127.0.0.1 -p 6379
127.0.0.1:6374 > 
```
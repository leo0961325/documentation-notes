# 壓縮 && 解壓縮
- 2018/07/04

Linux 常用壓縮技術, 因為多半壓縮只能對單一檔案作壓縮, 所以會將他們作 `tar 打包` 後, 再來壓縮 ( `tar` = `打包的軟體` )
```
*.Z         由 compress 壓縮    # 老舊~
*.zip       由 zip 壓縮         # 為了支援 Windows
*.gz        由 gzip 壓縮        # 可以解開 compress, zip, gz
*.bz2       由 bzip2 壓縮       # 
*.xz        由 xz 壓縮          # 這個比較新(壓縮品質不錯)

*.tar       由 tar 打包, 未壓縮
*.tar.gz    由 tar 打包, 由 gzip 壓縮
*.tar.bz2   由 tar 打包, 由 bzip2 壓縮
*.tar.xz    由 tar 打包, 由 xz 壓縮
```

## gzip, zcat/zmore/zless/zgrep
- 這邊只舉 `gzip`, `zcat`, `zgrep` 為例
- 可以把 `gzip` 想像成是為了取代 `compress` 而生

```sh
$ gzip [-cdtv#] filename
-c : 壓縮資料流導向螢幕, 可重新導向資料流
-d : 有寫這個的話, 表示是在作 解壓縮
-t : 有點像是在測試檔案用的吧, 檢驗壓縮檔的一致性
-v : 顯示出 原/壓縮後 的壓縮比資訊
-# : #為數字, 1(最快)~9(最佳), 預設 -6

$ ls -ldSr /etc/*   # ldSrh:詳細資訊, 只顯示Dir, 大小排序, 反向列出, 顯示KB MB GB
...(略)...

$ cp /etc/services /tmp/.   # 把剛剛看到最大的Dir 複製出去

$  gzip -v services
services:        79.7% -- replaced with services.gz

$ ll -h /etc/services /tmp/services*
-rw-r--r--. 1 root root 655K  6月  7  2013 /etc/services
-rw-r--r--. 1 tony tony 133K  7月  4 00:31 /tmp/services.gz
# gzip 預設會打包成 .gz
# 且原始檔會消失
# 此檔案可被 Windows 的 WinRAR/7zip解壓縮

# 等同 cat 看檔案, zcat 可看 .gz 的內容
$ zcat services.gz

# zgrep 可以找 .gz檔內的某些文字, 放在第幾行
$ zgrep -n 'http' services.gz
14:#       http://www.iana.org/assignments/port-numbers
89:http            80/tcp          www www-http    # WorldWideWeb HTTP
90:http            80/udp          www www-http    # HyperText Transfer Protocol
```


## bzip2, bzcat/bzmore/bzless/bzgrep
- 可以把 `gzip2` 想像成是為了取代 `gzip` 而生
- 指令幾乎與 `gzip` 一樣 ; 
- 相較 `gzip`, 大檔案的話, 壓縮品質提升, 但速度較慢

```sh
$ gzip2 [-cdkzv#] filename
-c : 壓縮資料流導向螢幕, 可重新導向資料流
-d : 有寫這個的話, 表示是在作 解壓縮
-k : 有寫的話, 壓縮完仍保留原始檔不刪除
-z : 壓縮的參數(此為預設, 沒必要寫這個...)
-v : 顯示出 原/壓縮後 的壓縮比資訊
-# : #為數字, 1(最快)~9(最佳), 預設 -6

$ bzip2 -v services
services:  5.409:1,  1.479 bits/byte, 81.51% saved, 670293 in, 123932 out.
# 122K
# 筆上面的 79% 還要強大~~  變成 81.5%
```

## xz, xzcat/xzmore/xzless/xzgrep
- 語法也幾乎與 `gzip2` 一樣
- 壓縮品質筆 `gzip2` 還要好, 時間更久 =..=

```sh
$ xz [-dtlkc#] filename
-d : 有寫這個的話, 表示是在作 解壓縮
-t : 檢驗壓縮檔的完整性
-l : 列出壓縮檔的相關資訊
-k : 有寫的話, 壓縮完仍保留原始檔不刪除
-c : 壓縮資料流導向螢幕, 可重新導向資料流
-# : #為數字, 1(最快)~9(最佳), 預設 -6

$ xz -v services
services (1/1)
  100 %        97.3 KiB / 654.6 KiB = 0.149

# 三種壓縮技術比較~
$ ll -h
-rw-r--r--. 1 tony tony 133K  7月  4 00:55 services.gz
-rw-r--r--. 1 tony tony 122K  7月  4 00:55 services.bz2
-rw-r--r--. 1 tony tony  98K  7月  4 00:31 services.xz

# 可看壓縮前後比較
$ xz -l services.xz
Strms  Blocks   Compressed Uncompressed  Ratio  Check   Filename
    1       1     97.3 KiB    654.6 KiB  0.149  CRC64   services.xz
```
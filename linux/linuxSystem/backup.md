# backup備份 restore還原
- [Backup](http://linux.vbird.org/linux_basic/0610hardware.php#backup_type)

## 工具
- dd (直接讀取磁碟, 非常慢喔)
- cpio (得要有 find 之類的找檔名指令)
- xfsdump/xfsrestore (可直接進行累積備份)
- rsync (非常快速)
- ghost (很早期的備份工具, 針對單機作backup&&restore)
- 再生龍(可把磁碟的東西複製成一個大檔案, 鳥哥很推薦這個)

## 完整備份之累積備份(Incremental backup)
週日作完整備份, 爾後則比較今天與`昨天`的差異, 備份差異部分. 再隔天, 一樣與`昨天`比較後, 備份差異的部分. 依此類推~


## 完整備份之差異備份(Differential backup)
週日作完整備份, 爾後則比較今天與`第一天`的差異, 備份差異部分. 再隔天, 一樣與`第一天`比較後, 備份差異的部分. 依此類推~ (`差異備份`會越來越大包)

### 鏡像備份(Mirror backup)

```sh
$ rsync -av <來源> <目標>
```


# 差異備份範例
- 2018/07/08
- [鳥哥 - 僅備份比某個時刻還要新的檔案](http://linux.vbird.org/linux_basic/0240tarcompress.php#pack)

```sh
# 某些情況下, 只會想要備份 `比某日期還新` 的檔案
# 找出比 /etc/passwd 還新, 且放在 /etc/裏頭的東西 (su)
$# find /etc -newer /etc/passwd
/etc
/etc/resolv.conf
/etc/rwtab.d
/etc/logrotate.d
/etc/shadow
/etc/selinux/targeted
/etc/selinux/targeted/tmp
/etc/selinux/targeted/tmp/modules
/etc/selinux/targeted/tmp/modules/100
...(略)...

$# ll /etc/passwd
-rw-r--r--. 1 root root 2541  6月 26 21:43 /etc/passwd

# 僅對於 (mtime) 2018/06/26 以後有異動過的檔案, 作差異備份~ (打包壓縮)
$# tar zcvf bb.tar.gz --newer-mtime="2018/06/26" /etc/*
tar: 選項 --newer-mtime: 以 2018-06-26 00:00:00 格式來處理日期「2018/06/26」
tar: 從成員名稱中移除前端的「/」
/etc/selinux/targeted/tmp/policy.linked                                  # 有備份
tar: /etc/abrt/abrt-action-save-package-data.conf：檔案沒有變更；未傾印     # 沒備份
...(略)...

# 查看 tar 內, 結尾非 「/」的檔名
$# tar ztvf bb.tar.gz | grep -v '/$'
-rw-r----- root/lp         410 2018-06-27 23:02 etc/cups/subscriptions.conf.O
-rw-r----- root/lp         111 2018-06-28 09:06 etc/cups/subscriptions.conf
-rw-r--r-- root/root      1062 2018-06-26 21:43 etc/group
...(略)...

```
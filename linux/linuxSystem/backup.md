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

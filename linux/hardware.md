# Linux硬梆梆的東東(比較底層的東西)
- 顯卡
- 檔案系統
- 硬體

> 在 Linux中, 每個裝置都被當成一個**檔案**來對待


## 常見的硬體裝置, 在 Linux中的檔名
裝置 | Linux內的檔名
--- | ----------------------
SCSI / SATA / USB <br> (統稱 SCSI硬碟) | `/dev/sd[a-p]` <br> ex: `/dev/sda`, `/dev/sda1`, `/dev/sda2` <br> 可以做到 15個邏輯分割區
IDE硬碟 | `/dev/hd[a-d]` (舊有系統), 但也有部分的 IDE硬碟, 被偽裝成了 `/dev/sd[a-d]` <br> 可以做到 63個邏輯分割區
Virtual I/O介面 | `/dev/vd[a-p]` (用於虛擬機器內)
印表機 | `/dev/usb/lp[0-15]` (USB介面) <br> `/dev/lp[0-2]` (25針腳印表機)
滑鼠 | `/dev/input/mouse[0-15]` (通用) <br> `/dev/psaux` (PS/2介面)
CDROM/DVDROM | `/dev/cdrom` (當前CDROM, 指向`/dev/sr0` )  <br> `/dev/sr[0-1]` (通用, CentOS比較常見) <br> ex: `/dev/sr0`

```
/dev/sda1

其中, 
sd: SCSI磁碟
a: 第 1 顆 SCSI碟
4: 第 4 個分割區
```

## 磁碟分割表的格式
> 整顆磁碟的`第一個磁區`記錄了整顆磁碟的重要資訊, 早期第一個磁區的重要資訊, 稱之為 MBR(Master Boot Record), 但隨著磁碟容量不斷擴大, 新一代的磁碟分割格式, 稱之為 GPT(GUID partition table)

(舊式)MBR分割表, 第一個磁區(512 bytes), 內有:
1. 主要開機區(Master boot record, MBR) - 446 byes
2. 分割表(partition table) - 64 bytes

MBR最大, 僅能容納 2.2T; 實體磁區大小 512Bytes; 32bit長度的磁區位置

```sh
# 列出所有儲存裝置
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 931.5G  0 disk
└─sda1   8:1    0 931.5G  0 part /
```
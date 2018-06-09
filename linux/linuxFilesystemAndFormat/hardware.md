# CentOS7 硬體部份


> 在 Linux中, 每個裝置都被當成一個**檔案**來對待

# Linux硬梆梆的東東(比較底層的東西)
- 顯卡
- 檔案系統
- 硬體

```sh
# gdisk 列出分割表
$ 

# dmesg 核心運作過程, 產生的訊息紀錄
$ 

# vmstat 分析系統(CPU/RAM/IO)目前的狀態
$ 

# lspci 列出 PCI介面裝置
$

# lsusb 列出 USB port
$ 

# iostat 列出整個 CPU與 周邊設備的I/O狀態 (類似 vmstat)
$ 

# lsmod: 查看核心模組
$ lsmod | grep nouveau
nouveau              1527946  0 
mxm_wmi                13021  1 nouveau
ttm                    93908  1 nouveau
i2c_algo_bit           13413  2 i915,nouveau
drm_kms_helper        146456  2 i915,nouveau
drm                   372540  4 ttm,i915,drm_kms_helper,nouveau
wmi                    19070  2 mxm_wmi,nouveau
video                  24400  2 i915,nouveau
i2c_core               40756  8 drm,i915,i2c_i801,i2c_hid,drm_kms_helper,i2c_algo_bit,nouveau,videodev
```

----------------------------------------------------------------------------------
# 未分類
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

----------------------------------------------------------------------------------
# Linux檔案系統
## 磁碟分割表的格式
1. (早期) MBR分割表 (max 2.2TB)
    - `第一個磁區`(實體磁區512 bytes; 32bits長度的磁區位置) 記錄了整顆磁碟的重要資訊, 有 2個部份
        1. 主要開機區(Master boot record, MBR) - 446 byes
        2. 分割表(partition table) - 64 bytes

2. (現代) GPT分割表
    - 可支援超過 2TB的大硬碟



```sh
# 列出所有儲存裝置
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 931.5G  0 disk
└─sda1   8:1    0 931.5G  0 part /
```

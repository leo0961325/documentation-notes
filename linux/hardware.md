# CentOS7 硬體部份

## 開機管理程式 grub

早期: `grub1`, `LILO`, `spfdisk(台灣很多人用)`

近期: `grub2`


-------------------------------------------------------------------
## 在 CentOS7 安裝 NVIDIA 顯示卡驅動程式 (尚未完成)
- 2018/03/24 
- [Installing Nvidia GPU Driver with Nvidia Detect](https://www.youtube.com/watch?v=C9Yf71qh0i4)

> CentOS7預設使用 `nouveau`這個顯示晶片的驅動程式, 若要安裝像是 Nvidia顯卡驅動的話, 得先下載好相對應的驅動程式, 關閉 `nouveau`, 然後關閉 `圖形界面(runlevel=3)` 的狀態下重新開機, 開始安裝 顯卡驅動, 然後重新設定 `runlevel=5`, 重新開機後, 應該就沒問題了^_^凸

```sh
# 查出電腦是用哪款的 NVIDIA顯卡

# 法1 從 PCI上查看
# 顯示目前主機上面的各個 PCI 介面的裝置
$ lspci
00:00.0 Host bridge: Intel Corporation Device 5904 (rev 02)
00:02.0 VGA compatible controller: Intel Corporation Device 5916 (rev 02)
00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21)
00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
00:1c.5 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #6 (rev f1)
00:1d.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #9 (rev f1)
00:1f.0 ISA bridge: Intel Corporation Device 9d58 (rev 21)
00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
00:1f.3 Audio device: Intel Corporation Device 9d71 (rev 21)
00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
01:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 10)
02:00.0 Network controller: Realtek Semiconductor Co., Ltd. RTL8821AE 802.11ac PCIe Wireless Network Adapter
03:00.0 3D controller: NVIDIA Corporation GM108M [GeForce 920MX] (rev a2)       ### 找到型號了!!

### 法2 額外安裝NVIDIA軟體來查看
$ sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
$ sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.repo.noarch.rpm
$ sudo yum -y install nvidia-detect
$ nvidia-detect -v
Probing for supported NVIDIA devices...
[10de:134f] NVIDIA Corporation GM108M [GeForce 920MX]       ### 找到型號了!!
This device requires the current 390.25 NVIDIA driver kmod-nvidia
[8086:5916] Intel Corporation Device 5916
An Intel display controller was also detected
```


----------------------------------------------------------------------------------
# Linux硬梆梆的東東(比較底層的東西)
- 顯卡
- 檔案系統
- 硬體

```sh
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
SCSI / SATA / USB | `/dev/sd[a-p]` <br> ex: `/dev/sda`, `/dev/sda1`, `/dev/sda2`
IDE硬碟 | `/dev/hd[a-d]` (舊有系統), 但也有部分的 IDE硬碟, 被偽裝成了 `/dev/sd[a-d]`
印表機 | `/dev/usb/lp[0-15]` (USB介面) <br> `/dev/lp[0-2]` (25針腳印表機)
滑鼠 | `/dev/input/mouse[0-15]` (通用) <br> `/dev/psaux` (PS/2介面)
CDROM/DVDROM | `/dev/cdrom` (當前CDROM, 指向`/dev/sr0` )  <br> `/dev/sr[0-1]` (通用, CentOS比較常見) <br> ex: `/dev/sr0`
Virtual I/O介面 | `/dev/vd[a-p]` (用於虛擬機器內)



## 磁碟分割表的格式
> 整顆磁碟的`第一個磁區`記錄了整顆磁碟的重要資訊, 早期第一個磁區的重要資訊, 稱之為 MBR(Master Boot Record), 但隨著磁碟容量不斷擴大, 新一代的磁碟分割格式, 稱之為 GPT(GUID partition table)

MBR分割表, 第一個磁區(512 bytes), 內有:
1. 主要開機區(Master boot record, MBR) - 446 byes
2. 分割表(partition table) - 64 bytes

```sh
# 列出所有儲存裝置
$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 931.5G  0 disk
└─sda1   8:1    0 931.5G  0 part /
```
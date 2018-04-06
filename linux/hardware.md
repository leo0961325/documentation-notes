# CentOS7 硬體部份

## 開機管理程式 grub

早期: `grub1`, `LILO`, `spfdisk(台灣很多人用)`

近期: `grub2`




-------------------------------------------------------------------
## 在 CentOS7 安裝 NVIDIA 顯示卡驅動程式 (尚未完成)
- 2018/03/24 

> CentOS7預設使用 `nouveau`這個顯示晶片的驅動程式, 若要安裝像是 Nvidia顯卡驅動的話, 得先下載好相對應的驅動程式, 關閉 `nouveau`, 然後關閉 `圖形界面(runlevel=3)` 的狀態下重新開機, 開始安裝 顯卡驅動, 然後重新設定 `runlevel=5`, 重新開機後, 應該就沒問題了^_^凸


> `lsmod` 觀察核心模組

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



# 安裝 NVIDIA driver
[Installing Nvidia GPU Driver with Nvidia Detect](https://www.youtube.com/watch?v=C9Yf71qh0i4)
```sh
# 
$ sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org

# 
$ sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.repo.noarch.rpm

#
$ sudo yum -y install nvidia-detect

# 
$ nvidia-detect -v
Probing for supported NVIDIA devices...
[10de:134f] NVIDIA Corporation GM108M [GeForce 920MX]
This device requires the current 390.25 NVIDIA driver kmod-nvidia
[8086:5916] Intel Corporation Device 5916
An Intel display controller was also detected
```

# 安裝 顯示卡驅動程式 - Nvidia

```sh
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

# ????
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
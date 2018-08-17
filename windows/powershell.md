# powershell 指令

```powershell
# 查詢自己的主機名稱
> HOSTNAME
520-QQ081-1
```


### sys-admin

```powershell
# 啟動 Hyper-V - https://docs.microsoft.com/zh-tw/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

```powershell
# 查詢虛擬交換器
> Get-VMSwitch
Name              SwitchType NetAdapterInterfaceDescription
----              ---------- ------------------------------
Private Network   Private
Default Switch    Internal


# 查詢 網卡
> Get-NetAdapter
Name                        InterfaceDescription               ifIndex  Status       MacAddress   LinkSpeed
----                        --------------------               -------  ------       ----------   ---------
vEthernet (Default Switch)  Hyper-V Virtual Ethernet Adapter        14  Disconnected (pass)       10 Gbps
Ethernet                    Realtek PCIe GBE Family Controller       2  Up           (pass)       100 Mbps
Wi-Fi                       Intel(R) Dual Band Wireless-AC 8260     17  Disconnected (pass)       6 Mbps


# 查詢 虛擬機器
> Get-VM
Name State   CPUUsage(%) MemoryAssigned(M) Uptime           Status   Version
---- -----   ----------- ----------------- ------           ------   -------
v01  Running 16          1238              00:11:52.2810    正常運作 8.2

# https://www.bountysource.com/issues/40110135-hyper-v-was-unable-to-find-a-virtual-switch-with-name-dockernat
> powershell -ExecutionPolicy ByPass -File "C:\Program Files\Docker\Docker\resources\MobyLinux.ps1" -create

```




### 一般指令

```powershell
> whoami /all
USER INFORMATION
----------------

使用者名稱                SID
========================= ==============================================
<網域名稱>\tony.jhou S-1-5-21-2132128451-2814014226-1695114138-1174

GROUP INFORMATION
-----------------

群組名稱                               類型       SID                                            屬性
====================================== ========== ============================================== ====================================
Everyone                               知名的群組 S-1-1-0                                        強制性群組, 預設為啟用, 已啟用的群組
# (略)...
BUILTIN\Administrators                 別名       S-1-5-32-544                                   僅用於拒絕的群組
# (略)...

PRIVILEGES INFORMATION
----------------------

特殊權限名稱                  描述               狀況
============================= ================== ======
SeShutdownPrivilege           關閉系統           已停用
SeChangeNotifyPrivilege       略過周遊檢查       已啟用
SeUndockPrivilege             從擴充座移除電腦   已停用
SeIncreaseWorkingSetPrivilege 增加處理程序工作組 已停用
SeTimeZonePrivilege           變更時區           已停用

使用者宣告資訊
-----------------------

使用者宣告未知。
```


```powershell
# And運算
> 1 -and 1
True
```

```powershell
# 檢視 IPv4 的 路由表資訊
> route print -4
===========================================================================
介面清單
 11...fc aa 14 83 8a c9 ......Realtek PCIe GBE Family Controller
 14...00 15 5d 01 10 02 ......Hyper-V Virtual Ethernet Adapter
 17...68 05 ca 1e d8 55 ......Intel(R) Gigabit CT Desktop Adapter #4
  1...........................Software Loopback Interface 1
  4...00 00 00 00 00 00 00 e0 Microsoft ISATAP Adapter #2
 24...00 00 00 00 00 00 00 e0 Microsoft ISATAP Adapter #4
===========================================================================

IPv4 路由表
===========================================================================
使用中的路由:
網路目的地                 網路遮罩         閘道          介面       計量
          0.0.0.0          0.0.0.0       10.0.1.254       10.0.1.110    281
         10.0.1.0    255.255.255.0            在連結上        10.0.1.110    281
       10.0.1.110  255.255.255.255            在連結上        10.0.1.110    281
       10.0.1.255  255.255.255.255            在連結上        10.0.1.110    281
        127.0.0.0        255.0.0.0            在連結上         127.0.0.1    331
        127.0.0.1  255.255.255.255            在連結上         127.0.0.1    331
  127.255.255.255  255.255.255.255            在連結上         127.0.0.1    331
      169.254.0.0      255.255.0.0            在連結上    169.254.36.197    271
   169.254.36.197  255.255.255.255            在連結上    169.254.36.197    271
  169.254.255.255  255.255.255.255            在連結上    169.254.36.197    271
        224.0.0.0        240.0.0.0            在連結上         127.0.0.1    331
        224.0.0.0        240.0.0.0            在連結上        10.0.1.110    281
        224.0.0.0        240.0.0.0            在連結上    169.254.36.197    271
  255.255.255.255  255.255.255.255            在連結上         127.0.0.1    331
  255.255.255.255  255.255.255.255            在連結上        10.0.1.110    281
  255.255.255.255  255.255.255.255            在連結上    169.254.36.197    271
===========================================================================
持續路由:
  網路位址          網路遮罩  閘道位址  計量
          0.0.0.0          0.0.0.0       10.0.1.254    預設值
===========================================================================
```


# 設定環境變數

```powershell
# 建立環境變數
> $Env:uu = "Tony"


# 取得環境變數 (後面開啟的 powershell 也吃得到此變數, 但是 cmd 一樣看不到)
> $Env:uu
Tony


# 取得 環境變數 詳細清單 (最後一定要加上「:」, 不指定特定變數的話, 表示查全部)
> Get-ChildItem Env:        # 只查 uu -> Get-ChildItem Env:uu

Name                           Value
----                           -----
bash_home                      C:\Program Files\Git
...(略)...
USERNAME                       tony.jhou
uu                             Tony


# 更改 環境變數
> $Env:uu = "TonyCJ"

# 刪除 環境變數
> Remove-Item Env:tt

# 設定到 系統環境變數 (以系統管理員方式執行 ps)
> setx key "<value>" /M
```

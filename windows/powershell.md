# powershell 指令

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
pomerobotservic\tony.jhou S-1-5-21-2132128451-2814014226-1695114138-1174

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
# powershell 指令

### sys-admin


```powershell
# 查詢虛擬交換器
> Get-VMSwitch

Name            SwitchType NetAdapterInterfaceDescription
----            ---------- ------------------------------
Private Network Private
預設切換        Internal
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
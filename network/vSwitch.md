# Virtual Switch
- 2018/05/17
- update 2018/09/30

對於 虛擬交換器的操作(新增/修改/刪除), 可能因為公司有設定網域 的關係, 而無法操作

```powershell
# 列出 虛擬交換器們
> Get-VMSwitch
Name             SwitchType NetAdapterInterfaceDescription
----             ---------- ------------------------------
Private Network  Private
Internal Network Internal
External Network External   Intel(R) Ethernet Connection (2) I219-V
預設切換         Internal   Teamed-Interface
DockerNAT        Internal       # Docker on Windows

# 移除虛擬交換器
> Get-VMSwitch "Private Network" | Remove-VMSwitch
```

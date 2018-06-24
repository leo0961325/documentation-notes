# Virtual Switch
- 2018/05/17

## problem: Windows 10 無法在 Hyper-V 新增 **私有以外的` 虛擬交換器`**?

> 經詢問老師後, 得知: Windows 10 升級到 `1709`版的時候, 預設會放一個 `預設切換` 的 `內部交換器` 在 Hyper-V裏頭, 而它會幫 VM 預設都用 `NAT` 的方式來設定虛擬網卡. 所以如果硬要 **自己新增 交換器** 的話, 得先把 `預設切換這個 內部交換器` 砍掉~ 才能新增其他 交換器. 而這個, 只能透過 指令的方式砍掉... 而老師不建議我這麼做. 指令如下:

> 指令: `Get-VMSwitch <虛擬交換器名稱> | Remove-VMSwitch` (老師不建議我使用)

```powershell
# 不知道為什麼無法執行
> Remove-VMSwitch "預設切換"

確認
確定要移除虛擬交換器 "預設切換"?
[Y] 是(Y)  [A] 全部皆是(A)  [N] 否(N)  [L] 全部皆否(L)  [S] 暫停(S)  [?] 說明 (預設值為 "Y"): A
Remove-VMSwitch : 移除虛擬乙太網路交換器失敗。
無法修改自動網際網路連線共用切換。
位於 線路:1 字元:1
+ Remove-VMSwitch "預設切換"
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Remove-VMSwitch]，VirtualizationException
    + FullyQualifiedErrorId : InvalidParameter,Microsoft.HyperV.PowerShell.Commands.RemoveVMSwitch
# Get-VMSwitch <虛擬交換器名稱> | Remove-VMSwitch
> Get-VMSwitch 預設切換 | Remove-VMSwitch

# 安裝完 Docker on Windows 後, 可正常使用的情況
> Get-VMSwitch
Name             SwitchType NetAdapterInterfaceDescription
----             ---------- ------------------------------
Private Network  Private
Internal Network Internal
External Network External   Intel(R) Ethernet Connection (2) I219-V
預設切換         Internal   Teamed-Interface
DockerNAT        Internal

# 安裝完 Docker on Windows 後, 無法使用的情況(找不到 DockerNAT)
> Get-VMSwitch

Name            SwitchType NetAdapterInterfaceDescription
----            ---------- ------------------------------
預設切換        Internal
Private Network Private
```
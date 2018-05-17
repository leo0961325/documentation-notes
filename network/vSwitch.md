# Virtual Switch
- 2018/05/17

## problem: Windows 10 無法在 Hyper-V 新增 **私有以外的` 虛擬交換器`**

> 經詢問老師後, 得知: Windows 10 升級到 `1709`版的時候, 預設會放一個 `預設切換` 的 `內部交換器` 在 Hyper-V裏頭, 而它會幫 VM 預設都用 `NAT` 的方式來設定虛擬網卡. 所以如果硬要 **自己新增 交換器** 的話, 得先把 `預設切換這張 內部交換器` 砍掉~ 才能新增其他 交換器. 而這張, 只能透過 指令的方式砍掉... 而老師不建議我這麼做. 指令如下:

```powershell
# Get-VMSwitch <虛擬交換器名稱> | Remove-VMSwitch
> Get-VMSwitch 預設切換 | Remove-VMSwitch
```
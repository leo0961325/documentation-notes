# [Microsoft Hyper-V](https://docs.docker.com/machine/drivers/hyper-v/)
- 2018/06/24
- [Windows 10 Docker-Machine 使用 Hyper-V](https://docs.docker.com/machine/drivers/hyper-v/#example)

Docker on Windows 10 使用 Docker machine 的問題


已經使用 系統管理員權限 來使用了~
```powershell
# 不曉得為啥...
> docker-machine create --driver hyperv myvm1
Running pre-create checks...
Error with pre-create check: "Hyper-V PowerShell Module is not available"

> Get-VMSwitch
Name      SwitchType NetAdapterInterfaceDescription
----      ---------- ------------------------------
DockerNAT Internal
預設切換  Internal   Teamed-Interface

> docker-machine create --driver hyperv --hyperv-virtual-switch "預設切換" myvm1
Running pre-create checks...
Error with pre-create check: "Hyper-V PowerShell Module is not available"
```
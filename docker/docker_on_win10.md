# Docker on Windows 10

- 2018/05/11
- 18.03.1-ce
- [相關解法 - 找這個回覆 kleskowy commented on 17 Nov 2017](https://github.com/docker/for-win/issues/324)
- [安裝 Docker for Windows 10](https://docs.docker.com/docker-for-windows/install/)

> 5/11, 不知道為什麼你他媽的一直灌不起來, 錯誤訊息也看不懂, 所以先記錄下來

```
Unable to create: 執行中的命令已停止，因為喜好設定變數 "ErrorActionPreference" 或一般參數設定為 Stop: Hyper-V 找不到名為 "DockerNAT" 的虛擬交換器。
位於 New-Switch，<無檔案>: 第 117 行
位於 <ScriptBlock>，<無檔案>: 第 394 行
   於 Docker.Core.Pipe.NamedPipeClient.Send(String action, Object[] parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Core\pipe\NamedPipeClient.cs: 行 36
   於 Docker.Actions.DoStart(SynchronizationContext syncCtx, Boolean showWelcomeWindow, Boolean executeAfterStartCleanup) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 67
   於 Docker.Actions.<>c__DisplayClass14_0.<Start>b__0() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 51
   於 Docker.WPF.TaskQueue.<>c__DisplayClass19_0.<.ctor>b__1() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.WPF\TaskQueue.cs: 行 59
```

> 5/11, 最後幾行的 Log file 長這樣
```
[15:33:28.260][NamedPipeServer][Info   ] TryGetVhdxSize()
[15:33:28.260][PowerShell     ][Info   ] Run script 'Get-VHD –Path "" | select -ExpandProperty Size'...
[15:33:28.262][NamedPipeServer][Info   ] TryGetVhdxSize done in 00:00:00.0019983.
[15:33:49.693][NamedPipeServer][Error  ] Unable to execute Start: Unable to create: 執行中的命令已停止，因為喜好設定變數 "ErrorActionPreference" 或一般參數設定為 Stop: Hyper-V 找不到名為 "DockerNAT" 的虛擬交換器。
位於 New-Switch，<無檔案>: 第 117 行
位於 <ScriptBlock>，<無檔案>: 第 394 行    於 Docker.Backend.HyperV.RunScript(String action, Dictionary`2 parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\HyperV.cs: 行 183
   於 Docker.Backend.ContainerEngine.Linux.Start(Settings settings, String daemonOptions) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\ContainerEngine\Linux.cs: 行 111
[15:33:50.227][NamedPipeClient][Error  ] Unable to send Start: Unable to create: 執行中的命令已停止，因為喜好設定變數 "ErrorActionPreference" 或一般參數設定為 Stop: Hyper-V 找不到名為 "DockerNAT" 的虛擬交換器。
位於 New-Switch，<無檔案>: 第 117 行
位於 <ScriptBlock>，<無檔案>: 第 394 行
[15:33:50.251][Notifications  ][Error  ] Unable to create: 執行中的命令已停止，因為喜好設定變數 "ErrorActionPreference" 或一般參數設定為 Stop: Hyper-V 找不到名為 "DockerNAT" 的虛擬交換器。
位於 New-Switch，<無檔案>: 第 117 行
位於 <ScriptBlock>，<無檔案>: 第 394 行
[15:35:09.808][ErrorReportWindow][Info   ] Open logs
```

> 5/11, 辛苦的弄了半個小時, 其實我真的沒動到什麼, 只是用 `系統管理員權限` 去開啟 `Hyper-V` 及 `Docker`, 然後忘了在什麼條件底下, 原本 **虛擬交換器管理員** 只有一個「預設切換」, 但偶然間出現 「DockerNAT」, 重開後又消失了!! 然後 Docker就成功啟動了... (幹!!  沙小...).  只是 `Docker`啟動成功後, 在開啟 `Hyper-V`, 就看不到 「DockerNAT」了.

> 5/14, 就在幾天後, 我又執行 Docker > Switch to Windows Containers..., 不一會兒又爆錯了
```
Unable to create: 執行中的命令已停止，因為喜好設定變數 "ErrorActionPreference" 或一般參數設定為 Stop: Hyper-V 找不到名為 "DockerNAT" 的虛擬交換器。
位於 New-Switch，<無檔案>: 第 117 行
位於 <ScriptBlock>，<無檔案>: 第 394 行
   於 Docker.Core.Pipe.NamedPipeClient.Send(String action, Object[] parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Core\pipe\NamedPipeClient.cs: 行 36
   於 Docker.Actions.<>c__DisplayClass23_0.<SwitchDaemon>b__0() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 262
   於 Docker.WPF.TaskQueue.<>c__DisplayClass19_0.<.ctor>b__1() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.WPF\TaskQueue.cs: 行 59
```

> 5/14, 點選還原回原始設定後, 錯誤訊息又不太一樣...orz
```
Unable to create: 執行中的命令已停止，因為喜好設定變數 "ErrorActionPreference" 或一般參數設定為 Stop: Hyper-V 找不到名為 "DockerNAT" 的虛擬交換器。
位於 New-Switch，<無檔案>: 第 117 行
位於 <ScriptBlock>，<無檔案>: 第 394 行
   於 Docker.Core.Pipe.NamedPipeClient.Send(String action, Object[] parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Core\pipe\NamedPipeClient.cs: 行 36
   於 Docker.Actions.DoStart(SynchronizationContext syncCtx, Boolean showWelcomeWindow, Boolean executeAfterStartCleanup) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 67
   於 Docker.Actions.<>c__DisplayClass16_0.<ResetToDefault>b__0() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 124
   於 Docker.WPF.TaskQueue.<>c__DisplayClass19_0.<.ctor>b__1() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.WPF\TaskQueue.cs: 行 59
```

> 5/15, 開機後又無法正常啟動...

```
Docker for Windows service is not running
   於 Docker.WPF.BackendClient.CheckService() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.WPF\BackendClient.cs: 行 356
   於 Docker.WPF.BackendClient.SendMessage(String action, Object[] parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.WPF\BackendClient.cs: 行 167
   於 Docker.Actions.DoStart(SynchronizationContext syncCtx, Boolean showWelcomeWindow, Boolean executeAfterStartCleanup) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 67
   於 Docker.Actions.<>c__DisplayClass14_0.<Start>b__0() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 51
   於 Docker.WPF.TaskQueue.<>c__DisplayClass19_0.<.ctor>b__1() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.WPF\TaskQueue.cs: 行 59
```


> 安裝完 Docker on Windows後, 使用 Hyper-V (而非VirtualBox), 看似正常安裝了, 但是 Hyper-V裏頭, 卻沒有 `MobyLinuxVM`, *Virtual Switch Manager*裏頭, 也沒有 `DockerNAT`. 估計是這邊不曉得哪裡有問題, 因而 docker一直無法正常運作. 2018/05/21


## Issue

- [Security warning appearing when building a Docker image from Windows against a non-Windows Docker host](https://github.com/moby/moby/issues/20397)

> Build Image from Dockerfile之後, 會看到 `Successfully tagged mt:latestSECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.`. 這是因為 Windows裏頭, 並不存在 *executable*, 所以這些訊息都會經由 stdout 輸出, 並且無法透過設定將它關閉提醒(17.04版以前, 此為 stderr).



# Docker Machine

- [Microsoft Hyper-V](https://docs.docker.com/machine/drivers/hyper-v/)
- [Cannot start docker after installation on Windows](https://stackoverflow.com/questions/36885985/cannot-start-docker-after-installation-on-windows)
- [Install Hyper-V on Windows 10](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)
- [在 Windows 10 上安裝 Hyper-V](https://docs.microsoft.com/zh-tw/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)
- [Error with pre-create check: "Hyper-V PowerShell Module is not available" #4342](https://github.com/docker/machine/issues/4342)
- [Source Code - docker/machine/drivers/hyperv/powershell.go](https://github.com/docker/machine/blob/master/drivers/hyperv/powershell.go)
- [Windows 10 如何啟用 docker 功能](https://blog.yowko.com/2017/05/windows-10-docker.html)
- 2018/09/03 (still failed)

我自己的解法~

1. Win+R > `ncpa.cpl`
2. (選擇使用來上網的網卡), 右鍵 > 內容
3. (上面的)共用
4. `允許其他網路使用者透過這台電腦的網際網路連線來連線(N)`
5. (下拉式選單) 選擇 vEthernet(DockerNAT) **`有個重要的前提`**
6. prompt 訊息提示視窗, 按確定吧~

> 當網際網路連線共用啟用後, 您的LAN介面卡會被設定成使用IP位址 192.168.137.1 . 您的電腦可能會因此失去與網路上其他電腦的連線. 如果這些電腦擁有靜態IP位址的話, 您應該將它們設定成自動取得它們的IP位址. 您確定要啟用網際網路連線共用嗎?

5的前提 : Docker 虛擬機(MobyLinuxVM) 所用的 **虛擬交換器** 選擇的是 `DockerNAT`, 才可用上面的做法

恩... 結果還是不能用, 馬der again...

```powershell
# 使用 admin 開啟 powershell
> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
> Enable-WindowsOptionalFeature -Online -FeatureName containers -All


# 部署映像服務與管理工具
> DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V


# 查看 VM
> Get-VM

Name        State   CPUUsage(%) MemoryAssigned(M) Uptime           Status   Version
----        -----   ----------- ----------------- ------           ------   -------
MobyLinuxVM Running 0           2048              01:55:18.6470000 正常運作 8.3
os6         Off     0           0                 00:00:00         正常運作 8.3
os7         Off     0           0                 00:00:00         正常運作 8.3
u16         Off     0           0                 00:00:00         正常運作 8.3

# 查看虛擬交換器
> Get-VMSwitch

Name                 SwitchType NetAdapterInterfaceDescription
----                 ---------- ------------------------------
PrivateVirtualSwitch External   Intel(R) Ethernet Connection (7) I219-V
DockerNAT            Internal
預設切換             Internal   Teamed-Interface

# 建立 Docker-Machine
# 無法使用 Docker Machine 阿~~~docker-machine create --driver "hyperv" master
> docker-machine create --driver "hyperv" master
Running pre-create checks...
Error with pre-create check: "Hyper-V PowerShell Module is not available"
```



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



## 2018/09/04

不知道怎麼搞的... 原本 DockerMachine無法使用, 弄一弄後, 整個 Docker 又掛了...

MobyLinux 沒灌起來 caused by DockerNAT 沒安裝成功

```
Error response from daemon: open \\.\pipe\docker_engine_windows: The system cannot find the file specified.

   於 Docker.Backend.DockerDaemonChecker.Check(Func`1 isDaemonProcessStillRunning) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\DockerDaemonChecker.cs: 行 63
   於 Docker.Backend.ContainerEngine.Windows.DoStart(Settings settings, String daemonOptions) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\ContainerEngine\Windows.cs: 行 218
   於 Docker.Backend.ContainerEngine.Windows.Start(Settings settings, String daemonOptions) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\ContainerEngine\Windows.cs: 行 93
   於 Docker.Core.Pipe.NamedPipeServer.<>c__DisplayClass9_0.<Register>b__0(Object[] parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Core\pipe\NamedPipeServer.cs: 行 46
   於 Docker.Core.Pipe.NamedPipeServer.RunAction(String action, Object[] parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Core\pipe\NamedPipeServer.cs: 行 144
```



# 依然無法使用(此篇不值得參考)

## Problem - 安裝完 Docker 之後, 卻找不到 DockerNAT

- 2018/09/04
- [Create a virtual switch for Hyper-V virtual machines](https://docs.microsoft.com/zh-tw/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)

```powershell
### 1. 安裝完 Docker 之後, 應該要有 DockerNAT, 但卻沒有出現!!
> Get-VMSwitch

Name                 SwitchType NetAdapterInterfaceDescription
----                 ---------- ------------------------------
PrivateVirtualSwitch External   Intel(R) Ethernet Connection (7) I219-V
預設切換             Internal   Teamed-Interface
# DockerNAT            Internal                 ### <----- 應該要有, 卻沒有被安裝, 導致 Docker daemon 一直無法啟動...

### 2. 然後使用 Hyper-V 管理員, 手動新增 虛擬交換器時, 發生錯誤!
# 經查上述網址, 發現因為 「移除之前的虛擬交換器 + 重新建立」會發生 「之前的東西沒刪乾淨, 導致無法建立新的」, 依照網頁指示, 下載軟體排除問題後重開機
```



- [docker/labs/Setup-Windows10](https://github.com/docker/labs/blob/master/windows/windows-containers/Setup-Win10.md)
- [about_Execution_Policies](https://technet.microsoft.com/zh-TW/library/hh847748.aspx)

```powershell
# 前往這邊~~ 「C:\Program Files\Docker\Docker\resources」
> .\MobyLinux.ps1 -create -switchname DockerNAT
.\MobyLinux.ps1 : 因為這個系統上已停用指令碼執行，所以無法載入 C:\Program Files\Docker\Docker\resources\MobyLinux.ps1 檔案。如需詳細資訊，請參閱 about_Execution_Policies，網址為 https:/go.microsoft.com/fwlink/?LinkID=13517
0。
位於 線路:1 字元:1
+ .\MobyLinux.ps1 -create -switchname DockerNAT
+ ~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

# 目前的執行政策沒有被授權
> Get-ExecutionPolicy
Restricted

> Get-ExecutionPolicy -List

        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       Undefined

# 查詢 CurrentUser 的執行原則
> Get-ExecutionPolicy -Scope CurrentUser
Undefined

# 設定執行原則
# Set-ExecutionPolicy -ExecutionPolicy <PolicyName> -Scope <scope>
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

# 建立 DockerNAT
> powershell -ExecutionPolicy ByPass -File 'C:\Program Files\Docker\Docker\resources\MobyLinux.ps1' -create -switchname DockerNAT

# 移除執行原則
# Set-ExecutionPolicy  -ExecutionPolicy Undefined
> Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope LocalMachine
```



# Docker Machine on Windows 10 問題

- 2018/09/26
- [Docker Machine 問題](https://docs.docker.com/get-started/part4/#set-up-your-swarm)
- [Docker Machine 下載點](https://github.com/docker/machine/releases)

在 Windows 10 Powershell 輸入

```powershell
docker-machine create -d hyperv --hyperv-virtual-switch "ExternalSwitch" myvm1
# Docker Machine error: Hyper-V PowerShell Module is not available

docker-machine --version
# 0.14
```

之後發現應該(99%) 是 0.14 版的 Docker Machine 有 bug!! (今 2018/09/26, Docker Machine 最新版為 0.15)

解法:

1. 下載 `docker-machine-Windows-x86_64.exe`,  把下載的 `docker-machine-Windows-x86_64.exe` 重新命名成 `docker-machine.exe`, 貼到 `C:\Program Files\Docker\Docker\resources\bin` 覆蓋!!

2. 開啟 Hyper-V 管理員 > 虛擬交換器管理員 > 建立 Public 虛擬交換器, 隨便你開心取名字吧~ 我取名為 ExternalSwitch, 之後會暫時斷線... (電腦內網路架構會調整)

3. 以系統管理員身分啟用 powershell

```powershell
> docker-machine create -d hyperv --hyperv-virtual-switch "ExternalSwitch" myvm1
Running pre-create checks...
(myvm1) No default Boot2Docker ISO found locally, downloading the latest release...
(myvm1) Latest release for github.com/boot2docker/boot2docker is v18.06.1-ce
(myvm1) Downloading C:\Users\tony\.docker\machine\cache\boot2docker.iso from https://github.com/boot2docker/boot2docker/releases/download/v18.06.1-ce/boot2docker.iso...
(myvm1) 0%....10%....20%....30%....40%....50%....60%....70%....80%....90%....100%
Creating machine...
(myvm1) Copying C:\Users\tony\.docker\machine\cache\boot2docker.iso to C:\Users\tony\.docker\machine\machines\myvm1\boot2docker.iso...
(myvm1) Creating SSH key...
(myvm1) Creating VM...
(myvm1) Using switch "ExternalSwitch"
(myvm1) Creating VHD
(myvm1) Starting VM...
(myvm1) Waiting for host to start...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this virtual machine, run: C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe env myvm1
# 成功!!
# 上面的過程, 得執行好幾分鐘...
```

如此, Hyper-V 裏頭, 就會看到多出兩台 myvm1 及 myvm2 了~~

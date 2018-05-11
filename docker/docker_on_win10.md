# Docker on Windows 10
- 2018/05/11
- 18.03.1-ce
- [相關解法 - 找這個回覆 kleskowy commented on 17 Nov 2017](https://github.com/docker/for-win/issues/324)

不知道為什麼你他媽的一直灌不起來, 錯誤訊息也看不懂, 所以先記錄下來

```
Unable to create: 執行中的命令已停止，因為喜好設定變數 "ErrorActionPreference" 或一般參數設定為 Stop: Hyper-V 找不到名為 "DockerNAT" 的虛擬交換器。
位於 New-Switch，<無檔案>: 第 117 行
位於 <ScriptBlock>，<無檔案>: 第 394 行
   於 Docker.Core.Pipe.NamedPipeClient.Send(String action, Object[] parameters) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Core\pipe\NamedPipeClient.cs: 行 36
   於 Docker.Actions.DoStart(SynchronizationContext syncCtx, Boolean showWelcomeWindow, Boolean executeAfterStartCleanup) 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 67
   於 Docker.Actions.<>c__DisplayClass14_0.<Start>b__0() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.Windows\Actions.cs: 行 51
   於 Docker.WPF.TaskQueue.<>c__DisplayClass19_0.<.ctor>b__1() 於 C:\gopath\src\github.com\docker\pinata\win\src\Docker.WPF\TaskQueue.cs: 行 59
```

最後幾行的 Log file 長這樣
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

-----------------------------

> 辛苦的弄了半個小時, 其實我真的沒動到什麼, 只是用 `系統管理員權限` 去開啟 `Hyper-V` 及 `Docker`, 然後忘了在什麼條件底下, 原本 **虛擬交換器管理員** 只有一個「預設切換」, 但偶然間出現 「DockerNAT」, 重開後又消失了!! 然後 Docker就成功啟動了... (幹!!  沙小...).  只是 `Docker`啟動成功後, 在開啟 `Hyper-V`, 就看不到 「DockerNAT」了.
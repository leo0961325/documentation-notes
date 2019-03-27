# .Net Core

- 2019/01/28


## 版本

```sh
$# dotnet --version
2.2.101                 # 目前 netcore SDK 版本

$# dotnet --info
.NET Core SDK (反映任何 global.json):
 Version:   2.2.101     # 目前 netcore SDK 版本
 Commit:    236713b0b7

執行階段環境:
 OS Name:     Windows
 OS Version:  10.0.17134
 OS Platform: Windows
 RID:         win10-x64
 Base Path:   C:\Program Files\dotnet\sdk\2.2.101\

Host (useful for support):
  Version: 2.2.0        # 目前 netcore Runtime 版本
  Commit:  1249f08fed

.NET Core SDKs installed:
  2.1.103 [C:\Program Files\dotnet\sdk]     # 已安裝的 SDK 版本
  2.1.104 [C:\Program Files\dotnet\sdk]     # 已安裝的 SDK 版本
  2.1.201 [C:\Program Files\dotnet\sdk]     # 已安裝的 SDK 版本
  2.1.503 [C:\Program Files\dotnet\sdk]     # 已安裝的 SDK 版本
  2.2.101 [C:\Program Files\dotnet\sdk]     # 已安裝的 SDK 版本

.NET Core runtimes installed:
  Microsoft.AspNetCore.All 2.1.7 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.All]  # 已安裝的 Runtime 版本
  Microsoft.AspNetCore.All 2.2.0 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.All]  # 已安裝的 Runtime 版本
  Microsoft.AspNetCore.App 2.1.7 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]  # 已安裝的 Runtime 版本
  Microsoft.AspNetCore.App 2.2.0 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]  # 已安裝的 Runtime 版本
  Microsoft.NETCore.App 2.0.6 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]        # 已安裝的 Runtime 版本
  Microsoft.NETCore.App 2.0.7 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]        # 已安裝的 Runtime 版本
  Microsoft.NETCore.App 2.1.7 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]        # 已安裝的 Runtime 版本
  Microsoft.NETCore.App 2.2.0 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]        # 已安裝的 Runtime 版本

To install additional .NET Core runtimes or SDKs:
  https://aka.ms/dotnet-download
```

## 版本切換

- [netcore 版本](https://github.com/dotnet/core/blob/master/release-notes/download-archive.md)

```sh
# 已安裝的 SDK 版本
$# dotnet --list-sdks
2.1.103 [C:\Program Files\dotnet\sdk]
2.1.104 [C:\Program Files\dotnet\sdk]
2.1.201 [C:\Program Files\dotnet\sdk]
2.1.503 [C:\Program Files\dotnet\sdk]
2.2.101 [C:\Program Files\dotnet\sdk]

# 已安裝的 runtime 版本
$# dotnet --list-runtimes
Microsoft.AspNetCore.All 2.1.7 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.All]
Microsoft.AspNetCore.All 2.2.0 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.All]
Microsoft.AspNetCore.App 2.1.7 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]
Microsoft.AspNetCore.App 2.2.0 [C:\Program Files\dotnet\shared\Microsoft.AspNetCore.App]
Microsoft.NETCore.App 2.0.6 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.NETCore.App 2.0.7 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.NETCore.App 2.1.7 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]
Microsoft.NETCore.App 2.2.0 [C:\Program Files\dotnet\shared\Microsoft.NETCore.App]

# 打開 netcore 版本對照的網頁 https://github.com/dotnet/core/blob/master/release-notes/download-archive.md
$# dotnet new globaljson

$# type global.json
{
  "sdk": {
    "version": "2.2.101"    # <- 在這邊填入電腦內已安裝的 SDK 版本
  }
}
# 之後, 此資料夾以下的所有子資料夾, 都會套用此 SDK 版本, 日後執行時, 搭配 SDK <-> Runtime 對照來執行~

### 底下是 SDK 版本以及 Runtime 版本無法對照時發生的錯誤範例
$# dotnet run
C:\Program Files\dotnet\sdk\2.1.503\Sdks\Microsoft.NET.Sdk\targets\Microsoft.NET.TargetFrameworkInference.targets(137,5): error NETSDK1045: 目前的 .NET SDK 不支援以 .NET Core 2.2 作為目標。請以 .NET Core 2.1 或更低版本作為目標，或是使用支援 .NET Core 2.2 的 .NET SDK 版本 。 [D:\tmp\demo\demo.csproj]

建置失敗。請修正建置錯誤後再執行一次。

$# 
```


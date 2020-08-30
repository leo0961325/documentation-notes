# Network Namespace

- 2020/08/30

## 摘要

Linux 從 v2.4.19 開始納入 **namespace** 的概念 用來 *隔離核心資源*

- mount namespace   : 檔案系統掛載點 (since v2.4.19)
- UTS namespace     : 主機名
- IPC namespace     : POSIX 程序間通訊消息隊列
- PID namespace     : 程序 PID 空間
- user namespace    : User ID 空間 (since v3.8)
- network namespace : IP位址 (since v2.6) (此篇重點!)

    
## Network Namespace

- 用來隔離 系統設備 && IP Address, port, route table, firewall rules, ...
- 每個 namespace 都有自己的 `/proc/net/`
- 透過調用 Linux 的 `clone(CLONE
)` (UNIX `fork()` 的延伸) 來建立 namespace
# Systemd Journal

- 2018/08/15

CentOS7 使用雙軌並行來記錄 Log, `舊制 rsyslog` && `新制 journalctl`


## syslog protocol

syslog 為工業標準, 採用 3 個位元來記錄 Log 的 `優先等級 priority` (severity of the message). 此標準會記錄 facility(the type of message) 及 priority(the severity of the message)

Code | Priority | Severity
---- | -------- | -------------------------
000  | emerg    | 系統異常
001  | alert    | 必須要被立即處理的錯誤
010  | crit     | 危急情況
011  | err      | 非危急的錯誤
100  | warning  | 警告
101  | notice   | 正常情況的重大事件
110  | info     | 事件資訊
111  | debug    | Debug 資訊



# 1. rsyslog (CentOS7 以前)

```sh

```



# 2. journalctl (CentOS7 新)

```sh
# 印出 最近一次開機到現在的 Log
$ journalctl
# notice 或 warning 以上, 會用粗體標記
# error以上, 會用 紅底標記

# 顯示最新 87 筆
$ journalctl -n 87

# 顯示 error 以上的 Log
$ journalctl -p err

# 追蹤 最新 Log (類似tail -f)
$ journalctl -f
# 也可使用 「--since」, 「--until」 來限定時間區間

# 可以查看 特定 pid 的 Log
$ journalctl _PID=1182

# 特定 uid 的 Log
$ journalctl _UID=81

# 特定 service 的 Log
$ journalctl _SYSTEMD_UNIT="sshd.service"
```


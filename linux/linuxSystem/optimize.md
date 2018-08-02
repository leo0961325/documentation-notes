# 系統優化相關


## 關閉印表機服務
- 2018/07/31
- 我的筆電根本就沒有要用印表機阿XD... 白白浪費近2年的效能
- 但是把東西轉成 pdf 到底是不是透過這服務... 就不知道了

```sh
$ systemctl status cups
● cups.service - CUPS Printing Service
   Loaded: loaded (/usr/lib/systemd/system/cups.service; enabled; vendor preset: enabled)
   Active: active (running) since 二 2018-07-31 09:11:49 CST; 6h ago
 Main PID: 1392 (cupsd)
   CGroup: /system.slice/cups.service
           └─1392 /usr/sbin/cupsd -f

$# systemctl stop cups
Warning: Stopping cups.service, but it can still be activated by:
  cups.socket
  cups.path

$# systemctl disable cups
Removed symlink /etc/systemd/system/multi-user.target.wants/cups.path.
Removed symlink /etc/systemd/system/multi-user.target.wants/cups.service.
Removed symlink /etc/systemd/system/sockets.target.wants/cups.socket.
Removed symlink /etc/systemd/system/printer.target.wants/cups.service.

$ systemctl status cups
● cups.service - CUPS Printing Service
   Loaded: loaded (/usr/lib/systemd/system/cups.service; disabled; vendor preset: enabled)
   Active: inactive (dead) since 二 2018-07-31 15:21:47 CST; 2min 47s ago
 Main PID: 1392 (code=exited, status=0/SUCCESS)

 7月 31 09:11:49 tonynb systemd[1]: Started CUPS Printing Service.
 7月 31 09:11:49 tonynb systemd[1]: Starting CUPS Printing Service...
 7月 31 15:21:47 tonynb systemd[1]: Stopping CUPS Printing Service...
 7月 31 15:21:47 tonynb systemd[1]: Stopped CUPS Printing Service.
```


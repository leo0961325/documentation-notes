# 開機相關


```sh
# 開機載入程序
$ /etc/rc.d/rc.local  # or /etc/rc.local

# 重新啟動系統登錄檔(os6)
$ /etc/init.d/rsyslogd restart
```


### note
`/etc/init.d/*` 這舊時代的 `systemV` 已經被新一代的 `systemd` 取代了
# Linux 系統時間

- 2018/08/18



## date

```sh
$ date
Mon Jul 23 21:34:56 CST 2018

$ date +%F
2018-07-23

$ date +%R
21:35
```


## timedatectl

系統開機時, 會去抓取 RTC(local hardware clock), 但硬體時間不准阿~ 所以通常會啟動 `chronyd` 來與 NTP Server 作時間校正, 但如果在封閉網路內的話(連不出去@@), 則需要到設定檔 `/etc/chrony.conf` 更改時間校正的 Server IP

```sh
$ timedatectl
      Local time: Wed 2018-08-15 18:54:33 CST   # 目前時區 時間
  Universal time: Wed 2018-08-15 10:54:33 UTC   # UTC 時間
        RTC time: Wed 2018-08-15 10:54:33       # 硬體時間
       Time zone: Asia/Taipei (CST, +0800)      # 洲別(大洋別)/首都
     NTP enabled: yes       # NTP 時間校正服務
NTP synchronized: no
 RTC in local TZ: no        # local hardware clock(RTC)
      DST active: n/a       # 日光節約時間
# Linux 關機時, 會把 UTC Time 寫入硬體時間
# Microsoft 開機時, 抓取的時間都是抓 BIOS 的 Local Time

# 更改 timezone -> America/New_York
$ timedatectl set-timezone America/New_York

$ $ timedatectl
      Local time: Wed 2018-08-15 07:00:00 EDT
  Universal time: Wed 2018-08-15 11:00:00 UTC
        RTC time: Wed 2018-08-15 11:00:00
       Time zone: America/New_York (EDT, -0400)
     NTP enabled: yes
NTP synchronized: yes
 RTC in local TZ: no
      DST active: yes
 Last DST change: DST began at
                  Sun 2018-03-11 01:59:59 EST
                  Sun 2018-03-11 03:00:00 EDT
 Next DST change: DST ends (the clock jumps one hour backwards) at
                  Sun 2018-11-04 01:59:59 EDT
                  Sun 2018-11-04 01:00:00 EST

$ timedatectl list-timezones  # 看所有時區
Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
Africa/Algiers
#...425個時區@@

# 更改時間
$ timedatectl set-time 09:00:00
```


## tzselect - 可互動式來設定時區

```sh
$ tzselect
```



# chronyd

早期使用 `nptd` 及 `nptq` 作時間校正, OS7 改用 `chronyd`

```sh
# 校時服務
$ systemctl status chronyd

# (不會看...)
$ chronyc sources -v
210 Number of sources = 2

  .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current synced, '+' = combined , '-' = not combined,
| /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^* 103-18-128-60.ip.mwsrv.c>     2   9   377   254   +109us[ +120us] +/-   34ms
^? t1.time.sg3.yahoo.com         0   6     0     -     +0ns[   +0ns] +/-    0ns
# 上面倒數第二行的「*」是目前時間校時鎖定的 Server

# 把系統時間寫入到 BIOS
$ sudo hwclock -w
```
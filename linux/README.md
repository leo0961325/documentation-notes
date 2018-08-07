# CentOS 7.x

安裝的 ISO 說明: 自從 CentOS7 開始, `版本命名依據` 就跟 `發表日` 有關
    「CentOS-7-x86_64-Everything-1503-01.iso」
    CentOS-7 表示 7.x版
    x86_64 為 64位原
    Everything 為 包山包海的版本
    1503 表示此版本在 2015/03 發表
    01.iso 為 CentOS7.1版

```sh
# 我的電腦環境
$ uname -a
Linux tonynb 3.10.0-514.el7.x86_64 #1 SMP Tue Nov 22 16:42:41 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

$ hostnamectl
   Static hostname: tonynb
         Icon name: computer-laptop
           Chassis: laptop
        Machine ID: 6e935c5d22124158bd0a6ebf9e086b24
           Boot ID: 3262e51d23a9478dbc268f562556a74c
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-514.el7.x86_64
      Architecture: x86-64

$ cat /etc/centos-release
CentOS Linux release 7.3.1611 (Core)

$ rpm --query centos-release
centos-release-7-3.1611.el7.centos.x86_64
```



# 主要目錄
Linux各大 dictribution 都有自己的 `文件存放位置`, 但幾乎都遵照 `Filesystem Hierarchy Standard (FHS)`, 重點在於規範 `每個特定的目錄下應該要放置什麼樣子的資料`

.        | Non-SysAdmin Usable            | SysAdmin Use Only
-------- | ------------------------------ | ---------------
static   | /usr <br> /opt                 | /etc <br> /boot
variable | /var/mail <br> /var/spool/news | /var/run <br> /var/lock

```sh
/bin/                                 # 可執行檔; (os7後, 連結至 /usr/bin/)
/boot/                                # 開機時使用的核心檔案目錄.
     /grub2/                                # 開機設定檔相關
/dev/                                 # 系統設備目錄
    /hda/                                   # IDE硬碟
    /sd1/                                   # SCSI硬碟
    /cdrom/                                 # 光碟機
    /fd0/                                   # 軟碟機
    /lp0/                                   # 印表機
/etc/                                 # 系統設定檔. ex: inittab, resolv.conf, fstab, rc.d
    /crontab                                # 排程工作
    /default/                               # 
        useradd                                 # 使用 useradd後, 預設的 新使用者 建立相關初始設定
    /fstab                                  # mount設定檔 (開機時 會依照此設定來作自動掛載; 每次使用 mount時, 預設也會動態更新此檔案)
    /hosts                                  # ip與 dns對照
    /init.d/                                # (CentOS6前, 所有的 服務啟動腳本) CentOS7仍在(但已經不使用 init 來管理服務了), 只剩部分東西還在這 (連結至 rc.d/init.d)
        netconsole                              # 各種模式下的 *netconsole 連結
        network                                 # 各種模式下的 *network 連結至此
    /inittab                                # (舊有的 xwindow服務, os7以後, 已經被 ooo.target 所取代)
    /issue                                  # 查看進站歡迎訊息(自己看得爽而已)
    /locale.conf                            # 系統預設語系定義檔 (一開始安裝就決定了!)
    /localtime/                             # 系統時間
    /login.defs                             # 建立使用者時, 該使用者的 系統愈設初始值
    /opt/                                   # 第三方協作軟體 /opt/ 的相關設定檔
    /passwd                                 # id 與 使用者帳號(User ID, UID) && 群組(Group ID, GID) 資訊
    /rc.d/                                  # 各種執行等級的啟動腳本
        /init.d/                                # 
            netconsole                              # 各種模式下的 *netconsole 連結至此
            network                                 # 各種模式下的 *network 連結至此
        /rc1.d/                                 # 單人維護模式
        /rc3.d/                                 # 純文字模式
        /rc5.d/                                 # 文字+圖形介面
            K50netconsole                           # (連結至 ../init.d/netconsole)
            S10network                              # (連結至 ../init.d/network)
    /resolv.conf                            # DNS 主機 IP 的設定檔
    /services                               # 服務 與 port 對映檔
    /skel/                                  # 預設建立使用者後, 使用者家目錄底下的東西
    /systemd/                               # 軟體的啟動腳本
        /system/                                # 依據系統所要提供的功能所撰寫的 服務腳本, 優先於 /run/systemd/system/ 及 /usr/lib/systemd/system/
    /sysconfig/
        /network-scripts/                       # CentOS 的網路設定資料放在這~
/home/                                      # 家目錄
/lib/                                 # 系統的共用函式庫檔案 (連結至 /usr/lib/)
    /modules/                               # 可抽換式的核心相關模組(驅動程式); 不同版本的核心模組
/media/                               # 移動式磁碟or光碟 掛載目錄 (可移除的裝置)
/mnt/                                 # "暫時性" 檔案系統 掛載目錄; 現在許多裝置都移到 /media/ 了, 所以暫時的, 依舊放這
/opt/                                 # 非 Linux預設安裝的外來軟體 (第三方協作軟體)
/proc/                                # 虛擬檔案系統(virtual filesystem), 東西都存在於 memory, 不占用 disk; 行程資訊目錄
/run/                                 # 系統開機後所產生的各項資訊 (可用記憶體來模擬); 某些服務or程式啟動後, 他們的 pid 會放在這.
    /lock/                                  # 某些裝置或檔案, 一次只能一人使用, 使用中會上鎖.
    /systemd/                               # 
        /system/                                # 系統執行過程中所產生的 服務腳本, 此內腳本優先於 /usr/lib/systemd/system/
/sbin/                                # 系統管理員 用的 工具or指令or執行檔; (連結至 /usr/sbin/)
/srv/                                 # 網路服務的一些東西 (如果不打算提供給外部網路存取的話, 建議放在 /var/lib/ )
/sys/                                 # 虛擬檔案系統(virtual filesystem), 東西都存在於 memory, 不占用 disk; 紀錄核心與系統硬體資訊
/tmp/                                 # 重開機後會清除
/usr/                                 # (unix software resource) Linux系統安裝過程中必要的 packages (軟體安裝/執行相關); 系統剛裝完, 這裡最占空間
    /bin/                                   # 一般使用者 用的 工具or指令or執行檔; 
    /games/                                 # 與遊戲相關
    /include/                               # c++ 的 header 與 include 放置處; 使用 tarball 方式安裝軟體時, 會用到裡面超多東西
    /lib/                                   # 系統的共用函式庫檔案
        /locale/                                # 存放語系檔
        /systemd/                               # 
            /system/                                # 每個服務最主要的 啟動腳本設定 , 類似CentOS6前的 /etc/init.d 底下的東西
    /libexec/                               # 大部分的 X window 的操作指令都放這. (不被使用這慣用的執行檔or腳本)
    /local/                                 # sys admin 在本機自行安裝的軟體, 建議放這邊
          /sbin/                                # 本機自行安裝的軟體所產生的系統執行檔(system binary), ex: fdisk, fsck, ifconfig, mkfs 等
    /sbin/                                  # 系統專用的 工具/指令/執行檔, ex: 某些伺服器軟體程式的東西
    /share/                                 # 唯讀架構的資料檔案; 共享文件; 幾乎都是文字檔
          /doc                                  # 系統文件
          /man                                  # 線上操作手冊
          /zoneinfo                             # 時區檔案
    /src/                                   # 一般原始碼 建議放這
        /linux/                                 # 核心原始碼 建議放這
/var/                                 # 登錄檔, 程序檔案, MySQL資料庫檔案, ... (與系統運作過程有關); 系統開始運作後, 這會慢慢變大;
    /cache/                                 # 系統運作過程的快取
    /log/                                   # 登入檔放置的目錄. 比較重要的有: /var/log/messages, /var/log/wtmp (紀錄登入者資訊)
        /dmesg                                  # 開機時偵測硬體與啟動服務的紀錄
        /messages                               # 開機紀錄
        /secure                                 # 安全紀錄
    /lib/                                   # 程式運作過程所需用到的 資料檔案 放置的目錄. ex: MySQL DB 放在 /var/lib/mysql/; rpm DB 放在 /var/lib/rpm/
        /mysql/                                 # mysql資料庫的資料儲存位置
    /mail/                                  # 個人電子郵件信箱的目錄. 這目錄也被放置到 /var/spool/mail/, 與之互為連結
    /lock/                                  # 某些裝置或檔案, 一次只能一人使用, 使用中會上鎖. (連結至 /run/lock/)
    /run/                                   # 早期 系統開機後所產生的各項資訊. (連結至 /run/)
    /spool/                                 # 通常用來放 佇列(排隊等待其他程式來使用)資料(理解成 快取目錄). ex: 系統收到新信, 會放到 /var/spool/mail/ , 但使用者收下信件後, 會從此刪除
          /cron/                                # 工作排成資料
          /mail/                                # 所有使用者的 信件資料夾集中處 ; 系通收到新信, 會放到這; 等待寄出的 email
          /mqueue/                              # 信件寄不出去, 會塞到這
          /news/                                # 新聞群組
```


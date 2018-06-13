# Linux 目錄配置 與 目錄管理 
- 2018/05/27

## 主要目錄
Linux各大 dictribution都有自己的文件存放位置, 但幾乎都遵照 `Filesystem Hierarchy Standard (FHS)` 的標準在走, FHS 重點在於規範 `每個特定的目錄下應該要放置什麼樣子的資料`, 他只規範了 3 類, 分別是「/」、「/usr」、「/var」

.        | sharable                       | unsharable
-------- | ------------------------------ | ---------------
static   | /usr <br> /opt                 | /etc <br> /boot
variable | /var/mail <br> /var/spool/news | /var/run <br> /var/lock

```sh
/                                     # 與開機系統有關
/bin/                                 # 可執行檔; (os7後, 連結至 /usr/bin/)
/boot/                                # 開機時使用的核心檔案目錄.
/boot/grub2/                                  # 開機設定檔相關
/dev/                                 # 系統設備目錄
/dev/hda/                                     # IDE硬碟
/dev/sd1/                                     # SCSI硬碟
/dev/cdrom/                                   # 光碟機
/dev/fd0/                                     # 軟碟機
/dev/lp0/                                     # 印表機
/etc/                                 # 系統設定檔. ex: inittab, resolv.conf, fstab, rc.d
/etc/crontab                                  # 排程工作
/etc/hosts                                    # ip與 dns對照
/etc/init.d/                                  # CentOS6(含)以前, 所有的服務啟動腳本都在這
/etc/localtime/                               # 系統時間
/etc/inittab                                  # (舊有的 xwindow服務, os7以後, 已經被 ooo.target 所取代)
/etc/opt/                                     # 第三方協作軟體 /opt/ 的相關設定檔
/etc/systemd/                                 # 軟體的啟動腳本
/etc/sysconfig/network-scripts/                       # CentOS 的網路設定資料放在這~
/home/                                        # 家目錄
/lib/                                 # 系統的共用函式庫檔案 (連結至 /usr/lib/)
/lib/modules/                                 # 可抽換式的核心相關模組(驅動程式); 不同版本的核心模組
/media/                               # 移動式磁碟or光碟 掛載目錄 (可移除的裝置)
/mnt/                                 # "暫時性" 檔案系統 掛載目錄; 現在許多裝置都移到 /media/ 了, 所以暫時的, 依舊放這
/opt/                                 # 非 Linux預設安裝的外來軟體 (第三方協作軟體)
/proc/                                # 虛擬檔案系統(virtual filesystem), 東西都存在於 memory, 不占用 disk; 行程資訊目錄
/run/                                 # 系統開機後所產生的各項資訊 (可用記憶體來模擬); 某些服務or程式啟動後, 他們的 pid 會放在這.
/run/lock/                                    # 某些裝置或檔案, 一次只能一人使用, 使用中會上鎖.
/sbin/                                # 系統管理員 用的 工具or指令or執行檔; (連結至 /usr/sbin/)
/srv/                                 # 網路服務的一些東西 (如果不打算提供給外部網路存取的話, 建議放在 /var/lib/ )
/sys/                                 # 虛擬檔案系統(virtual filesystem), 東西都存在於 memory, 不占用 disk; 紀錄核心與系統硬體資訊
/tmp/                                 # 重開機後會清除
/usr/                                 # (unix software resource) Linux系統安裝過程中必要的 packages (軟體安裝/執行相關); 系統剛裝完, 這裡最占空間
/usr/bin/                                     # 一般使用者 用的 工具or指令or執行檔; 
/usr/games/                                   # 與遊戲相關
/usr/include/                                 # c++ 的 header 與 include 放置處; 使用 tarball 方式安裝軟體時, 會用到裡面超多東西
/usr/lib/                                     # 系統的共用函式庫檔案
/usr/libexec/                                 # 大部分的 X window 的操作指令都放這. (不被使用這慣用的執行檔or腳本)
/usr/local/                                   # sys admin 在畚箕自行安裝的軟體, 建議放這邊
/usr/local/sbin/                                      # 畚箕自行安裝的軟體所產生的系統執行檔(system binary), ex: fdisk, fsck, ifconfig, mkfs 等
/usr/sbin/                                    # 系統專用的 工具/指令/執行檔, ex: 某些伺服器軟體程式的東西
/usr/share/                                   # 唯讀架構的資料檔案; 共享文件; 幾乎都是文字檔
/usr/share/doc                                        # 系統文件
/usr/share/man                                        # 線上操作手冊
/usr/share/zoneinfo                                   # 時區檔案
/usr/src/                                     # 一般原始碼 建議放這.
/usr/src/linux/                                       # 核心原始碼 建議放這
/var/                                 # 登錄檔, 程序檔案, MySQL資料庫檔案, ... (與系統運作過程有關); 系統開始運作後, 這會慢慢變大;
/var/cache/                                   # 系統運作過程的快取
/var/log/                                     # 登入檔放置的目錄. 比較重要的有: /var/log/messages, /var/log/wtmp (紀錄登入者資訊)
/var/log/dmesg                                        # 開機時偵測硬體與啟動服務的紀錄
/var/log/messages                                     # 開機紀錄
/var/log/secure                                       # 安全紀錄
/var/lib/                                     # 程式運作過程所需用到的 資料檔案 放置的目錄. ex: MySQL DB 放在 /var/lib/mysql/; rpm DB 放在 /var/lib/rpm/
/var/lib/mysql/                                       # mysql資料庫的資料儲存位置
/var/mail/                                    # 個人電子郵件信箱的目錄. 這目錄也被放置到 /var/spool/mail/, 與之互為連結
/var/lock/                                    # 某些裝置或檔案, 一次只能一人使用, 使用中會上鎖. (連結至 /run/lock/)
/var/run/                                     # 早期 系統開機後所產生的各項資訊. (連結至 /run/)
/var/spool/                                   # 通常用來放 佇列(排隊等待其他程式來使用)資料(理解成 快取目錄). ex: 系統收到新信, 會放到 /var/spool/mail/ , 但使用者收下信件後, 會從此刪除
/var/spool/cron/                                      # 工作排成資料
/var/spool/mail/                                      # 系通收到新信, 會放到這; 等待寄出的 email
/var/spool/mqueue/                                    # 信件寄不出去, 會塞到這
/var/spool/news/                                      # 新聞群組
```


# [Quickstart](https://www.zabbix.com/documentation/4.0/manual/quickstart)

- 2019/07/24
- v4.0


# 1. Login and configuration user

Overview: 如何增加 Zabbix user

- user: Admin (`Zabbix administrators`)
- password: zabbix

Zabbix administrators 群組的 Users, 可以在最上頭的 Tabs 看到 `Configuration` 及 `Administration`

## 新增使用者

Administration > Users > Create user > (輸入使用者資訊)

之後會看到多了個 Users, 底下有 3 個 Tab:

- User: 個人基本資訊(密碼, 所屬群組, Theme(暗黑風格唷), 語系...)
- Media: 報警方式(Email, SMS, ...) 及 Log-Level
- Permissions: 可選擇目前 User 的 *User type* (預設: 使用者建立後, has no permissions to access hosts)
    - 須前往 Users 裏頭, 點選 Groups 欄位裡的值(會跳到 User groups). 點選 Permissions Tab > Select (接著, 挑選這個使用者可以監控(Read-only) 的 Host groups)

後續就可以用這個使用者來做登入 && 監控


# 2. New host

Overview: 如何增加 被監控端. 任何的 physical server, network switch, VM, app 都可以是 被監控端.

Configuration > Hosts

這頁可以定義 被監控端 有哪些, 預設會有一個 **Zabbix server**(也就是 監控端本身, 預設定義了監控自己). 它的 Availability 出現 `紅色的 ZBX`(無法監控), 後續再說...

Configuration > Hosts > Create host > (輸入被監控端)

底下有很多個 Tab (這邊只講 Host, 其他的我不懂):

- Host:
  - Host name: 系統辨識用的 host
  - Visible name: 使用者看的 host name
  - Groups: 這個被監控端, 所屬的群組
  - Agent interfaces: 被監控端 的位址 (被監控端需要安裝 zabbix-agent)
  - (其他略)


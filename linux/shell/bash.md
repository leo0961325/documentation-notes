# bash

```sh
# 看前3行
$ $ cat /etc/passwd | head -3
root:x:0:0:root:/root:/bin/bash             # 使用 root 登入後, 是使用 /bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin     # daemon 這系統帳號, 使用的是 /sbin/nologin來作操作
```

# 快速命令

```sh
# 為指令設定別名 (只作用於目前 session)
$ alias lla='ls -al'
```

# 不知道怎麼分類的零碎範例...
```sh
# 查詢指令是否為 bash shell 的內建命令
$ type lla
lla is aliased to 'ls -al'

$ type cd
cd is a shell builtin
```

```sh
# bash 指令換行, 使用「 \」
$# ls /home/tony \
>   /var \
>   /etc
# (熱鍵)若使用換行後, 發現後續的行數輸入一堆錯誤的東西, 從指標處
# Ctrl + u : 刪除此行指標前的所有字
# Ctrl + k : 刪除此行指標後的所有字
```

```sh
$ echo $USER
tony

$ mail              # 使用 mail 來收信
No mail for tony

$ ls /var/spool/mail    # 依照不同使用者, 指向不同檔案
root  rpc  tony  tony2

$ echo $MAIL        # 收信的檔案路徑變數
/var/spool/mail/tony
```

# 變數
- export:  自訂變數 -> 環境變數
- declare: 環境變數 -> 自訂變數

呼叫變數
```sh
# 取用變數, 底下兩者效果相同 ${varialbe}, $variable, 但是建議用 ${variable}
$ echo $PATH
$ echo ${PATH}  # 較佳!!

$ var=foo
$ echo $varbar
                # 沒東西
$ echo ${var}bar
foobar
```

引號
```sh
# 設定變數前後, 不能加「 」, 如果要用的畫, 得用 "" 或 '' 框起來
$ var="lang is ${LANG}"       # 雙引號內, 可使用變數
$ echo ${var}
lang is zh_TW.UTF-8

$ var='lang is ${LANG}'       # 單引號內, 把變數是為純字串
$ echo ${var}
lang is ${LANG}

$ var="lang is ""$LANG"       # 這寫法很爛, 超難讀懂
$ echo ${var}
lang is zh_TW.UTF-8
```

跳脫字元 \
```sh
$ var=tony\ chou            # 如果硬是不要用引號, 然後硬要用「 」
$ echo ${var}
tony chou
```

反單引號 `
```sh
# 下面兩者相同  $(xxx) = `xxx`
$ v1=$(uname -r)
$ echo ${v1}
3.10.0-693.21.1.el7.x86_64

$ v2=`uname -r`
$ echo ${v2}
3.10.0-693.21.1.el7.x86_64
```

系統變數
```sh
# 通常大寫字元 為 系統變數~ ex:
$ echo $HOME
$ echo $PATH
```

export: 讓 自訂變數 -> 環境變數 (子程序就能用到了~~)
```sh
$ vv=87
$ echo ${vv}
87
$ bash          # 近入子程序
$ echo ${vv}

$ exit          # 離開子程序
exit
$ export vv
$ bash          # 近入子程序
$ echo ${vv}
87
```

取消變數
```sh
$ echo ${v2}
3.10.0-693.21.1.el7.x86_64
$ unset v2
$ echo ${v2}
                            # 沒東西了~
```

查看 環境變數
```sh
$ env                   # 可看到所有的 環境變數
HOSTNAME=tonynb
SELINUX_ROLE_REQUESTED=
TERM=xterm
SHELL=/bin/bash
HISTSIZE=1000
...(略)... 約 30 個

$ export                # 可看到所有的 環境變數 (還有額外功能)
declare -x HISTCONTROL="ignoredups"
declare -x HISTSIZE="1000"
declare -x HOME="/home/tony"
declare -x HOSTNAME="tonynb"
declare -x LANG="zh_TW.UTF-8"
...(略)... 約 30 個
```

隨機亂數
```sh
# 產生 [0, 32767] 之間的亂數
$ echo ${RANDOM}
14852

# declare: 讓 環境變數 -> 自訂變數
# 如果要產生 [0,9]勒? 得自己組合, 然後把變數丟給 「用數學處理後的容器」
$ declare -i rand=${RANDOM}*10/32768; echo ${rand}
8
```


# PS1 變數

```sh
[tony@tonynb dev]$ set | grep PS1
PS1='[\u@\h \W]\$ '

[tony@tonynb dev]$ echo ${PS1}
[\u@\h \W]\$                ## 預設的 PS 顯示格式, 玩壞了再從這改回去

[tony@tonynb dev]$
  ↑    ↑      ↑
  \u   \h     \W
# 顯示格式的概念啦@@

[tony@tonynb dev]$ echo ${PS2}
>
```

因為有太多太多了... 可去 `man bash` 搜尋 `PS1` 或 `看鳥哥`

節錄部分...

symbolic | Description
-- | -------------------
\h | 第一個小數點前的`主機名稱`
\@ | 顯示時間, 格式為 am/pm
\u | 使用者帳號
\w | 完整工作名稱
\W | 最相近的目錄名稱 (用 basename 函數算出來的)
\t | 24小時格式的時間 HH:MM:SS
\\$ | root為 # ; 否則為 $

自己玩 PS1
```sh
# 如果想要看起來是這樣 「<<(使用者帳號)@我最強 (時間)>>$ 」
[tony@tonynb home]$ PS1='<<\u@我最強 \t>>'
<<tony@我最強 22:29:11>>$               # 之後就會變成這樣了@@
```

## 查看目前的程序 「$」變數
```sh
$ ps
  PID TTY          TIME CMD
24031 pts/0    00:00:00 bash
31492 pts/0    00:00:00 ps

# 查看目前的程序
$ echo ${$}
24031               # 此即為 程序識別碼 或稱為 PID (Process ID)
```

## 「?」 變數

「?」 代表上次執行完後回傳的值, 若上次指令結束時`沒有出錯`, 則 `?` 為 0 ; 否則會是 > 0 的值

```sh
$ echo ${HOME}
$ echo ${?}
0               # 上次指令語法無誤

$ 12name=tony
$ echo ${?}
127             # 上次指令有錯
```



# 其他

~/`.bash_history` : 前一次登入以前所執行過的指令 ; 此次登入時執行的指令會愈存在 memory, 登出時會寫入此檔案

```sh
# 列出所有 環境變數 + 與bash操作介面有關的變數 + 使用者自定義的變數
$ set
(會跑出超多超多超多~~~變數)
```
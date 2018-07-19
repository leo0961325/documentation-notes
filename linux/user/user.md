# 帳戶管理 與 ACL權限
- 2018/07/16
- 每個檔案都有 `擁有人(User ID, UID)` && `擁有群組(User Group, GID)`
- `UID 與 帳號 對映檔` 放在 `/etc/passwd`
- `GID` 放在 `/etc/group`
- Linux 不會認識帳號, 而是透過 `/etc/passwd` 找到 `帳號` 對映的 `UID`


# User ID && 使用者帳號 && /etc/passwd

```sh
$ id tony
uid=1000(tony) gid=1000(tony) groups=1000(tony),10(wheel),983(docker),1002(shared)

$ ll -d /home/tony
drwx--x---+ 33 tony tony 4096  7月 16 22:47 /home/tony      # 比較這邊

$ $ cat /etc/passwd | grep tony
tony:x:1000:1000:tony:/home/tony:/bin/bash
# 上面有 7 個欄位 (由 6 個「:」分隔), 分別為 
# 1 tony         -> 使用者帳號名稱
# 2 x            -> 密碼(加密存於 /etc/shadow) (Linux 早期把密碼放這)
# 3 1000         -> 使用者帳號 對映的 UID
# 4 1000         -> 使用者帳號 對映的 GID
# 5 tony         -> 使用者 資訊欄位說明 (鳥哥說這欄不是很重要), ((後續關鍵字 finger , chfn ))
# 6 /home/tony   -> 登入後, 進入的 家目錄
# 7 /bin/bash    -> 登入後, 取得的 shell 位置

# 假如沒事亂改上面的第三欄的 1000 為 2000
$ ll -d /home/tony
drwx--x---+ 33 1000     # 比較這邊
#                ↑ 應該是 superblock 還什麼鬼的依然指向 第三欄的 UID 1000 吧!!  會導致之後的 tony 近不了 /home/tony
```

上述的第三欄 `UID`:
- 0 : 系統管理員 (一般使用者把這改為 0, 利碼晉級 Linux 之神)
- 1~999 : 系統帳號 (通常是安裝軟體後產生的)
    - 1~200 : 由 Linux Distribution 自行產生
    - 200~999 : 一般使用者 晉級 系統帳號 && 安裝軟體 的範圍 (我到底在寫什麼...)
- 1000~非常大的數字 : 一般使用者



# Group ID && 使用者群組 && /etc/group
```sh
$ cat /etc/group | grep tony
wheel:x:10:tony,tony2
tony:x:1000:tony                # tony
docker:x:983:tony
tony2:x:1001:                   # tony2
shared:x:1002:tony2,tony        # 之前作的 共享目錄
# 有 4 個欄位, 3 個「:」分隔
# 1 群組名稱
# 2 群組密碼 , 放在 /etc/gshadow
# 3 GID
# 4 此群組底下的弟兄們, 使用「,」分隔

$ 

```



# 登入過程
1. 尋找 `/etc/passwd` 是否有此帳號, 找出 `UID`
2. 依照剛找到的帳號, 前往 `/etc/group` 尋找 `GID`
3. 前往 `/etc/shadow`, 依照 `帳號`(還是 `UID`) 及 `輸入的密碼`, 與此 家密後的密碼 作 @^#%"^&... 換算 && 比對


```sh
$ ll /etc/passwd
-rw-r--r--. 1 root root 2541  7月 16 23:08 /etc/passwd

$ ll /etc/shadow
----------. 1 root root 1483  7月 14 15:41 /etc/shadow
# ↑ Ubuntu 16.04 為 -rw-r-----

$# cat /etc/shadow | grep -n 3
root:%*ht^6...(PASS)...msW02/::0:99999:7:::
bin:*:17110:0:99999:7:::
daemon:*:17110:0:99999:7:::
# 上面有 8 個 「:」, 9個欄位分別為
# 1 使用者帳號
# 2 很厲害的加密加密之後讓人看不懂的密碼
# 3 最近更動密碼的日期, start from 1970/1/1, 過一天 +1, (GOOGLE Linux date 累積總秒數)
# 4 密碼不可被更動的日數
# 5 密碼需要重新變更的天數
# 6 密碼需要變更期限前的警告天數
# 7 密碼過期後的寬限時間(過了就失效了)
# 8 帳號失效日
# 9 (目前沒用到)


```



# root 密碼忘記了@@?
- 有救!

重開機進入 `單人維護模式` (會取得約當於 root 權限的 shell), 再使用 `passwd` 修改密碼

or 

`用光碟開機` 掛載到 / , 把 /etc/shadow 的 root 密碼欄位清空, 重開機後再改密碼

```sh
$ $ authconfig --test | grep hashing
 password hashing algorithm is sha512       # 目前密碼的加密機制
```
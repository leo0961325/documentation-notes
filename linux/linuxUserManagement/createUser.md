# 純文字介面, 建立使用者相關...
- 2018/07/14



# 建立使用者 && 群組

<font color="red">建議</font> : 使用 `groupadd` 時, 明確指定 `-g` "group id" . <br> 因為新增使用者 `useradd` 時, 預設都會新增一個同名的 "group id" 當成它預設的 "primary group" (可能將來會導致 「uid number != gid number」~~~ 讓人看不爽阿 ~~~)

```sh
# 建立使用者群組
$# groupadd <新建立的使用者群組>

# 把 使用者 -> 使用者群組
$# useradd -G <使用者群組> <新使用者帳戶>
$# usermod -aG <使用者群組> <已經存在的使用者帳戶>

# 設定 使用者 密碼
$# echo "<密碼>" | passwd --stdin <使用者帳戶>

# 查看 使用者 已經加入到那些 使用者群組
$# groups <使用者帳戶>
```



# 建立 共享資料夾 共享目錄
- [SUID/SGID/SBIT 權限](http://linux.vbird.org/linux_basic/0220filemanager.php#suid)
```sh
# 建立要共享的資料夾
$# mkdir /home/shared

# 改變這個資料夾的使用者群組
$# chgrp <使用者群組> /home/shared

# 設定目錄具有 SGID的權限
$# chmod 2770 /home/shared

$# ll -d /home/shared
```


```sh
# 快速新增使用者 && 設定同名密碼
$# uu=smartTony
$# useradd ${uu} ; echo ${uu} | passwd --stdin ${uu}
```
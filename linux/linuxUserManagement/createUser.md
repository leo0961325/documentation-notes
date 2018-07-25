# 純文字介面, 建立使用者相關...
- 2018/07/14



# 建立使用者 && 群組
```sh
# 建立使用者群組
$# groupadd <新建立的使用者群組>

# 把 使用者 -> 使用者群組

$# useradd -G <使用者群組> <新使用者帳戶>
# -g xxx : 初始群組 為 xxx
# -G xxx : 次要群組 為 xxx
# -u xxx : 手動分配 UID xxx 給該使用者
# -e xxx : 指定帳號失效日 xxx
# -f xxx : 密碼到期期限 為 xxx (重設密碼), 0:立即失效 ; -1:永遠不會失效
# -M : 告訴系統, 建立使用者就好了, 不用幫他建立 家目錄
# -r : 讓這個變成系統帳號

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


# 刪除使用者

```sh
$# userdel <使用者帳號>
```
# 安全性相關
- 2018/06/09


# 檔案隱藏屬性 (我用 特殊屬性 來理解它...)

> 隱藏屬性對於 Linux 來說, 只能在 Ext2/Ext3/Ext4 中完整生效, 像是 CentOS7預設使用的 xfs, 僅有部分支援
- [鳥哥 chattr](http://linux.vbird.org/linux_basic/0220filemanager.php#chattr)


```sh
$ touch qq
$ sudo chattr +i qq
$ rm qq
rm: 無法移除 'qq': 此項操作並不被允許

$ lsattr
----i----------- ./qq
```

最常用到的有 
1. `chattr +a` 檔案 無法作 append 以外的事情, 且無法被刪除; 
2. `chattr +i` 檔案 無法被 刪除, 更名, 設定連結, 等等操作



# 特殊權限 SUID, SGID, SBIT
- [鳥哥-特殊權限](http://linux.vbird.org/linux_basic/0220filemanager.php#suid)

```sh
ls -ld /tmp; ls -l /usr/bin/passwd
drwxrwxrwt. 20 root root 4096  6月  9 20:59 /tmp                # 有 t 出現在 rwx 裏頭
-rwsr-xr-x. 1 root root 27832  6月 10  2014 /usr/bin/passwd     # 有 s 出現在 rwx 裏頭
```

# 特殊權限
1. SUID (權限 4)
2. SGID (權限 2)
3. SBIT (權限 1)

```sh
# 要把檔案改成 「-rwsr-xr-x」
$ chmod 4755 xxx
```



## 1. SUID (只能作用於 檔案)
```sh
$ ls -l /usr/bin/passwd
-rwsr-xr-x. 1 root root 27832  6月 10  2014 /usr/bin/passwd
   ^     ^
 非擁有者可執行此二進位檔案(runtime 期間, 擁有 owner權限)
```


# 2. SGID (可用於 檔案 與 目錄) (不是很懂...)

```sh
$ sudo ls -l /var/lib/mlocate/mlocate.db /usr/bin/locate
-rw-r-----. 1 root slocate 9763613  6月  9 15:08 /var/lib/mlocate/mlocate.db
-rwx--s--x. 1 root slocate   40512 11月  5  2016 /usr/bin/locate
      ^  ^
  擁有 x 權限的使用者, 可執行此二進位檔案, runtime期間, 將會獲得該程式群組的支援

$ 
  
```

## 3. SBIT(Sticky Bit) 只針對 目錄 有效
(先 Pass...)



```sh
$ touch test

$ chmod 4755 test; ll test
-rwsr-xr-x. 1 tony tony 0  6月  9 22:01 test

$ chmod 6755 test; ll test
-rwsr-sr-x. 1 tony tony 0  6月  9 22:01 test

$ chmod 1755 test; ll test
-rwxr-xr-t. 1 tony tony 0  6月  9 22:01 test

$ chmod 7666 test; ll test
-rwSrwSrwT. 1 tony tony 0  6月  9 22:01 test    # test為紅底, 且具有空的 SUID/SGID權限 (大寫)

$ $ chmod u=rwxs,go=x test; ls -l test # 「,」前後不能加空白
-rws--x--x. 1 tony tony 0  6月  9 22:01 test    

$ chmod g+s,o+t test; ls -l test
-rws--s--t. 1 tony tony 0  6月  9 22:01 test

```






# 安全性相關

- 2018/06/09



# Firewall

Firewall Zone:
- block : 
- dmz : 
- drop : 
- external : 
- home : 
- internal : 
- public : 
- trusted : 
- work : 



# 檔案隱藏屬性 (我用 特殊屬性 來理解它...)

- [鳥哥 chattr](http://linux.vbird.org/linux_basic/0220filemanager.php#chattr)

隱藏屬性對於 Linux 來說, 只能在 Ext2/Ext3/Ext4 中完整生效, 像是 CentOS7 預設使用的 `xfs`, 僅有部分支援

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



# SELinux

- Linux 2.6版開始使用的**加強安全行的機制**

```sh
$ vi /etc/sysconfig/selinux
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=enforcing
# SELINUXTYPE= can take one of three two values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```

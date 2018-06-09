# 查硬碟容量 df 與 du

```sh
$ df [-ahikHTm] <目錄 or 檔案>
# a : 所有的檔案系統, 包含「/proc」(都在記憶體裡面, 不佔用磁碟空間)
# h : 已 kb, mb, gb, tb...表示
# T : 列出該 partition的 filesystem名稱, ex: xfs
# i : 已 inode代替 磁碟容量

# 預設以 bytes呈現
$ df
檔案系統             1K-區段     已用     可用 已用% 掛載點
/dev/mapper/cl-root 83845120  9466372 74378748   12% /
devtmpfs             1873356        0  1873356    0% /dev
tmpfs                1889720    41788  1847932    3% /dev/shm   # 記憶體虛擬出來的磁碟空間(通常是總實體記憶體的一半)
tmpfs                1889720     9384  1880336    1% /run
tmpfs                1889720        0  1889720    0% /sys/fs/cgroup
/dev/sda1            1038336   247708   790628   24% /boot
/dev/mapper/cl-var  52403200  2712540 49690660    6% /var
/dev/mapper/cl-home 83845120 11016896 72828224   14% /home
tmpfs                 377944        4   377940    1% /run/user/42
tmpfs                 377944       48   377896    1% /run/user/1000

$ df -h
檔案系統             容量  已用  可用 已用% 掛載點
/dev/mapper/cl-root   80G  9.1G   71G   12% /
devtmpfs             1.8G     0  1.8G    0% /dev
tmpfs                1.9G   42M  1.8G    3% /dev/shm    # 記憶體模擬, 在裡頭的存取非常快, 但開機後會消失
tmpfs                1.9G  9.2M  1.8G    1% /run
tmpfs                1.9G     0  1.9G    0% /sys/fs/cgroup
/dev/sda1           1014M  242M  773M   24% /boot
/dev/mapper/cl-var    50G  2.6G   48G    6% /var
/dev/mapper/cl-home   80G   11G   70G   14% /home
tmpfs                370M  4.0K  370M    1% /run/user/42
tmpfs                370M   48K  370M    1% /run/user/1000

$ df -T
檔案系統            類型      1K-區段     已用     可用 已用% 掛載點
/dev/mapper/cl-root xfs      83845120  9466372 74378748   12% /
devtmpfs            devtmpfs  1873356        0  1873356    0% /dev
tmpfs               tmpfs     1889720    42124  1847596    3% /dev/shm
tmpfs               tmpfs     1889720     9384  1880336    1% /run
tmpfs               tmpfs     1889720        0  1889720    0% /sys/fs/cgroup
/dev/sda1           xfs       1038336   247708   790628   24% /boot
/dev/mapper/cl-var  xfs      52403200  2712312 49690888    6% /var
/dev/mapper/cl-home xfs      83845120 11017240 72827880   14% /home
tmpfs               tmpfs      377944        4   377940    1% /run/user/42
tmpfs               tmpfs      377944       48   377896    1% /run/user/1000
```

```sh
$ du [-ahskm] <檔案 or 目錄>
# h : 人看得懂的 kb, mb, gb, ...
# s : 只列出總容量
# S : 不包含子目錄下的統計
# a : 列出所有的檔案與目錄容量(預設只有統計檔案數量)

$ du -a | head -3
0	./.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/langpack-zh-TW@firefox.mozilla.org.xpi
4	./.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/.fedora-langpack-install
4	./.mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}

# --max-depth=1, 最多到第一層子目錄的空間使用情形
$ du ~ -h --max-depth=1 | head -3
21M	/home/tony/.mozilla
662M	/home/tony/.cache
536M	/home/tony/.config
```
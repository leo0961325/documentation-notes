# CentOS7 為主

我的電腦環境如下
```sh
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

File Name            | Description
-------------------- | ------------------------------------------
installCentOS7.md    | 安裝一大堆有的沒的的說明
linux.md             | Linux`指令`及`概念`
hadoopNote.md        | Hadoop (新手誤入) (還沒認真開始寫)
vim.md               | 神之編輯器~~
iCentOS7.sh          | 因為很常重灌... 所以把安裝指令寫成腳本
bird.md              | 沒啥用...
other/installCentOS6 | 好久以前寫的...
other/ubuntu16.04.md | 好久以前寫的...
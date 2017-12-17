# [Orientation]((https://docs.docker.com/get-started/))
- 2017/12/15

## 1. Orientation 
##### 2. Containers 
##### 3. Services
##### 4. Swarms 
##### 5. Stacks 
##### 6. Deploy your app

---

我的使用環境~~~
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

安裝自己上網看啦@@凸, Docker安裝完後

```sh
$ docker --version
Docker version 17.09.0-ce, build afdb6d4

# 底下這行, 未必能執行!!! 如果正常執行~ 此篇不用再往下看了~~~
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
To generate this message, Docker took the following steps:
...(略)...
```

如果上面出現問題, 應該有87%是權限問題了! 繼續往下看~
```sh
# 1. 找找看有沒有名為 docker的 group
$ cat /etc/group | grep docker
docker:x:983:
# 上面一行告訴我們~ 有喔! 且 某個殺小的鬼東西(我真的不知道這是什麼...)為 983

# 2. 如果沒有的話, 執行此行
$ sudo groupadd docker

# 3. 把目前使用者, 加入 docker的群組~
$ sudo usermod -aG docker $USERNAME

# 4. 再次看看~
$ cat /etc/group | grep docker
docker:x:983:tonynb
# 我的電腦就是 tonynb, 已經加入 docker的群組了
```

---


# [Part1 - Orientation](https://docs.docker.com/get-started/)
- 2017/12/15

### 1. [Orientation ](./part1.orientation.md)
##### 2. [Containers](./part2.containers.md)
##### 3. [Services](./part3.services.md)
##### 4. [Swarms](./part4.swarm.md)
##### 5. [Stacks](./part5.stacks.md) 
##### 6. [Deploy your app](./part6.deploy.md)

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

我的 Docker版本 
```sh
$ docker --version
Docker version 17.09.0-ce, build afdb6d4
```

==== 安裝步驟 ====

安裝自己上網看啦@@凸

==== 安裝步驟 ====

安裝完後, 先測試一下, 如果有看到 Hello from Docker!的字樣, 表示沒問題了...
```sh
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
...(略)...
# 如果正常執行~ 此篇不用再往下看了~~~
```

如果上面出現問題, 應該有87%是權限問題了! 繼續往下看~
```sh
# 1. 找找看有沒有名為 docker的 group
$ cat /etc/group | grep docker
docker:x:983:
# docker這個使用者群組的 Group ID為 983

# 2. 如果上步驟沒有出現的話, 執行此行
$ sudo groupadd docker

# 3. 把目前使用者, 加入 docker的群組~
$ sudo usermod -aG docker $USERNAME

# 4. 再次看看~
$ cat /etc/group | grep docker
docker:x:983:tonynb
# 我的電腦就是 tonynb, 已經加入 docker的群組了
```
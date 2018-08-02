# bash - issue

## bash 進站訊息 (沒啥鳥用, 自己看爽的)

登入訊息, 歡迎訊息, 進站訊息, ssh登入訊息

- /etc/issue        : 本機 tty 進去看到的訊息
- /etc/issue.net    : 遠端 telnet 進去看到的訊息
- /etc/motd         : 遠端 ssh 進去看到的訊息

```sh
$ cat /etc/issue
\S
Kernel \r on an \m
```

進入 tty2~tty6之後看到場景如下~
```sh
CentOS Linux 7 (Core)
Kernel 3.10.0-693.21.1.el7.x86_64 on an x86_64

tonynb login:
```

script | Description
------ | --------------
\S     | OS name
\r     | OS edition
\m     | hardware grade(i386/i686...)
\t     | time
\d     | date
\l     | which tty
\n     | host name
\o     | domain name


```sh
$ sudo vi /etc/motd

---------------------                   -------------------
|     |       |     |                   |     |     |     |
|     /       \     |                   |     /     \     |
|    /         \    |                   |    /       \    |
|----           ----|                   |----         ----|
|     |-------|     |                   |     |-----|     |
|     |       |     |                   |     |     |     |
|     |       |     |                   |     |     |     |
---------------------                   -------------------
          |                                      |         
        --|--                                   /|\        
       /  |  \                                 / | \       
         / \                                    / \        
```


```sh
# 打算把訊息塞到 /etc/motd
$ echo "QQQ" >> /etc/motd
# 但是權限不夠

# 
$ echo "QQQ" | sudo /etc/motd


$ echo "QQQ" | sudo tee -a /etc/motd
```



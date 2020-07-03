# bash腳本練習及備註

幾乎都是從[鳥哥](http://linux.vbird.org/linux_basic/)那邊來的

```sh
$ $ uname -a
Linux tonynb 3.10.0-693.21.1.el7.x86_64 #1 SMP Wed Mar 7 19:03:37 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

$ cat /etc/centos-release
CentOS Linux release 7.4.1708 (Core)
```

> 指令 `command [-options] parameter1 parameter2 ...`


### set -e && set -x

- [What does set -e mean in a bash script?](https://stackoverflow.com/questions/19622198/what-does-set-e-mean-in-a-bash-script)
- [Aborting a shell script if any command returns a non-zero value?](https://stackoverflow.com/questions/821396/aborting-a-shell-script-if-any-command-returns-a-non-zero-value/821419#821419)
- [Stop on first error](https://stackoverflow.com/questions/3474526/stop-on-first-error)

> 常看到有人都會使用 `set -ex`. `help -m set | vim -` 看更多說明

```bash
#!/bin/bash
set -e 
# Scripts.....
# 上頭這種 `set -e` 常看到出現再 shell script, 就是再告知, 腳本內如果出錯的話, 立即停止執行
# 用來避免前期錯誤導致後續雪崩式的錯誤
```

- [What does `set -x` do?](https://stackoverflow.com/questions/36273665/what-does-set-x-do)

```bash
#!/bin/bash
set -x
# Scripts.....
# 將所有 executable commands 印到 terminal(debug用). 後續可使用
# 「set +x」將該設定 disable 掉
```

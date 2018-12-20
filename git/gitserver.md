# Git Server

- 2018/12/20


## 自己搞 Git Server

- Computer A : Git Server
- Computer B : Git Client


### Computer A

```sh
### A
# 安裝完 Git 之後
$# useradd qoo; echo 'qoo' | passwd --stdin qoo

$# ssh qoo@localhost

$# mkdir q1

$# cd q1

$# git --bare init
```

### Computer B

```sh
# git clone ID@HOST:/Path/ProjDir
$# git clone qoo@192.168.124.23:/home/qoo/q1
warning: You appear to have cloned an empty repository.

$# git remote -vv
origin  qoo@192.168.124.23:/home/qoo/q1 (fetch)
origin  qoo@192.168.124.23:/home/qoo/q1 (push)

# 編輯完, Commit 之後

$# git push
# 要打密碼

# 傳送公鑰, 將來免輸入密碼
$# ssh-copy-id qoo@192.168.124.23
```



# 追蹤遠端分支
- 2018/06/17

> 專案之間相似行頗高, 想把一個專案丟給A, B 客戶; <br> A客戶 -> `dev-a分支`, B客戶 -> `dev-b分支`

## Prerequest
- 熟悉 git add, git commit, git branch, git pull, git push
- 熟悉 git hub
- 預先設定好 github ssh 傳輸
- 2台 電腦
- 2組 github帳號 (cool21540125, test21540125)

## 1. 專案起始 (cool21540125)
```sh
$ git init qq
$ cd qq
$ echo "Initialization~" >> README.md
$ git add .
$ git commit -m "Init commit"

# 前往 Github, 建立空專案, 名為 qq

$ git remote add origin git@github.com:cool21540125/qq.git
$ git push -u origin master

# Github, master 已有 README.md

$ git checkout -b dev
$ echo "hi" >> a.txt
$ git add .
$ git commit -m "新增 a.txt"

$ git branch -a # 看看就好
# * dev
#   master
#   remotes/origin/master
$ git branch -r # 看看就好
#   origin/master
$ git branch -v # 看看就好
# * dev    a779b32 新增 a.txt
#   master b12b9ea Init commit

$ git push --set-upstream origin dev
$ echo "amigo" >> b.txt
$ git add .
$ git commit -m "新增 b.txt"
$ git push

# Github, dev 已新增 a.txt 及 b.txt

$ git checkout master
$ git merge dev
$ git push

# Github, master 已與 dev 重疊

$ git checkout dev
$ echo "haha" >> c.txt
$ git add .
$ git commit -m "新增 c.txt"
$ git push

$ git branch -a # 看看就好
# * dev
#   master
#   remotes/origin/dev
#   remotes/origin/master
$ git branch -r # 看看就好
#   origin/dev
#   origin/master
$ git branch -vv # 看看就好
# * dev    188f9ec [origin/dev] 新增 c.txt
#   master e61d254 [origin/master] 新增 b.txt
```

## 2. Clone專案 (test21540125)
```sh
$ git clone git@github.com:cool21540125/qq.git
$ cd qq
$ ls
# 只有 README.md, a.txt, b.txt

$ git branch -a # 看看就好
# * master
#   remotes/origin/HEAD -> origin/master
#   remotes/origin/dev
#   remotes/origin/master
$ git branch -r # 看看就好
#   origin/HEAD -> origin/master
#   origin/dev
#   origin/master
$ git branch -v # 看看就好
# * master e61d254 新增 b.txt

$ git pull origin dev
# From github.com:cool21540125/qq
#  * branch            dev        -> FETCH_HEAD
# Updating e61d254..188f9ec
# Fast-forward
#  c.txt | 1 +
#  1 file changed, 1 insertion(+)
#  create mode 100644 c.txt

$ ls
# README.md  a.txt  b.txt  c.txt

$ git branch -a # 看看就好
# * master
#   remotes/origin/HEAD -> origin/master
#   remotes/origin/dev
#   remotes/origin/master
$ git branch -r # 看看就好
#   origin/HEAD -> origin/master
#   origin/dev
#   origin/master
$ git branch -v # 看看就好
# * master 188f9ec [ahead 1] 新增 c.txt
```

## 3. 修改專案 (cool21540125)

```sh
$ git checkout -b dan
$ echo "zzz" > z.txt
$ git add .
$ git commit -m "New z.txt"
$ git checkout master
$ git merge dan
$ git push


```
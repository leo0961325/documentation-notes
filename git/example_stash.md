# git stash 及 git tag的用法
- 2018/03

## Prerequest: 安裝好 git, git bash
```sh
$ git --version
git version 2.13.3.windows.1
```

## 範例
```sh
### 2/8 起始一個「happy」專案, 用來幫助「快樂神經病公司」問候全體員工, 並鼓舞士氣的人性化軟體.
git init 'happy'
cd happy
touch Hello.java
echo 'print("Good Morning");' > Hello.java
git add Hello.java
git commit -m "初始 commit, 完成 Hello的功能"
git tag 1.0
git log --graph --oneline
# 已經開發好了 1.0版, 裡面只有 Hello.java


### 3/5 在 develop分支, 開始進行 GoodJob.java的開發
git checkout -b develop
touch GoodJob.java
echo 'print("Good Job!!");' > GoodJob.java
git add GoodJob.java
git commit -m "開發完 GoodJob部分的功能"
git branch
ls
git log --graph --oneline
# 要開始開發新功能 GoodJob.java, 為了不影響主線(master), 因此利用分支(develop)來開發, 但因為還沒開發完成, 所以不能 merge回 master


### 3/31 終於, 在日期內把 GoodJob.java開發完成, 並且合併到 master了
echo 'print("Good Bye. You are fired!!!");' >> GoodJob.java
git add GoodJob.java
git commit -m "完成第二版, GoodJob功能開發完成"
git checkout master
git merge develop --no-ff -m "完成 GoodJob功能的開發"
git branch
git tag 2.0
ls
git log --graph --oneline
# GoodJob.java 開發完成!! merge回 master


### 5/3 開始開發第三支程式 Tired.java, 快完成時, 被告知 Hello.java 有緊急BUG, stash起來
git checkout develop
touch Tired.java
echo 'print("I am ...");' >> Tired.java
git stash save -u "正在寫 Tired.java, 被抓去修 Hello.java的 bug"
git stash list
# 把開發到一半的東西, 丟到 暫存版


### 5/5 終於, 把 Hello.java的 bug修完了, 合併回主程式, 並且更新版本編號
git checkout master
git checkout -b bugFix
echo 'print("Hello~~~~~~");' > Hello.java
git add Hello.java
git commit -m "修正 Hello的 bug"
git checkout master
git merge bugFix --no-ff -m "合併 develop分支 - 完成 Hello的開發"
git branch
git tag 2.1
ls
git log --graph --oneline
# 把 Hello.java(2.0版) 的 bug修完了! merge回


### 5/8 回去繼續開發 Tired.java
git stash list
git checkout develop
git stash pop
echo 'print("I am very tired!!");' >> Tired.java
git add Tired.java
git commit -m "Finish Tired.java"
git checkout master
git merge develop --no-ff -m "合併 develop分支 - 完成 Tired的功能"
git branch
git tag 3.0
ls
git log --graph --oneline
```
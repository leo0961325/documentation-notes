# 使用 git remote (2018/3/21 未完成!!)

## Prerequest: 
1. 安裝好 git
2. 註冊 git hub
> 模擬情境: Tony與 Andy共同開發 qq專案(`開啟2個 Terminal`), 一開始由 Tony建立專案, 完成一部分後, Andy開始介入開發, 兩人開發到一半的功能, 都會 push到 **遠端分支**, 等到完成時, 再由 Tony來將分支合併到 master, 隨著專案的開發... 團隊逐漸壯大

### Tony Terminal
```sh
git init 'qq'
cd qq
touch README.md
echo 'ONLY TEST, NOTHING HERE!!!!' > README.md
touch Hello.java
echo 'print("Good Morning");' > Hello.java
git add Hello.java
git commit -m "初始 commit, 完成 Hello的功能"
git tag 1.0
git log --graph --oneline
```

### Git Repository
1. 到 Github建立新的專案, 名為 `qq-proj`

### Tony Terminal
```sh
### 上傳專案到 github - "qq-proj"
git remote add origin https://github.com/cool21540125/qq-proj.git
git tag 1.0
git push -u origin master
git log --graph --oneline
```

### Andy Terminal
```sh
### Andy把專案拉下來(clone)以後, 開始著手開發 Idiot.java
git clone https://github.com/cool21540125/qq-proj.git
cd qq-proj
git checkout -b develop
touch Idiot.java
echo 'I am idiot!' > Idiot.java
git add Idiot.java
git commit -m "完成 Idiot的功能"
# 我不知道底下3個差在哪邊...
git remote -v
git branch -a
git branch -r

git checkout master
git merge develop
git tag 2.0
git log --graph --oneline
```

### Tony Terminal
```sh
### Tony切換到分支後, 開始著手開發 Wahaha.java
git checkout -b feature
touch Wahaha.java
echo 'I am happy, wahahahaa' > Wahaha.java
git add Wahaha.java
git commit -m "Wahaha開發到一半, 需要Joshua協助開發"
git push --set-upstream origin feature
```

### Joshua Terminal
```sh
### Joshua參與專案, 接手 Tony留下來的技術債~
git clone https://github.com/cool21540125/qq-proj.git
git remote -v
git branch -r
git branch -a
git checkout -b feature

# 下面這個會失敗~ 因為 feature這個分支並沒有在追蹤遠端的 origin/feature分支
git pull

# 下面這個, 會誤把 origin/feature合併到 master
git pull origin feature
git log --graph --oneline
git reset HEAD^ --hard

# 設定 feature 追蹤 origin/feature
git branch --set-upstream-to=origin/feature feature
git pull
git log --graph --oneline
git branch -r

```
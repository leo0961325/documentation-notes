# 使用 git remote 
- 2018/3/22

```sh
# 這些先寫起來放, 隨時可用... 
git branch -a       # 顯示所有本地分支 && 遠端分支

git branch          # 顯示所有本地分支
git branch -v       # 顯示所有本地分支 -詳細一點點
git branch -vv      # 顯示所有本地分支 -超級詳細
```
# Prerequest: 
1. 安裝好 git
2. 註冊 git hub
3. 底下會扯到的關鍵字及概念:
    - git add
    - git commit
    - git branch
    - git tag
    - git stash
    - git pull
    - git push



# 故事開始~
> 模擬情境: Tony與 Andy共同開發 qq專案(`開啟2個 Terminal`), 一開始由 Tony建立專案, 完成一部分後, Andy開始介入開發, 爾後又有 Joshua加入, 完成後會 push到 **遠端分支**. **`需要開啟3個 Git Bash來模擬 3個本地端專案`**

### Tony Terminal
```sh
### Tony建立初始專案, 完成了 Hello.java, 並且標註為1.0版
git init 'qq'
cd qq
touch Hello.java
echo 'Good Morning;' > Hello.java
git add Hello.java
git commit -m "Tony: 首次提交, 完成 Hello功能"
git tag 1.0
git log --graph --oneline
```

### Git Repository
- 到 Github建立新的專案, 名為 `qq-proj`

### Terminal - Tony
```sh
### 上傳專案到 github - "qq-proj"
git remote add origin git@github.com:cool21540125/qq-proj.git
git push -u origin master
git push origin 1.0
```

### Terminal - Andy
```sh
### 新進員工 Andy, 加入開發團隊, 著手開發 Idiot.java
git clone git@github.com:cool21540125/qq-proj.git
cd qq-proj
git checkout -b develop
touch Idiot.java
echo '5987' > Idiot.java
git add Idiot.java
git commit -m "Andy: 完成 Idiot功能"
git branch -vv
git checkout master
git merge develop
git pull
git tag 2.0
git log --graph --oneline
git push
git push origin 2.0
# 這邊要注意, 開始會有時間軸的問題!!
# Andy push後, Tony可能已經在開發其他東西了(而不知道 Andy作了啥), 時空開始分歧...
```

### Terminal - Tony
```sh
### Tony開始著手開發新功能 Wahaha.py, 完成一部份, 推送到遠端後, 等待新人來接手
git checkout -b feature
touch Wahaha.py
echo 'I am happy, wahahahaa' > Wahaha.py
git add Wahaha.py
git commit -m "Tony: Wahaha開發到一半, 需要Joshua協助開發"
ls
git push --set-upstream origin feature
```

### Terminal - Joshua
```sh
### 業界顧問 Joshua加入開發, 接手 Tony的 Wahaha.py
git clone git@github.com:cool21540125/qq-proj.git joshua
cd joshua
git checkout -b feature
git branch -vv
ls
git log --graph --oneline

# 下面這個會失敗~ 因為 feature這個分支並沒有在追蹤遠端的 origin/feature分支
git pull

# A 及 B 效果一樣, 都是作 feature 追蹤並 pul origin/feature, ※ 個人建議用 B ※
## A(自動設定'目前的分支'去追蹤的'遠端分支')
git pull origin feature

## B (手動設定'本地特定分支'去追蹤'特定遠端分支')
git branch --set-upstream-to=origin/feature feature
git pull

git log --graph --oneline
echo '白癡' >> Wahaha.py
git add Wahaha.py
git commit -m "Josh: 完成 Tony寫到一半的 Wahaha"
git log --graph --oneline
git checkout master
git log --graph --oneline
git merge feature
git log --graph --oneline
git pull
git tag 3.0
git log --graph --oneline
git push
git push origin 3.0
```

### Terminal - Andy
```sh
### 持續朝向下一版邁進~~ 新增了 Powerful.java, 但發現了自己之前寫的 Idiot.java有 bug...
git checkout develop
touch Powerful.java
echo '我好厲害' > Powerful.java
ls
git log --graph --oneline
git stash save -u "發現之前的 Idiot有 bug, 先把現在的東西暫存起來..."
ls
git checkout master
git checkout -b bugFix
echo 'I am NOT idiot!!!!' > Idiot.java
echo '除了我以外, 通通都是白癡' >> Idiot.java
git add Idiot.java
git commit -m "Andy: 修改 Idiot的大BUG"
git checkout master
git merge bugFix
git pull

git push
git tag 2.1
git push origin 2.1
git log --graph --oneline

# 發現 tag 版本錯亂了~~~
git tag -d 2.1
git push --delete origin 2.1
git tag 3.1
git push origin 3.1
git log --graph --oneline
```

### Terminal - Joshua
```sh
cat Idiot.java
git pull
cat Idiot.java
git log --graph --oneline
git push
```


### Terminal - Andy
```sh
# 改完bug後, 繼續回去開發 Powerful.java
ls
git checkout develop
git stash pop
ls
echo '誰都贏不過我' >> Powerful.java
echo '哼' >> Powerful.java
git add Powerful.java
git commit -m "Andy: 林北完成了 Powerful"
git checkout master
git merge develop

git log --graph --oneline
git pull
git log --graph --oneline
git tag 4.0
git push
git push origin 4.0
git log --graph --oneline
```

### Terminal - Tony
```sh
# Tony打算看看現在專案改成什麼德行...
git checkout master
git pull
git log --graph --oneline
```
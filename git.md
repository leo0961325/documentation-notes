# git相關知識

- [Git 建立共用repo](https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/03.md)
- [Git branch的操作](https://blog.gogojimmy.net/2012/01/21/how-to-use-git-2-basic-usage-and-worflow/)
- [Git初學者心得分享](http://www.mrmu.com.tw/2011/05/06/git-tutorial-for-beginner/)
- [Git中文化電子書](https://git-scm.com/book/zh-tw/v2)
- [Git視覺化遊戲](http://learngitbranching.js.org/)

<br />



# 示意圖

## 狀態週期
![GitCommit03](img/gitCommit03.jpg)

## 遞交流程
![GitFlow](img/gitFlow.jpg)

1. 還沒經過add後 -> unstage
2. 經過add但尚未commit -> stage

# 概念備註 

origin | master
--- | ---
遠端repo的預設名稱 | 本地端分支的預設名稱

## 層級
層級 | 指令 | 說明
--- | --- | ---
儲存庫層級 |  | 只對目前的repo有效(default)
使用者層級 | --global | 對目前使用者有效
系統層級 | --system | 對所有使用者/儲存庫都有效

<br />



# 設定指令

## - 設定commit訊息
### 標準指令
```sh
$ git config --global alias.st status
$ git config --global alias.co commit
```

### 範例
```
$ git config --global user.name "TonyCJ"
$ git config --global user.email "cool21540125@gmail.com"
$ git config --list
    user.name=TonyCJ
    user.email=cool21540125@gmail.com
```
---



## - 設定指令別名
### 標準指令
```sh
$ git config <層級> alias.<別名的名稱> '<你的git命令>'
```

### 範例
```
# 想在bash(純文字介面)底下看到log狀態, 可以打
$ git log

# 或者, 想要以樹狀結構看log, 可以打下面這這行...
$ git log --graph --decorate --pretty=oneline --abbrev-commit

# 因為實在太囉唆了, 把他設別名
$ git config --global alias.tree 'log --graph --decorate --pretty=oneline --abbrev-commit'

# 如此一來, git log樹狀結構便可以用簡短指令查看了
$ git tree
```
---



## - 忽略「空白」所造成的影響(ex:Ruby)
### 標準指令
    
```sh
# Git會主動忽略空白造成的影響
$ git config --global apply.whitespace nowarn
```


---
## - 增加Git輸出時的顏色
### 標準指令
```sh
# git輸出的時候, 能有漂漂亮亮的顏色
$ git config --global color.ui true
```
---
## 分支

-f 選項直接讓分支指向另一個 commit

```sh
git branch -f master HEAD~3

```

---

## - 遠端連線設定

### 標準指令
```sh
# Client端設定(windows)
$ ssh-keygen -t rsa -C '<e-mail>'
# -C 是指讓識別碼以email為識別值, 而非預設的「帳號@遠端主機位址」
```

### 範例
```sh
$ ssh-keygen -t rsa -C 'cool21540125@gmail.com'

# 如果要設定git server, 繼續往下作...
# 把剛剛產生的id_rsa.pub寄給git server管理者

$ cd ~/.ssh
$ scp id_rsa.pub <遠端機器>:/tmp/id_rsa.user1.pub 
# 最後一行沒試過, 有待查證
```

---


---



## - Git環境 組態參數

    組態檔可能存在於3個地方

    a. /etc/gitconfig
    b. ~/.gitconfig、~/.config/git/config
    c. 專案裏頭的.git/config

## --- 

# 指令彙整

```$ git config <para>```
| para | 說明 |
| --- | --- |
| --global |  |
| --system |  |
| --local |  |
| --blob |  |
| --f |  |
| --list | 顯示組態設定值 |

---

## 操作指令

- 建立新的git repo
    ```sh
    $ git init
    ```

- 建立共享式repo -沒有工作目錄的純儲存庫(bare repository)

    建立完後, 裡面千萬不要去動到. 只能用來儲存 Git 的相關資訊.
    使用時機:

    - 多人同台電腦開發

    - 同作者多台電腦同步repo
    ```sh
    $ git init --bare
    ```

- 鎖定遠端repo、遠端repo追蹤
    ```sh
    $ git init
    $ git add README.md
    $ git commit -m 'xxx'
    $ git remote add origin https://github.com/cool21540125/illu.git
    $ git push -u origin master
    ```

- 加入至stage狀態
    建議使用互動式模式來加入檔案到stage狀態
    ```sh
    $ git add -i
    $ git add .
    ```

- git commit歷史訊息
    ```sh
    $ git log
    $ git log --stat
    $ git log -p
    ```

- 不要commit特定檔案

    把檔名加入.gitignore即可
    ```sh
    $ vi .gitignore
    ```
- 檢查目前commit所有內容的狀態索引
    [有捨才有得 - 設定.gitignore忽略檔案不被track](http://italwaysrainonme.blogspot.tw/2013/01/git-gitignore-commit.html)

    ```sh
    $ git ls-files --stage
    100644 7984d412fa0fe0a427c7240c0958e0f858499310 0       .gitignore
    100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0       t1
    ```

- 紀錄變更

    ```sh
    $ git status
    $ git status -s

    把不加入追蹤的檔案, 放到.gitignore中
    $ cat .gitignore
    ```
    
- merge VS rebase
    以目前branch為主, 把master與目前branch合併為新版
    ```
    $ git merge master
    ```

    把目前branch作<font color='yellow'>Commit</font>及<font color='yellow'>搬移</font>到master branch底下
    ```
    $ git rebase master
    ```

- 回到過去
	強制移動master指向從HEAD往上數的第3個parent commit
	```sh
	$ git branch -f master HEAD~3
	```


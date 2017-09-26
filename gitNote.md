# git相關知識

- https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/03.md
- https://gogojimmy.net/2012/01/17/how-to-use-git-1-git-basic/
- https://blog.gogojimmy.net/2012/01/21/how-to-use-git-2-basic-usage-and-worflow/
- http://www.mrmu.com.tw/2011/05/06/git-tutorial-for-beginner/

---

## 概念

1. 還沒經過add後 -> unstage
2. 經過add但尚未commit -> stage

===

## 設定指令

- 設定commit訊息
    ```
    $ git config --global user.name "TonyCJ"
    $ git config --global user.email "cool21540125@gmail.com"
    $ git config --list
        user.name=TonyCJ
        user.email=cool21540125@gmail.com
    ```

- 設定指令別名(偷懶@@)
    ```
    $ git config --global alias.st status
    $ git config --global alias.co commit
    ```

- 忽略「空白」所造成的影響(ex:Ruby)

    Git會主動忽略空白造成的影響
    ```
    $ git config --global apply.whitespace nowarn
    ```

- 增加Git輸出時的顏色
    ```
    $ git config --global color.ui true
    ```

- 遠端連線設定
    Client端設定(windows)
    ```
    $ ssh-keygen -t rsa -C 'cool21540125@gmail.com'
    ```
    Note: -C 是指讓識別碼以email為識別值, 而非預設的「帳號@遠端主機位址」

    (如果要設定git server, 繼續看下面...)
    把剛剛產生的id_rsa.pub寄給git server管理者
    ```
    $ cd ~/.ssh
    $ scp id_rsa.pub <遠端機器>:/tmp/id_rsa.user1.pub 
    ```




===

## 操作指令

- 建立新的git repo
    ```
    $ git init
    ```

- 建立共享式repo -沒有工作目錄的純儲存庫(bare repository)

    建立完後, 裡面千萬不要去動到. 只能用來儲存 Git 的相關資訊.
    使用時機:

    - 多人同台電腦開發

    - 同作者多台電腦同步repo
    ```
    $ git init --bare
    ```

- 鎖定遠端repo、遠端repo追蹤
    ```
    $ git init
    $ git add README.md
    $ git commit -m 'xxx'
    $ git remote add origin https://github.com/cool21540125/illu.git
    $ git push -u origin master
    ```

- 加入至stage狀態
    建議使用互動式模式來加入檔案到stage狀態
    ```
    $ git add -i
    $ git add .
    ```

- git commit歷史訊息
    ```
    $ git log
    $ git log --stat
    $ git log -p
    ```

- 不要commit特定檔案

    把檔名加入.gitignore即可
    ```
    $ vi .gitignore
    ```
- 檢查目前commit所有內容的狀態索引
    [有捨才有得 - 設定.gitignore忽略檔案不被track](http://italwaysrainonme.blogspot.tw/2013/01/git-gitignore-commit.html)
    ```
    $ git ls-files --stage
    100644 7984d412fa0fe0a427c7240c0958e0f858499310 0       .gitignore
    100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0       t1
    ```

- 
    
    
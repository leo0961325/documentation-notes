# git相關知識

- [Git 建立共用repo](https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/03.md)
- [Git branch的操作](https://blog.gogojimmy.net/2012/01/21/how-to-use-git-2-basic-usage-and-worflow/)
- [Git初學者心得分享](http://www.mrmu.com.tw/2011/05/06/git-tutorial-for-beginner/)
- [Git中文化電子書](https://git-scm.com/book/zh-tw/v2)
- [Git視覺化遊戲](http://learngitbranching.js.org/)

# A. 概念
## 名詞定義
branch | 說明
------ | ------
master | 本地端分支的預設名稱
origin | 遠端repo的預設名稱


---
## 遞交流程
![GitFlow](img/gitFlow.jpg)


---
## 層級
層級       | 指令     | 說明
--------- | -------- | ---
儲存庫層級 | --local  | 只對目前的repo有效(default)
使用者層級 | --global | 對目前使用者有效
系統層級   | --system | 對所有使用者/儲存庫都有效


---
## Merge 與 Rebase
> Merge: `合併後, 分支仍然存在`
```sh
$ git branch
* master
  tony

$ git merge tony
...(一堆log)...
```

> Rebase: `合併後, 分支與 master在相同 index`
```sh
$ git branch tony
  master
* tony

$ git rebase master         # 把 tony搬到 master的下一個階段
...(一堆log)...

$ git checkout master

$ git rebase tony           # 把 (落後的)master, 合併到 tony
```


---
## 組態檔的位置
層級 | 位置
--- | ---
system | /etc/gitconfig
user   | ~/.gitconfig、~/.config/git/config
local  | 專案裏頭的.git/config

---
## HEAD節點標籤
此節點標籤, 永遠代表最新的 commit
```sh
$ git show HEAD
# 顯示最新 commit的詳細資料
```

---
## git merge
把指定的分支, 合併到目前的分支
```sh
# 目前位於 branch A
# 打算合併 branch B
$ git merge B
#  B   A
#   \  |
#    \ |
#     \|
#      A
```


---
## git merge 「fast-forward merge」
讓 master分支, 沿著分支快轉前進(不會產生新的節點)
```sh
#  O bug/123分支
#  |
#  O
#   \
#    O master分支
$ git checkout master
$ git merge bug/123
#  O master, bug/123分支
#  |
#  O
#   \
#    O 
```


---
## git merge 「3-way merge」
讓 master, 沿著依照分支合併, 但留下歷史紀錄
```sh
#  O bug/123分支
#  |
#  O
#   \
#    O master分支
$ git checkout master
$ git merge --no-ff bug/123
#    O 4df9f67 (HEAD -> master)
#   /|
#  O | (bug/123分支)
#  | |
#  O |
#   \|
#    O 5223fd5(過去的master)
```


---
## git reset 取消提交
將 git檔案庫回復到某一個舊節點的狀態.
取消最近一次的合併動作
```sh
$ git reset HEAD^ --hard
# --hard, 表示資料夾中的檔案也要一起回復
```


## cherry-pick (有點高段, 不好使用...)
把某一個 commit節點的檔案版本, 合併到資料夾的檔案
```sh
$ git cherry-pick commit <節點標籤>
```


---
## 放棄合併衝突
執行合併後, 產生衝突, 打算放棄此合併, 則會回到未執行合併前的狀態
```sh
$ git merge --abort

$ git cherry-pick --abort
```


---
## git rebase
```sh

```



# B. Git 組態

## 設定別名
> 指令: `git config --<層級> alias.<縮寫名稱> <原始指令>`
```sh
$ git config --global alias.cm "commit -m"
# 將來可用 git cm "..." 來代替 git commit -m "..."

$ git config --global alias.unstage "reset HEAD --"     # 將檔案從 index中移除
# 將來可用 git unstage a.js 來取代 git reset HEAD a.js

$ git config --global alias.undo "reset --soft HEAD~1"  # 取消最近一次提交
# 將來可用 git undo a.js 來取代 git reset --soft HEAD~1 a.js

$ git config --global alias.tree "log --graph --decorate --pretty=oneline --abbrev-commit"
# 將來可用 git tree 來漂亮的看提交紀錄

$ git config --global alias.tree2 "log --graph --oneline --all --decorate"
# 將來可用 git tree2 來漂亮的看提交紀錄
```


---
## 移除別名
> 指令 : `git config --<層級> --unset alias.<已建立的別名>`


---
## 必用
```
$ git config --global user.name "TonyCJ"
$ git config --global user.email "cool21540125@gmail.com"
$ git config --list
    user.name=TonyCJ
    user.email=cool21540125@gmail.com
```


---
## 忽略「空白」所造成的影響
```sh
$ git config --global apply.whitespace nowarn
```


---
## 增加Git輸出時的顏色
```sh
$ git config --global color.ui true
```


---
## 遠端連線設定 (For Windows)
```sh
> ssh-keygen -t rsa -C '<e-mail>'
# -C 是指讓識別碼以email為識別值, 而非預設的「帳號@遠端主機位址」
```


---
## 顯示所有組態
```sh
> git config -l

> git config --system -l  # 系統層級

> git config --global -l  # 使用者層級
```


---
## .gitignore
```git
*.txt        # 不要追蹤所有 txt檔
!note.txt    # 但是排除 note.txt(要追蹤)
```


---
## 取消追蹤特定檔案
將檔名加到 `.gitignore`即可
```sh
$ vi .gitignore     # 把檔名加入.gitignore即可
```


# C. 指令彙整
## 選項
選項 | 說明 | 範例 
--- | --- | ---
-s | 簡易資訊 | git status -s


---
## 參數
 參數   |      說明       | 範例
 ------ | -------------- | ---
 --blob |                |
 --f    |                |
 --list | 顯示組態設定值  | 

# D. 操作指令
## 建立新的git repo
> 參考: [共用儲存庫](https://ithelp.ithome.com.tw/articles/10132804)
```sh
$ git init
$ git init --bare
```


---
## 鎖定遠端repo、遠端repo追蹤
```sh
$ git init
$ git add README.md
$ git commit -m 'xxx'
$ git remote add origin https://github.com/cool21540125/illu.git
$ git push -u origin master
```


---
## 加入至stage狀態
```sh
$ git add -i    # 建議使用互動式模式來加入檔案到stage狀態
$ git add .     # (不建議使用, 請用上者來代替)

# 把已經 git add 的檔案, 從已追蹤名單中移除
$ git rm --cached <檔名>
# ((--cached 也可以解釋成, 從快取中... 或 從 index中...))

# 
$ 
```


---
## 回到過去
```sh
$ git branch -f master HEAD~3
# 強制移動master指向從HEAD往上數的第3個parent commit
```


---
## 刪除分支
```sh
$ git branch -d <要刪除的分支名稱>
# 若該分支還沒作 merge, 則無法刪除

$ git branch -D <要刪除的分支名稱>
# 強制刪除
```


---
## 重新命名分支
```sh
$ git branch -m <新的分支名稱>
```


---
## 清理檔案庫
Git經過一段時間之後, .git的資料夾會變得無比的巨大, 可以使用下列指令來清理此檔案庫, 指令為
```sh
$ git gc
```

option       |                 說明
------------ | ----------------------------------------
N/A          | (預設) 會用比較快速的方式檢查&&清理
--aggressive | 最慢、最仔細
--auto       | Git自動判斷是否需要清理, 情況良好則不動作
--no-prune   | 不要清除repo, 而是用整了的方式


# E. 其他
## 這幹嘛的我忘了...
```sh
$ git branch -f master HEAD~3
# -f 選項直接讓分支指向另一個 commit
```


---
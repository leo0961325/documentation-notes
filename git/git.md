# git相關知識

- [Learning git in 30 days](https://github.com/doggy8088/Learn-Git-in-30-days/tree/master/zh-tw)
- [Git branch的操作](https://blog.gogojimmy.net/2012/01/21/how-to-use-git-2-basic-usage-and-worflow/)
- [Git初學者心得分享](http://www.mrmu.com.tw/2011/05/06/git-tutorial-for-beginner/)
- [Git中文化電子書](https://git-scm.com/book/zh-tw/v2)
- [Git視覺化遊戲](http://learngitbranching.js.org/)

```sh
# 作業環境
$ uname -a
Linux tonynb 3.10.0-514.el7.x86_64 #1 SMP Tue Nov 22 16:42:41 UTC 2016 x86_64 x86_64 x86_64 

# 版本
$ git --version
git version 2.14.3
```

# A. 概念
> Git為 `分散式版本控管系統(Distributed Version Control System)`. 
## 示意圖
![Git0](img/git01.jpg)

![Git1](img/git02.jpg)
```
add : 將 檔案 加入版本控管

```

# B. 名詞定義
## 分支名稱
Name   | Description
------ | ----------------------------------
master | Local repository Default Name
origin | Remote repository Default Name





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
#  B  A
#   \ |
#    \|
#     A
```


---
## git merge 「fast-forward merge」
讓 master分支, 沿著分支快轉前進(不會產生新的節點)
```sh
# 「O」代表每次 commit, (越下面的 commit表示越新,)
# 「*」代表目前所在分支
#
#  O master (較舊)
#   \
#    O 
#    |
#    O bug/123* (最新)

# Case1 - 合併 master與 bug/123 (合併後, 沒有留下合併的歷史紀錄)
$ git checkout master
$ git merge bug/123
#  O
#   \
#    O 
#    |
#    O bug/123, master*

# Case2 - 合併 master與 bug/123, 使用「--no-ff」 (合併後, 留下歷史紀錄)
$ git checkout master
$ git merge bug/123 --no-ff 
#  O
#  |\
#  | |
#  | O bug/123
#  | |
#  |/
#  O master*
```


---
## git merge 「3-way merge」
因為分支與 master 都有各自 commit了, 導致彼此的歷史沒有重疊
```sh
#         O 
#         |\
#         O | 
#         | O bug/123*
#  master O
$ git checkout master
$ git merge bug/123
#         O 
#         |\
#         O | 
#         | O bug/123
#         O |
#         |/
#         O master*
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

$ git rebase --abort        # rebase分兩段, 第一段結束後, 要放棄 rebase
$ # git rebase --continue   # 解決完第一段 rebase衝突後

$ git cherry-pick --abort
```


---
## git reflog(小烏龜)
Reflow是 HEAD變動的歷史紀錄


---
## git rebase
```sh

```



# C. Git 組態

## 層級
LEVEL  | option   | Path           | Description
------ | -------- | -------------- | -------------------------
Local  | --local  | .git/config    | 只對目前的repo有效(預設)
User   | --global | ~/.gitconfig   | 對目前使用者有效
System | --system | /etc/gitconfig | 對所有使用者/儲存庫都有效


## 查詢、設定、移除
```sh
# 查詢組態
$ git config -l
$ git config -l --system
$ git config -l --global
$ git config -l --local
$ git config  <Config_Section.Config_Name> # 顯示特定組態

# 設定組態
$ git config --global user.name "TonyCJ"
$ git config --global user.email "cool21540125@gmail.com"

# 忽略「空白」所造成的影響
$ git config --global apply.whitespace nowarn

# 增加Git輸出時的顏色
$ git config --global color.ui true
```


## 查詢、設定、移除 別名
> *設定別名* : `git config --<層級> alias.<縮寫名稱> <原始指令>`

> *移除別名* : `git config --<層級> --unset alias.<已建立的別名>`
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
## .gitignore - 取消追蹤
```
*.txt        # 不要追蹤所有 txt檔
!note.txt    # 但是排除 note.txt(要追蹤)
```


---
## 更改 remote repo
```sh
$ git remote -v
origin  https://github.com/cool21540125/illu.git (fetch)
origin  https://github.com/cool21540125/illu.git (push)

$ git remote set-url origin git@github.com:cool21540125/documentation-notes.git
Verify that the remote URL has changed.

$ git remote -v
origin  git@github.com:cool21540125/documentation-notes.git (fetch)
origin  git@github.com:cool21540125/documentation-notes.git (push)
```






# D. 操作指令
## 選項
選項 | 說明 | 範例 
--- | --- | ---
-s | 簡易資訊 | git status -s


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
## git stash 暫存版
- `git stash` 已追蹤 的檔案 建立暫存版 (同 `git stash save`)
- `git stash -u`　已追蹤 + 未追蹤 的檔案 建立暫存版 

- [參考這邊](https://github.com/doggy8088/Learn-Git-in-30-days/blob/master/zh-tw/13.md)
- [保證簡單好懂得範例](./stash_example.txt)


---
## git reset 改變範圍
param   | data in repo | git index | file in dir
------- |:------------:|:---------:|:------------:
--soft  | v            |           | 
--mixed | v            | v         | 
-- hard | v            | v         | v
## 建立新的git repo
> 參考: [共用儲存庫](https://ithelp.ithome.com.tw/articles/10132804)
```sh
$ git init
$ git init --bare
```



---
## 遠端分支
> 
```sh
$ git config -l | grep master
branch.master.remote=origin
branch.master.merge=refs/heads/master
```


```sh
# 查看本地/遠端分支
$ git branch -a
* develop
  logging
  master
  remotes/origin/logging
  remotes/origin/master
```
---
## 修改 Commit訊息
```sh
$ git commit --amend -m "<Commit String>"
```


---
## 鎖定遠端repo、遠端repo追蹤
> 加入 remote repository, 語法: `git remote add origin <遠端repo>`

script                             | Description
---------------------------------- | ------------
`git push origin <branch name>`    | 把指定分支的最新狀態, 推送到 remote repo
`git push -u origin <branch name>`<br>( `-u` 可改成 `--set-upstream` ) | (同上), <br>且會在設定檔內紀錄「本地 repo分支」與「遠端 repo分支」的對應關係

```sh
$ git init
$ git add README.md
$ git commit -m 'xxx'
$ git remote -v
#(沒東西)

$ git remote add origin https://github.com/cool21540125/tttt.git

$ git remote -v
remote.origin.url=https://github.com/cool21540125/tttt.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*

$ git push -u origin master
```


---
## 加入至stage狀態
[git add 差異說明](https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add)

> ※ 以下 `不保證完全正確`, 因為有版本問題...

script | New Files | Modified Files | Deleted Files | Sub-Folder Files
--- |:---:|:---:|:---:|:---:
git add -A | V | V | V | V
git add . | V | V | **`X`** | **`X`**
git add -u | **`X`** | V | V | ?

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

## 查詢歷史紀錄
> 語法: `git reflog <branchName>` , 查詢任何分支變動的歷史紀錄<br>
  若只有打 `git reflog` or `git reflog HEAD`, 則表示列出 HEAD變動的歷史紀錄
```sh
$ git reflog HEAD
5fc27fb (HEAD -> master, origin/master, origin/HEAD) HEAD@{0}: commit: fix git.md
b333f91 HEAD@{1}: commit: modify docker, i18n, html, linux, ubuntu1604
65251ea HEAD@{2}: commit: ADD html.md
a41e99a HEAD@{3}: commit: sql.md
ac69d3f HEAD@{4}: pull: Merge made by the 'recursive' strategy.
# 上頭的 : commit:, 表示是 commit所導致的變動, 另外還有 rebase, pull, ...等

# 若要回到以前的狀態 ac69d3f
$ git reset --hard HEAD@{4}
# 慎用 --hard
```

---
# E. 其他零碎片段

> `沒有工作目錄的儲藏庫`(no working tree / no working directory), 為 「bare repository」

> `index` 的目的: 用來記錄「那些檔案即將被提交到下一個 Commit版本中」

```sh
# 把被改壞的檔案, 還原回它當時在此 branch的狀態, 如此可避免使用「git reset --hard」
$ git checkout <branch> <fileName>

# -f 選項直接讓分支指向另一個 commit
$ git branch -f master HEAD~3
```
# Git相關指令
- 架設Git Server
- git相關指令

參考
- [git book - --local-branching-on-the-cheap](https://git-scm.com/book/zh-tw/v2)

---

## 1. Git Server


## 2. Git相關指令

### - 安裝Git後, 首先需要做的事情就是設定使用者

```
$ git config --global user.name "<Your Name>"
$ git config --global user.email "<Your e-mail>"
```

### - Git環境 組態參數

組態檔可能存在於3個地方

    a. /etc/gitconfig
    b. ~/.gitconfig、~/.config/git/config
    c. 專案裏頭的.git/config




```$ git config <para>```
| para | 說明 |
| --- | --- |
| --global |  |
| --system |  |
| --local |  |
| --blob |  |
| --f |  |
| --list | 顯示組態設定值 |

## 紀錄變更

```
$ git status
$ git status -s

把不加入追蹤的檔案, 放到.gitignore中
$ cat .gitignore
```




---
更新日期 2017/09/24, by Tony
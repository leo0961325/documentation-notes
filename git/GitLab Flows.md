# GitLab 的 git

- 2020/01/21

## 基本觀念

- GitLab 的 `Merge Request` = GitHub 的 `Pull Request`


## Commit

```bash
### 1. GitLab 上, 建立一個 Issue (ex: #118)

### 2. 建立關聯 此稱為 首次關聯(First Commit)
$# git commit -m "XXX Ref: #118"  # 同專案
# 或
$# git commit -m "XXX https://gitlab.com/<username>/<projectname>/issues/#118>"  # (跨專案)
$# git push

### 結果
# 會建立 issue 與 first commit 之間的關聯
```

> 建立 MR 後, 處理完裡面關聯的 Issue 後才可 Merge MR
>
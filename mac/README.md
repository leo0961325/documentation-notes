# Tips for Mac

### 安裝 tab-completion
```bash
$# brew install bash-completion
$# [ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion
```

### 修改畫面截圖路徑
```bash
$# mkdir ~/Desktop/screenshots/
$# defaults write com.apple.screencapture location ~/Desktop/screenshots/
```

### jq
```bash
$# brew install jq
$# curl https://randomuser.me/api/ | jq  # 交由 jq 做解析(會做 beauty)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1179    0  1179    0     0   1548      0 --:--:-- --:--:-- --:--:--  1547
{
  "results": [
    {
      "gender": "female",
      "name": {
        "title": "Mrs",
        "first": "Crystal",
        "last": "Garcia"
      },
      "location": {
        "street": {
          "number": 2127,
...(略)...

$# $ curl https://randomuser.me/api/ | jq '.results[0].name'  # 可作 filter
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1147    0  1147    0     0   1525      0 --:--:-- --:--:-- --:--:--  1523
{
  "title": "Miss",
  "first": "Mia",
  "last": "Smith"
}

```
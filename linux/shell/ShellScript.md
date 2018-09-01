
## RH134-RHEL7-en-1-20140610, p64 範例

```sh
# 若一次性排程工作 > 0, bash 就睡覺吧~
while [ $(atq | wc -l) -gt 0 ]; do sleep 1s; done
```
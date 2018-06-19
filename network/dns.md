# DNS
- 2018/06/12

> DNS NameSpace:
將 IP 服務等命名, 並使用階層結構將這些名字組織起來的結果

> DNS Domain:
在 DNS NameSpace中, 可含有下層的節點 => `共用相同識別尾碼`的東西的集合

> DNS Zone:
為分散管理, 在 DNS NameSpace 切割出的連續區域. 不同的 Zone必有各自的 database(file 或 AD 中的容器) 儲存自己 Zone 中的 Records. 不同的　Zone可由不同組人管理.

> Fully Qualified Domain Name(FQDN):
在 DNS NameSpace中, 節點的完整名稱. 轉換規則: 由下往上, 每層加「.」區隔

```
Internet DNS Namespace(部分)
|- com 
|- org 
|- gov 
|- mil 
|- edu 
|- net 
|- arpa 
|- tw 
|- jp 
|- us 
|- ...
```

Zone Type | 每個 Zone | 有完整的內容 | 管理者權限 | 用途
--------- | --- | --- | --- | --- | --- | ---
paimary(Master file) | 1個 | Y | R/W | 讓管理者管理 Zone 中的 Resource Record 提供 client 或其他 DNS Server 查詢
secondary () | N個 | Y | Readonly | 會分擔 Primary Zone 的 DNS Server(Master Server) 的負擔, 或在 Primary Zone 的 DNS Server 故障時仍能提供查詢
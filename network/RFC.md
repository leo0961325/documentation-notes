# RFC 文件

<details>
    <summary> RFC List... </summary>

- [rfc2119](#rfc2119) - Key words for use in RFCs to Indicate Requirement Levels
- [rfc2616](#rfc2616) - Hypertext Transfer Protocol -- HTTP/1.1
- [rfc7540](#rfc7540) - Hypertext Transfer Protocol Version 2 (HTTP/2)
</details>



# [rfc2119](https://www.ietf.org/rfc/rfc2119.txt)

## Key words for use in RFCs to Indicate Requirement Levels

- 2018/08/10

> 這篇只是在定義 `RFC 文件們` 用詞的定義

term        | Description
----------- | ---------------------------
MUST        | absolute requirement
SHOULD      | 建議應該怎麼做
MAY         | 可有可無
REQUIRED    | (同 MUST)
SHALL       | (同 MUST)
RECOMMENDED | (同 SHOULD)
OPTIONAL    | (同 MAY)



# [rfc2616](https://www.ietf.org/rfc/rfc2616.txt)

## Hypertext Transfer Protocol -- HTTP/1.1

> HTTP/1.1 的第一篇創始文章, 由 (1997) 發表至今 (2018), 仍是 internet 主流協定.



# [rfc7540](https://www.ietf.org/rfc/rfc7540.txt)

## Hypertext Transfer Protocol Version 2 (HTTP/2)

> 

- `HTTP/2` 為 `HTTP/1.1` 的 替代方案
- `HTTP/2` 藉由引入 「header field compression(表頭壓縮)」 及 「allow multiple concurrent exchange on the same(允許共時)」來提升網路傳輸效能, 減少前端網路延遲的知覺.
- `HTTP/1.0` && `HTTP/1.1` 過大的 `http header` 容易造成 `TCP congestion`, 因而 `HTTP/2` 允許 相同連線上 交錯 `request` 與 `response message`, 並允許對 `request` 作優先級別的排序
    - `HTTP/1.0` : 相同時間內, 只能有一個 `TCP connection`
    - `HTTP/1.1` : 相較於 `1.0`, 增加了 `request pipeline`, 部份解決 `addressed request concurrency`



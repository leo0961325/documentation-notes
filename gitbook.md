# [GitBook](https://wastemobile.gitbooks.io/gitbook-chinese/content/index.html)

## 設定檔
* 對一本書的所有設定，都以 JSON 格式寫在 `book.json` 檔案中

扮演 README 的角色名稱, 可以改變的架構設定有： readme, langs, summary 與 glossary
```
{
    "structure": {
        "readme": "myIntro.md"
    }
}
```



書名
```
{ "title": "My Awesome Book" }
```

設定變數
```
{
    "variables": {
        "myVariable": "Hello World"
    }
}
```


書籍簡介, 預設值是 README 檔案中的第一個段落內容
```
{ "description": "This is such a great book!" }
```

書籍的 ISBN
```
{ "isbn": "978-3-16-148410-0" }
```

語言
```
{ "language": "en" }
```

設定對應的 CSS 樣式表
```
{
    "styles": {
        "website": "styles/website.css",
        "ebook": "styles/ebook.css",
        "pdf": "styles/pdf.css",
        "mobi": "styles/mobi.css",
        "epub": "styles/epub.css"
    }
}
```

設定本書使用到的外掛
```
{ "plugins": ["mathjax"] }
```

## 目錄架構 (Tables Of Contents)
* 使用 `SUMMARY.md` 來定義書籍的 TOC

---
多語言版本 `LANGS.md`
```md
* [中文版](ch/)
* [English](en/)
* [French](fr/)
* [Español](es/)
```

## 內容參照（Content referencing - conref）
```md
 {% include "./test.md" %}

 {% include "git+https://github.com/GitbookIO/documentation.git/README.md#0.0.1" %}
 ```
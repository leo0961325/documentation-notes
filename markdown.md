# GitBook
[GitBook中文解說 - 2.4](https://wastemobile.gitbooks.io/gitbook-chinese/content/format/chapters.html)

---


GitBook的 `SUMMARY.md` 

- 定義書籤的目錄架構(多層次章節的設定). 

- 製作**書籍目錄**(Tables Of Contents, TOC).

- 只是簡單的連結表格, 「連結的名稱」只是「章節的標題」, 連結標的則是「實際內容的檔案(包含路徑)」.

- 
---

部、章、節、小節

範例
```
# Summary

* [第一章](chapter1.md)
* [第二章](chapter2.md)
* [第三章](chapter3.md)
```

```
# Summary

* [第一部](part1/README.md)
    * [寫作是美好的](part1/writing.md)
    * [GitBook 也不錯](part1/gitbook.md)
* [第二部](part2/README.md)
    * [我們歡迎讀者回饋](part2/feedback_please.md)
    * [對作者更好的工具](part2/better_tools.md)
```


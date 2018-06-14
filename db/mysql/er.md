# ER-Model 資料庫規劃
- 2018/06/13

- [關於 Cascade](https://dba.stackexchange.com/questions/44956/good-explanation-of-cascade-on-delete-update-behavior?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

> 若兩個 Table, `Parent` 及 `Child`, 如果 **Foreign Key** 已經被定義為 `ON DELETE CASCADE`, 表示一旦 `Parent` 的 **Primary Key** 被移除後, 則不留孤兒. 而 `ON DELETE RESTRICT` 放在 **Foreign Key** 則表示, 需要把 `Child` 淨空之後, 才可以殺 `Parent`.
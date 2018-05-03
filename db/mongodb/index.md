# MongoDB Index
- 2018/05/03
- 這篇應該不會寫得很認真

```js
// 取得 coll 的索引
db.coll.getIndexes();
{
	"v" : 2,
	"key" : {
		"_id" : 1
	},
	"name" : "_id_",
	"ns" : "pome.status"
}
```
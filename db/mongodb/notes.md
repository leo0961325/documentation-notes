# pymongo

```sh
$ pip freeze | grep pymongo
pymongo==3.5.1
```

```py
>>> a = datetime.datetime.utcnow()
>>> a
datetime.datetime(2017, 11, 30, 7, 55, 57, 756000)

# 塞到 MongoDB後
>>> insert({ 'dt': a })
```

```mongo
ISODate("2017-11-30T07:55:57.756Z")
```


# MongoDB Index

- 2018/05/03
- 這篇應該不會寫得很認真

```js
// 附加 index
db.coll.createIndex({'_id': -1});

// 取得 coll 的索引
db.coll.getIndexes();
{
	"v" : 2,
	"key" : {
		"_id" : 1
	},
	"name" : "_id_",
	"ns" : "db_name.status"
}
```



# pymongo join

```py
>>> db2.users.insert_one({
    "_id": "Tom Benzamin",
    "addresses": ['addr A', 'addr B']
})
<pymongo.results.InsertOneResult at 0x17f6d334788>
```

```py
>>> db2.address.insert_many([{
        "_id": "addr A",
        "building": "22 A, Indiana Apt",
        "pincode": 123456,
        "city": "Los Angeles",
        "state": "California"
    }, {
        "_id": "addr B",
        "building": "170 A, Acropolis Apt",
        "pincode": 456789,
        "city": "Chicago",
        "state": "Illinois"
    }
])
<pymongo.results.InsertManyResult at 0x17f6d334f08>
```

```py
>>> result = db2.users.find_one({'_id': 'Tom Benzamin'})

>>> addr = db2.address.find({'_id': {'$in': result['addresses']}})
>>> list(addr)
[
    {
        '_id': 'addr A',
        'building': '22 A, Indiana Apt',
        'city': 'Los Angeles',
        'pincode': 123456,
        'state': 'California'
    },{
        '_id': 'addr B',
        'building': '170 A, Acropolis Apt',
        'city': 'Chicago',
        'pincode': 456789,
        'state': 'Illinois'
    }
]
```


# [$addToSet](https://docs.mongodb.com/manual/reference/operator/update/addToSet/)
- v3.6

- [MongoDB - Update objects in a document's array (nested updating)
](https://stackoverflow.com/questions/10522347/mongodb-update-objects-in-a-documents-array-nested-updating)

### 原始資料
```js
db.bar.remove({_id: 123});

db.bar.insertOne({
    _id : 123,
    total : 100,
    items : [
        { name : "A", price : 20 },
        { name : "B", price : 50 },
        { name : "C", price : 30 }
    ]
});

db.bar.find({}, {_id: 0});
```

### Q1. 更改 name=A者, 價格+1 並且更新 total
```js
db.bar.update(
    { "items.name": { $eq: "C"} }, 
    { $inc: { total: 1, "items.$.price": 1}}, 
    false, 
    true
);
```

### Q2. name=D, 價格 70(如果沒有的話就新增)
```js
db.bar.update(
    {"items.name": { $ne: "D" }}, 
    { $addToSet: { "items": { "name": "D", "price": 70 }}}, 
    false, 
    true
);
```

### Q3. name=D, 價格 80(如果沒有的話就新增)
```js

```
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
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



# MongoDB 以前用過但懶得整理...

```js
cursor = db.test.find()

while (cursor.hasNext()) {
    x = cursor.next()
    print(x._id)
}
```


```js
// 更改舊 document, 新增 kv到 sub-document
// { "_id": 1, "people": {"name": "tony" } }
db.test.update({_id: 1}, { $set: {'people.country': 'taiwan'}})
// { "_id": 1, "people": {"name": "tony" , "country": "taiwan" } }
```


```js
// 更改舊 document, 新增
// { "_id" : 1, "foo" : "bar", "obj" : { "status" : "new", "country" : "eu" } }
// { "_id" : 2, "foo" : "bar", "obj" : { "status" : "new" } }
db.test.updateMany({'_id': 1}, { $set: { 'obj.country' : 'eu'}} )
// { "_id" : 1, "foo" : "bar", "obj" : { "status" : "new", "country" : "eu" } }
// { "_id" : 2, "foo" : "bar", "obj" : { "status" : "new" } }
```


```js
// 更改舊 document, 更改 sub-document 的 value
// { "_id" : 1, "foo" : "bar", "obj" : { "status" : "new", "country" : "eu" } }
// { "_id" : 2, "foo" : "bar", "obj" : { "status" : "new", "country" : "tw" } }
// { "_id" : 3, "foo" : "bar", "obj" : { "status" : "new", "country" : "tw" } }
db.test.updateMany({'obj.country': 'tw'}, { $set: { 'obj.country': 'taiwan'}   } )
// { "_id" : 1, "foo" : "bar", "obj" : { "status" : "new", "country" : "eu" } }
// { "_id" : 2, "foo" : "bar", "obj" : { "status" : "new", "country" : "taiwan" } }
// { "_id" : 3, "foo" : "bar", "obj" : { "status" : "new", "country" : "taiwan" } }

// 找  系列燈號表
db.status.find({'context': 'lightTable', '': '800系列'}, {'_id': 0, 'context': 0, 'lightTable.light': 0, 'towerLightNumber': 0}).pretty();

// 刪除燈號表
db.status.deleteOne({'context': 'lightTable', '': '800系列'});

// 對 array內部做pull || push 語法
db.status.update({'context': 'lightTable', '': '800系列', 'lightTable.status': 'PM'}, {$push: {'lightTable.$.light': '222'}});
db.status.update({'context': 'lightTable', '': '800系列', 'lightTable.status': 'undefined'}, {$pull: {'lightTable.$.light': '222'}});

// 
db.status.find({}, {'_id': 0});
db.status.find({'context': 'light'}, {'_id': 0});
db.status.find({'context': 'light'}, {'_id': 0, 'context': 0});
db.status.find({'context': 'lightTable'}, {'_id': 0, 'context': 0, 'lightTable.light': 0});
db.status.find({'context': 'lightTable', '': '800系列'}, 
        {'_id': 0, 'context': 0, '': 0, 'towerLightNumber': 0}).pretty();

// 
db.status.aggregate([ 
    {'$match': {'context': 'light'}}, 
    {'$project': {'arrayofkeyvalue': {'$objectToArray': "$$ROOT"}}}, 
    {'$unwind':"$arrayofkeyvalue"}, 
    {'$group':{'_id':'null', 'allkeys':{'$addToSet':"$arrayofkeyvalue.k"}}}
]);

// jsohua給的 update
db.menu.update_one({'machine': 'HITACHI MS-510_1','sensorMenu.type': 'towerLight'}, 
                   {'$set': {'sensorMenu.$.towerLightSeries':'800系列'}},
                   upsert=True)

// 找出所有機器內含 towerLight的機器資訊
db.menu.find({'sensorMenu.type':'towerLight'}, {'_id': 0, 'enable': 0, 'machineID': 0, 'productionLine': 0, 'buildDate': 0, 'sensorMenu.sensorID': 0, 'sensorMenu.enable': 0});

// 修改顏色
db.towerLight.update(
    { _id: { $eq: pk } },
    { $set: { color: color }}
)

// 新增 kv到 towerLight
db.towerLight.update(  
    { 'cn': '機台閒置' }, 
    { $set: {'900系列': '000'}}
)

// 從 towerLight刪除 kv
db.towerLight.update(
    { '900': '000' }, 
    { $unset: {'900': ''} }
)

// 查machineMenu 的燈號元件的資訊
db.machineMenu.aggregate([{'$unwind': '$sensorMenu'}, {'$match': {'sensorMenu.type': 'towerLight'}},{'$project': {'_id':0, 'sensorMenu.id':0, 'company':0, 'factory':0, 'productionLine':0, 'model':0, 'machine':0, 'enable':0, 'sensorMenu.enable': 0, 'sensorMenu.cn':0}}])
/*
{ "sensorMenu" : { "sensor" : "towerLight_1", "displayMode" : "800系列", "type" : "towerLight" } }
{ "sensorMenu" : { "sensor" : "towerLight_1", "displayMode" : "800系列", "type" : "towerLight" } }
*/

// 
db.machineMenu.aggregate([
    {'$unwind': '$sensorMenu'}, 
    {'$match': {'sensorMenu.type': 'towerLight'}},
    {'$project': {'sensor':'$sensorMenu.sensor', 'displayMode': '$sensorMenu.displayMode', '_id':0}},
])

// 更改 key的名字
db.towerLight.updateMany({}, {'$rename': { '500系列': 'default' }})

// 有displayMode這個欄位的資料
db.dataMenu.find({displayMode:{$exists: true}});    

// 若sensorMenu.type = 'counter', 增加 sensorMenu.cn = '計數器'
db.machineMenu.updateMany( { 'sensorMenu.type':'counter' },   {  '$set': {'sensorMenu.$.cn':'計數器'}  } );

db.machineMenu.updateMany( {'sensorMenu.type': 'towerLight'},  { '$set': {'sensorMenu.$.displayMode': '800系列'}})
```

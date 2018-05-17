# MongoDB 語法備註
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
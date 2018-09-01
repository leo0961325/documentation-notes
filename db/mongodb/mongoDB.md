# MongoDB

## linux環境使用mongo

```sh
$ mongod --dbpath ~/mongodb                     #自定義路徑，儲存data files
$ mongod --fork --logpath ~/log/mongodb.log     #背景執行，並且把log寫入指定log檔
```


## mongodb權限管理

因mongodb預設安裝好後是沒有保護機制的，需自行建立登入機制保護資料

```js
use admin;
db.createUser({user:"root",pwd:"password123",roles:[{role:"root",db:"admin"}]});
// 這樣就有一個root帳號了!

// 接著創建專屬資料庫的帳號
use test;

// 擁有管理者權限
db.createUser({user:"admin",pwd:"password123",roles: [{ role: "readWrite", db: "test" }]});

// 擁有使用者權限
db.createUser({user:"user",pwd:"password123",roles: [{ role: "read", db: "test" }]});
// 登出 MongoDB

// 登入 MongoDB 再進 MongoDB 就要使用 帳號密碼 登入
mongod --auth --fork --dbpath ~/mongodb --logpath ~/log/mongodb.log
```


登入遇到

1. about to fork child process, waiting until server is ready for connections ERROR: child process failed, exited with error number 100 - 因為mongodb不正常關閉，刪除DBPATH裡的mongod.lock文件
2. ERROR:  child process failed ,exited with error number 1 - 增加DBPATH的寫入權限即可


```js
use admin;
db.auth("root", "password123");         // 以root登入
use test;
db.auth("admin", "password123");        // 以admin權限登入test資料庫(讀寫皆可)
db.auth("user", "password123");         // 以user權限登入test資料庫(只能讀)
```



# 規劃實務

- [MongoDB Schema 設計指南](https://blog.toright.com/posts/4483/mongodb-schema-%E8%A8%AD%E8%A8%88%E6%8C%87%E5%8D%97.html)
- 2017/12/01


### Child-Referencing

單一 Document內的子元素, 可能有上百個, 可用 Child-Referencing ( `資料主角`紀錄`子文件`位置 )

```js
// 模擬資料
db.parts.insertMany([
    {"_id": "q1", "qty":94,  "cost": 0.94, "price": 3.99, "address": "tw" },
    {"_id": "q2", "qty":23,  "cost": 0.38, "price": 1,    "address": "cn" },
    {"_id": "q3", "qty":322, "cost": 1.58, "price": 400,  "address": "jp" }
]);
db.main.insertOne({"_id": "tony", "age": 30,"has": [ "q1", "q2", "q3" ]});

// 查詢方式
owner = db.main.findOne({_id: 'tony'});
qry = db.parts.find({_id: { $in:  owner.has }});
// { "_id" : "q1", "qty" : 94, "cost" : 0.94, "price" : 3.99, "address" : "tw" }
// { "_id" : "q2", "qty" : 23, "cost" : 0.38, "price" : 1, "address" : "cn" }
// { "_id" : "q3", "qty" : 322, "cost" : 1.58, "price" : 400, "address" : "jp" }
```


### Parent-Referencing

單一 Document內的子元素, 可能有巨量級資料, 可用 Parent-Referencing ( 每筆`子文件`紀錄`資料主角`位置 )

```js
// 模擬資料
db.hosts.insertOne({_id:"ObjectID('AAAB')",name:'goofy.example.com',ipaddr:'127.66.66.66'});
db.logmsg.insertOne({time:new Date(),message:'cpuisonfire!',host:"ObjectID('AAAB')"});

// 尋找方式
host = db.hosts.findOne({ipaddr: '127.66.66.66'});
qry = db.logmsg.find({host: host._id}).toArray();
// [
//         {
//                 "_id" : ObjectId("5a214ed99dc338934f58000c"),
//                 "time" : ISODate("2017-12-01T12:45:13.206Z"),
//                 "message" : "cpuisonfire!",
//                 "host" : "ObjectID('AAAB')"
//         }
// ]
```


### Two-Way Referencing

兩邊資料都剖大, 有可能雙向查找

> 優點: 查找容易<br />
  缺點: 更新時, 需要一次更新兩個地方, `必須手動同步關聯狀態`.
```js
// 模擬資料 使用者 對應 工單
db.person.insertOne({_id:"ObjectID('AAF1')",name:"KateMonster",tasks:["ObjectID('ADF9')","ObjectID('AE02')","ObjectID('AE73')"]})
db.tasks.insertOne({_id:"ObjectID('ADF9')",description:"Writelessonplan",due_date:new Date(),owner:"ObjectID('AAF1')"})
```


### Intermediate (媒介設計模式)

#### 多對一反正規化

```js
// 模擬資料
db.products.insertOne({_id:'left-handedsmokeshifter',manufacturer:'AcmeCorp',catalog_number:1234,parts:[{id:"ObjectID('F17C')",name:'fanbladeassembly'},{id:"ObjectID('D2AA')",name:'powerswitch'}]});
db.parts.insertMany([{_id:"ObjectID('AAAA')",name:'#4grommet'},{_id:"ObjectID('F17C')",name:'fanbladeassembly'},{_id:"ObjectID('D2AA')",name:'powerswitch'}])

// 以 products.parts.id為清單, 找到對應的 parts._id 的詳細資訊, 運用的技巧稱為 Application-level Join
product = db.products.findOne({catalog_number: 1234});
part_ids = product.parts.map( function(doc) { return doc.id } );
product_parts = db.parts.find({_id: { $in : part_ids } } ).toArray();
```


### aggregate + update

- [Aggregation with update in mongoDB](https://stackoverflow.com/questions/19384871/aggregation-with-update-in-mongodb)
- 2017/12/13

```js
// 1. 
> db.agg.insertMany([{ 
    "_id": ObjectId("525c22348771ebd7b179add8"), 
    "cust_id": "A1234", 
    "score": 500, 
    "status": "A",
    "clear": "No"
},{ 
    "_id": ObjectId("525c22348771ebd7b179add9"), 
    "cust_id": "A1234", 
    "score": 1600, 
    "status": "B",
    "clear": "No"
}]);

// 2.
> db.agg.find();
{ "_id" : ObjectId("525c22348771ebd7b179add8"), "cust_id" : "A1234", "score" : 500, "status" : "A", "clear" : "No" }
{ "_id" : ObjectId("525c22348771ebd7b179add9"), "cust_id" : "A1234", "score" : 1600, "status" : "B", "clear" : "No" }

// 3a.
var gg = db.agg.aggregate([
    {'$match': { '$or': [{'status': 'A'}, {'status': 'B'}]}},
    {'$group': {'_id': '$cust_id', 'total': {'$sum': '$score'}}},
    {'$match': {'total': {'$gt': 2000}}}
]);

// 3b.
gg.forEach(function(x) {
        db.agg.update({'cust_id': x._id}, {'$set': {'clear': 'YES'}}, {'multi': true});
    }
);

// result
> db.agg.find();
{ "_id" : ObjectId("525c22348771ebd7b179add8"), "cust_id" : "A1234", "score" : 500, "status" : "A", "clear" : "YES" }
{ "_id" : ObjectId("525c22348771ebd7b179add9"), "cust_id" : "A1234", "score" : 1600, "status" : "B", "clear" : "YES" }
```

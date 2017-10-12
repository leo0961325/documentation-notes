# MongoDB
- mongoDB on Windows 10
- 版本資訊如下
```cmd
> mongo --version
MongoDB shell version v3.4.9
git version: 876ebee8c7dd0e2d992f36a848ff4dc50ee6603e
OpenSSL version: OpenSSL 1.0.1u-fips  22 Sep 2016
allocator: tcmalloc
modules: none
build environment:
    distmod: 2008plus-ssl
    distarch: x86_64
    target_arch: x86_64
```


下載完mongoDB後，加入環境變數後，開啟CMD

>> mongod --dbpath d:\mongodb\data\db(自定義的資料夾，該資料夾會記錄DB的訊息)

再開啟另一個CMD
>> mongo 即可使用mongoDB

## 安裝 MongoDB服務

在剛剛mongodb的目錄下，建立`mongod.cfg`, 內容如下:
```txt
systemLog:
    destination: file
    path: d:\mongodb\data\log\mongod.log
storage:
    dbPath: d:\mongodb\data\db
```

接著以管理員身分打開CMD, 安裝服務、啟動服務
```cmd
> mongod --config D:\mongodb\mongod.cfg --install
> net start MongoDB (啟動服務)
```

其他相關指令如下, 
```cmd
> net start MongoDB (關閉服務)

若遇到啟動失敗，可試著刪除db/mongod.lock，接著執行
> mongod --config D:\mongodb\mongod.cfg --remove
> mongod --config D:\mongodb\mongod.cfg --install
```

## linux環境使用mongo
```sh
$ mongod --dbpath ~/mongodb                     #自定義路徑，儲存data files
$ mongod --fork --logpath ~/log/mongodb.log     #背景執行，並且把log寫入指定log檔
```

# 三種關閉mongod的方式
* use admin #在mongo shell裡      
db.shutdownServer()
* mongod --shutdown
* kill -2 (mongod process ID)

## mongodb權限管理
因mongodb預設安裝好後是沒有保護機制的，需自行建立登入機制保護資料<br>
```js
use admin
db.createUser({user:"root",pwd:"PASSWORD",roles:[{role:"root",db:"admin"}]})
// 這樣就有一個root帳號了!
```

```js
// 接著創建專屬資料庫的帳號
use test

// 擁有管理者權限
db.createUser({user:"admin",pwd:"PASSWORD",roles: [{ role: "readWrite", db: "test" }]}) 

// 擁有使用者權限，接著登出
db.createUser({user:"user",pwd:"PASSWORD",roles: [{ role: "read", db: "test" }]}) 

// 這時候在進mongodb就要使用帳號密碼登入
mongod --auth --fork --dbpath ~/mongodb --logpath ~/log/mongodb.log 
'''

'''
登入遇到
1.about to fork child process, waiting until server is ready for connections，
ERROR: child process failed, exited with error number 100
因為mongodb不正常關閉，刪除DBPATH裡的mongod.lock文件
2.ERROR:  child process failed ,exited with error number 1
增加DBPATH的寫入權限即可
```

```js
use admin
db.auth("root", "PASSWORD")         // 以root登入
use test
db.auth("admin", "PASSWORD")        // 以admin權限登入test資料庫(讀寫皆可)
db.auth("user", "PASSWORD")         // 以user權限登入test資料庫(只能讀)
```

## 基本操作
show dbs<br>
* Collections List<br>
1. show collections<br>
2. show tables<br>
3. db.getCollectionNames()<br>
use (database name) #沒有該名稱資料庫就創建，若有就切換到該資料庫<br>
* Create Operations<br>
1. db.collection.insertOne() #創建一筆資料<br>
2. db.collection.insertMany() #創建多筆資料(list)
* Read Operations<br>
1. db.collection.find()
* Update Operations<br>
1. db.collection.updateOne()<br>
2. db.collection.updateMany()<br>
3. db.collection.replaceOne()
* Delete Operations<br>
1. db.collection.deleteOne()<br>
2. db.collection.deleteMany()


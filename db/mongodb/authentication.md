# MongoDB 權限機制
- 2018/05/21
- MongoDB v3.4、v3.6
- [Official - Enable Auth](https://docs.mongodb.com/v3.4/tutorial/enable-authentication/)
- [MongoDB user role設定筆記](https://www.facebook.com/notes/%E9%84%AD%E6%A5%AD%E8%96%B0/%E5%B7%A5%E4%BD%9C%E7%AD%86%E8%A8%98mongodb-user-role%E8%A8%AD%E5%AE%9A%E7%AD%86%E8%A8%98/10152402345234468/)
- [MongoDB建立資料庫使用者帳號](https://ithelp.ithome.com.tw/articles/10113778)
- [官方 Built-In Roles](https://docs.mongodb.com/v3.4/reference/built-in-roles/)

-------------------------------------

# [幫 MongoDB 搞權限](https://docs.mongodb.com/v3.4/tutorial/enable-authentication/#overview)

管理權限的 Database `admin`, 一開始需要在裡面創建一個使用者(名字應該隨便吧@@?), 要賦予 `userAdmin` or `userAdminAnyDatabase` 的權限. 如此一來, This user can administrate user and roles such as: create users, grant or revoke roles from users, and create or modify customs roles.


幾個關鍵性的名詞
- roles
- users
- resources
- databases


## Roles - 分為 2 類
### 1. ~~User-Defined Roles~~ (pass)

### 2. [Built-In Roles](https://docs.mongodb.com/v3.4/reference/built-in-roles/)
- userAdmin
- userAdminAnyDatabase - 只能管控 users 和 roles, 無法作 collection 的 CRUD
- manageOpRole

```
+ Database User Roles
+ Database Admin Roles
+ Cluster Admin Roles
+ BackupandRestoration Roles
+ All-DB Roles
+ Superior-Roles
+ Internal Roles
```



## [官方範例](https://docs.mongodb.com/v3.4/tutorial/enable-authentication/#procedure)

1. 建立 Mongo Daemon
```sh
# 這底下的資料夾盡量是空的, 玩壞了以後, 可以整個刪除XD
# 當然, 服務得先關掉
$ mongod --port 27017 --dbpath /tmp/qq
```

2. 進入 mongodb
```sh
$ mongo --port 27017
```

3. 開始搞權限
```js
> use admin
> db.createUser({
    user: 'myUserAdmin',
    pwd: 'abc123',
    roles: [
        { role: 'userAdminAnyDatabase', db: 'admin' }
    ]
});
// 底下是回傳值... (不是指令)
Successfully added user: {
    "user" : "myUserAdmin",
    "roles" : [
        {
            "role" : "userAdminAnyDatabase",
            "db" : "admin"
        }
    ]
}
// 完成後離開 mongodb
// 這時候, 「/tmp/qq/」 裏頭, 會多出一大堆莫名其妙的東西
```

4. 再次使用權限進入
```sh
$ mongod --auth --port 27017 --dbpath /tmp/qq
```

5. 使用剛建立的 `myUserAdmin` User 登入
```sh
$ mongo --port 27017 -u "myUserAdmin" -p "abc123" --authenticationDatabase "admin"
```
或者, 使用 `mongo` 進入 MongoDB, 再進行權限驗證
```js
> db.auth({user: 'myUserAdmin', pwd: 'abc123'})
1       // 權限驗證成功
```

6. 建立其他的 user
```js
> use test
> db.createUser(
  {
    user: "myTester",
    pwd: "xyz123",
    roles: [ { role: "readWrite", db: "test" },
             { role: "read", db: "reporting" } ]
  }
)
// return 
Successfully added user: {
    "user" : "myTester",
    "roles" : [
        {
            "role" : "readWrite",
            "db" : "test"
        },
        {
            "role" : "read",
            "db" : "reporting"
        }
    ]
}
```

7. 使用剛建立的 `myTester` User 登入

```sh
$ mongo --port 27017 -u "myTester" -p "xyz123" --authenticationDatabase "test"
```
或者, 用 `mongo` 進入 MongoDB, 再進行權限驗證
```js
> user test
> db.auth("myTester", "xyz123")
```

[Manage Users and Roles](https://docs.mongodb.com/v3.4/tutorial/manage-users-and-roles/)
```js
> use admin
> db.createRole(
   {
     role: "manageOpRole",
     privileges: [
       { resource: { cluster: true }, actions: [ "killop", "inprog" ] },
       { resource: { db: "", collection: "" }, actions: [ "killCursors" ] }
     ],
     roles: []
   }
)
{
        "role" : "manageOpRole",
        "privileges" : [
                {
                        "resource" : {
                                "cluster" : true
                        },
                        "actions" : [
                                "killop",
                                "inprog"
                        ]
                },
                {
                        "resource" : {
                                "db" : "",
                                "collection" : ""
                        },
                        "actions" : [
                                "killCursors"
                        ]
                }
        ],
        "roles" : [ ]
}
```


# 以前弄的

```js
// 建立 帳號為 root 的使用者, 設定密碼, 對 admin 擁有 root (系統預設)的權限
use admin;
db.createUser({ user: "root", pwd: "root_pd", roles: [{ role: "root", db: "admin" }] });

// 建立 帳號為 root 的使用者, 設定密碼, 對 db2 擁有 dbOwner (系統預設)的權限
use db2;
db.createUser({ user: "admin", pwd: "admin_pwd", roles: [{ role: "dbOwner", db: "db2" }] });
```

一旦建立完權限機制之後, 往後使用 mongoDB, 都得打帳號密碼了 QQ
```sh
# mongo <host>:<port>/<db> -u<id> -p<pd>
$ mongo 192.168.124.81:27017/admin -u root -p
# (下一行打密碼)
```

然後, 想為已建立過的使用者, 建立其他的權限
```sh
$ mongo -u root -p --authenticationDatabase admin

$ db.createUser({user: 'admin', pwd: 'admin_pwd', roles: [{ role: 'dbOwner', db: 'db2'}]})
```
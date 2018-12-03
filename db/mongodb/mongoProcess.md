# MongoDB Process

如果不打算使用 Daemon 啟用 MongoDB, 也可以使用 前景執行的方式, 來使用 MongoDB

1. 建立 Mongo Daemon (不使用服務)
```sh
# 先建立空目錄 /tmp/qq
mongod --dbpath /tmp/qq --bind_ip 0.0.0.0 --port 27017 
# 預設只有 localhost 能存取
# 最起碼要指定 --dbpath, 否則會依照組態來建立
```

2. 進入 mongodb
```sh
mongo
```

3. 幫 DB 搞權限
```js
> use admin
> db.createUser({
    user: 'tony',
    pwd: 'password123',
    roles: [
        { role: 'userAdminAnyDatabase', db: 'admin' }
    ]
});
// 底下是回傳值... (不是指令)
Successfully added user: {
    "user" : "tony",
    "roles" : [
        {
            "role" : "userAdminAnyDatabase",
            "db" : "admin"
        }
    ]
}
// 離開 mongodb,「/tmp/qq/」 裏頭, 會多出一大堆莫名其妙的東西
```

4. 使用 tony 登入
```sh
### 登入方式 1
mongo -u tony -p --authenticationDatabase admin
# 輸入密碼, 即可進入 admin DB
```

```sh
### 登入方式 2
$ mongo

# 先進入 MongoDB, 再進行權限驗證
> use admin;

> db.auth({user:'tony', pwd:'password123'});
1       # 權限驗證成功
```

5. 建立其他的 user
```js
> use test;
> db.createUser(
  {
    user: "tony2",
    pwd: "password456",
    roles: [ { role: "readWrite", db: "test" },
             { role: "read", db: "reporting" } ]
  }
);
// return 
Successfully added user: {
    "user" : "tony2",
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

6. 使用 tony2 登入
```sh
### 登入方式 1
$ mongo -u tony2 -p  --authenticationDatabase test

### 登入方式 2
$ mongo

> user test

> db.auth("tony2", "password456");
1
```

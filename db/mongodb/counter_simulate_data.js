/* 說明
    作者: 
        Tony

    建立日期: 
        2018/05/04

    相依性:
        npm install mongodb

    如何使用: 
        使用 node(v8.11.1) 執行本程式 

    程式幹嘛用的:
        每 freq 豪秒, 塞1筆模擬的 Counter data到 <dbName> 裡的 <collName>

        資料格式如下:
        {
            "_id": ObjectID(),          MongoDB ID
            "v": <int>,                 亂數產生 - 資料值(累計值) 
            "dt": <datetime>,           資料來源時間(毫秒) ISODate
            "src": <string>             資料來源的 感應器名稱 or 感應器ID
            "type": "co",               Counter以 "co" 表示
        }

    參考:
        https://gist.github.com/dolphin278/5445957
*/

// 參數 ********************************************************

var uid = '';
var upd = '';
var host = "127.0.0.1";
var port = 27017;
var dbName = "test";
var collName = "raw_counter";
var src = 'co1';                    // 資料來源
var freq = 500;                     // 每筆 「freq/1000 」秒

// 程式開始 ******************************************************

var MongoClient = require('mongodb').MongoClient;

if (uid === '' && upd === '') {
    var url = "mongodb://" + host + ":" + port + "/";
} else {
    var url = "mongodb://" + uid + ":" + upd + "@" + host + ":" + port + "/";
}

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db(dbName);
    dbo.collection(collName).deleteMany({'src': src, 'type': 'co'});
    dbo.collection(collName, function(err, collName) {
        var q = 0;              // 累計 counter值
        var i = 0;              // 第幾筆
        var data;

        setInterval(function() {
            q += Math.round(Math.random() * 3);
            data = {
                q: q,
                dt: new Date(),
                src: src,
                type: 'co',
            }

            collName.insert(data, function(err, doc) {
                i++;
                console.log('第 ' + i + ' 筆\n', data);
            });
        }, freq * 1);
    });
});

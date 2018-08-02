/* 說明
    如何使用: 用 node 執行此程式即可.
    
    author: Tony
    date: 2018/05

    相依性:
        mongodb (nodejs模組)

    程式幹嘛用的:
        每 freq 豪秒, 塞1筆模擬資料到 dbName 裡的 collName

    參考:
        https://gist.github.com/dolphin278/5445957
*/

// 參數 ********************************************************

var uid = '';
var upd = '';
var host = "127.0.0.1";
var port = 27017;
var dbName = "test";
var collName = "test";
var freq = 1;               // 每筆 「freq/1000 」秒

// 程式開始 ******************************************************

var MongoClient = require('mongodb').MongoClient;

if (uid === '' && upd === '') {
    var url = "mongodb://" + host + ":" + port + "/" + dbName;
} else {
    var url = "mongodb://" + uid + ":" + upd + "@" + host + ":" + port + "/" + dbName;
}

MongoClient.connect(url, function(err, db) {
    db.collection(collName, function(err, collection) {
        var itemsSent = 0;

        setInterval(function() {
            collection.insert({
                value: Math.round(Math.random() * 100),
                dt: new Date().toLocaleString()
            }, function(err, doc) {
                itemsSent++;
                // console.log('items sent', itemsSent);
            });
        }, freq * 1);
    });
});

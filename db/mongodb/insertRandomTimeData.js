/* 說明
    作者: 
        Tony
    
    建立日期: 
        2018/05/04

    相依性:
        npm install mongodb
        npm install gaussian

    如何使用: 
        使用 node.js 執行本程式 (v8.11.1)
        node insertRandomTimeData.js

    程式幹嘛用的:
        每 freq 豪秒, 塞1筆模擬資料到 dbName 裡的 collName
        模擬觸發事件送資料到資料庫的情況

    參考:
        https://gist.github.com/dolphin278/5445957
*/

// 參數 ********************************************************

var uid = '';
var upd = '';
var host = "127.0.0.1";
var port = 27017;
var dbName = "test";
var collName = "randTime";

// 亂數模擬參數---
var mean = 10;
var variance = 10;

// 程式開始 ******************************************************

var MongoClient = require('mongodb').MongoClient;
var gaussian = require('gaussian');

if (uid === '' && upd === '') {
    var url = "mongodb://" + host + ":" + port + "/" + dbName;
} else {
    var url = "mongodb://" + uid + ":" + upd + "@" + host + ":" + port + "/" + dbName;
}

var dist = gaussian(mean, variance);

function onCollection(err, collection) {
    var itemsSent = 0;
    var time_period;

    function call_me() {
        collection.insert({
            dt: new ISODate(),

        }, function(err, doc) {
            itemsSent++;
            console.log('items sent', itemsSent + '.');
        }); 

        setTimeout(call_me, 1000 * dist.ppf(Math.random())); // 平均 mean秒, 變異數 variance秒, 塞資料
    } 

    call_me();
}

function onConnected(err, db) {
    db.collection(collName, onCollection);
}

MongoClient.connect(url, onConnected);
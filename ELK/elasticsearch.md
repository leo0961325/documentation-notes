# ElasticSearch

可以把 ES 當成 `分散式架構之下的非關聯式資料庫`

- node : server
- index : database
- type : table
- fields : columns
- documents : rows


```sh
### 新增
$# curl -XPOST http://127.0.0.1:9200/logstash-2016.12.23/testPOST -H 'Content-Type: application/json' -d  "{ \"userNme\" : \"weiwei\", \"@timestamp\" : \"2016-12-23T02:50:29.070Z\", \"message\" : \"This is a meaage for testing POST\" }" 
# return
{
    "_index" : "logstash-2016.12.23",
    "_type" : "testPOST",
    "_id" : "6n4nPmgBczqAoTW_OB6w",
    "_version" : 1,"result":"created",
    "_shards" : {
        "total" : 2,
        "successful" : 1,
        "failed" : 0
    },
    "_seq_no" : 0,
    "_primary_term" : 1
}

### 查詢
#                  Host        Port      DB              Table      PK
$# curl -XGET http://127.0.0.1:9200/logstash-2016.12.23/testPOST/6n4nPmgBczqAoTW_OB6w
{
    "_index" : "logstash-2016.12.23",
    "_type" : "testPOST",
    "_id" : "6n4nPmgBczqAoTW_OB6w",
    "_version" : 1,
    "found" : true,
    "_source" : {
        "userNme" : "weiwei",
        "@timestamp" : "2016-12-23T02:50:29.070Z",
        "message" : "This is a meaage for testing POST"
    }
}

### 查詢 特定 type 之下的所有紀錄 (「?pretty」 資料輸出人性化)
$# curl -XGET http://127.0.0.1:9200/logstash-2016.12.23/testPOST/_search?pretty
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   543  100   543    0     0    543      0  0:00:01 --:--:--  0:00:01 33937{
  "took" : 17,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 1,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "logstash-2016.12.23",
        "_type" : "testPOST",
        "_id" : "6n4nPmgBczqAoTW_OB6w",
        "_score" : 1.0,
        "_source" : {
          "userNme" : "weiwei",
          "@timestamp" : "2016-12-23T02:50:29.070Z",
          "message" : "This is a meaage for testing POST"
        }
      }
    ]
  }
}

### POST (有 ?pretty 唷)
$# curl -XPOST http://127.0.0.1:9200/logstash-2016.12.23/testPOST/6n4nPmgBczqAoTW_OB6w/_update?pretty -H 'Content-Type: application/json' -d '{"doc" : { "userName" : "red queen" }}'
{
  "_index" : "logstash-2016.12.23",
  "_type" : "testPOST",
  "_id" : "6n4nPmgBczqAoTW_OB6w",
  "_version" : 2,
  "result" : "noop",
  "_shards" : {
    "total" : 0,
    "successful" : 0,
    "failed" : 0
  }
}

### DELETE
$# curl -XDELETE http://127.0.0.1:9200/logstash-2016.12.23
{"acknowledged":true}

### DELETE (也可用「*」)
$# curl -XDELETE http://127.0.0.1:9200/logstash-2016.12.*
```
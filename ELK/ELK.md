# ELK

- [ELK 30 天系列好文](https://ithelp.ithome.com.tw/users/20103420/ironman/1046)
- start from 2019/01/11

## Elastic Search
- **搜尋** 及 **分析工具**
- `儲存資料, 並作 index`
- `資料格式為 json`
- 最常被用來作 **Log Management**
- Apache Lucene
- 類似產品: Splunk 和 Solr 


## Logstash
- 把來自不同系統的 `data送到 Elastic Search`
- 將前述的 `資料作格式化`

## Kibana
- `資料視覺化`
- 搜尋、分析的 UI


# Elastic start

```sh
$# wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.5.4.tar.gz
$# tar -zxf elasticsearch-6.5.4.tar.gz
$# cd elasticsearch-6.5.4/

# 使用 Daemon 的方式執行 (可能會報錯)
$# ./bin/elasticsearch -d -p pid
OpenJDK 64-Bit Server VM warning: If the number of processors is expected to increase from one, then you should configure the number of parallel GC threads appropriately using -XX:ParallelGCThreads=N
OpenJDK 64-Bit Server VM warning: INFO: os::commit_memory(0x00000000c5330000, 986513408, 0) failed; error='Cannot allocate memory' (errno=12)
#
# There is insufficient memory for the Java Runtime Environment to continue.            # ← ELK 把 JVM 的 heapsize 開太大
# Native memory allocation (mmap) failed to map 986513408 bytes for committing reserved memory.
# An error report file with more information is saved as:
# logs/hs_err_pid7037.log

### 把下面的 memory 改小一點~
$# vim config/jvm.options
-Xms512m        # 原為 -Xms1g
-Xmx512m        # 原為 -Xmx1g

$# ./bin/elasticsearch -d -p pid

$# curl localhost:9200
{
  "name" : "tJVEoN5",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "5-G3_TizS_CWNxYhmk_GRw",
  "version" : {
    "number" : "6.5.4",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "d2ef93d",
    "build_date" : "2018-12-17T21:17:40.758843Z",
    "build_snapshot" : false,
    "lucene_version" : "7.5.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

# Elastic

> Base on RestfulAPI 的 `High scalability` && `High abilability` 的 `real-time` Full-test scan engine.

- base on `Lucene` : 全文檢索的框架 (作者是 Hadoop 的作者)

人家常拿 `elastic` 與 `solr` 比較, 就我現在學到的, solr 可支援 `html`, `pdf`, `word`, `excel`, `csv`, ..., 相對 Elastic 只支援 `json`; 但 Elastic 搜尋效率優於 solr




-------------------------------------

> 語法: `curl -X<Verb> '<Protocol>://<Host>:<Port>/<Path>?<Query_String>' -d '<Body>'`

- Verb - 下列其一, GET, POST, PUT, HEAD, DELETE
- Host:Port - Elastic Search Cluster. Default port 為 *9200*
- Path - API endpoint


```sh
# 想查詢所有 Elastic Search的 cluster number
$ curl -XGET http://localhost:9200/_cat/nodes

# 想搜尋字串的話, 則用 "_search"
```
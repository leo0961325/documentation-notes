# ElasticSearch

- 2019/01/16
- ElasticSearch: v6.5.4
- java: v1.8.0_161

## General Concept

- open source
- real-time
- full-text search
- RESTful
- Cross platform (Java)
- Distributed -> Scalable
- search engine
- big data
- Denormailization (JSON data type)


## ES vs RDB

ElasticSearch | RDBMS
------------- | ---------
Index         | Database
Mapping/Type  | Table
Document      | Row
Field         | Column/Field
Mapping       | Schema
Shard         | Partition/Shard
(all indexed) | Index
Query DSL     | SQL
JSON Object   | Tuple


## Config

```sh
### ES 目錄位置
/etc
    /elasticsearch
        /elasticsearch.keystore	    # 
        /elasticsearch.yml	        # 設定主檔
        /jvm.options	            # JVM 相關設定(含 Memory)
        /log4j2.properties	        # Logging 機制設定
        /role_mapping.yml	        # ES role
        /roles.yml	                # 
        /users	                    # 
        /users_roles	            # 

# Log4j : 
#   
#   
```

### log4j2

方便 Programmer 在 Code 中加入 logging , 並輸出到 目標裝置

- 目標裝置: console, file, streaming, tcp, syslog, ...
- 5 種 Logging Level: DEBUG, INFO, WARN, ERROR, FATAL

具備 3 大元件:
- Logger   : Programmer 在程式中使用來作 logging 的元件
- Appender : 將 Log Message 輸出到各個裝置
- Layout   : Log Message 格式



### 設定主檔 elasticsearch.yml

1. Cluster
    - cluster.name: my-application

2. Node     : Master/Slave 名稱
    - node.name: node-1
    - node.attr.rack: r1

3. Paths    : 資料位置
    - path.data: /var/lib/elasticsearch
    - path.logs: /var/log/elasticsearch

4. Memory   : 資源配置

5. Network  : Bind addresses
    - network.host: 192.168.0.1
    - http.port: 9200

6. Discovery : 新加入的 node, 初始化時要找尋的 hosts
    - 預設為 ["127.0.0.1", "[::1]"]
    - discovery.zen.ping.unicast.hosts: ["host1", "host2"]

7. Gateway   : Cluster 重啟之後, 直到 N 個節點啟動後, 才開始作 recovery
    - gateway.recover_after_nodes: 3

8. Various   : (其他)
    - action.destructive_requires_name: true

```sh
$# curl  http://localhost:9200
{
  "name" : "_SUWv5v",               # node.name
  "cluster_name" : "tonyvm95",      # cluster.name
  "cluster_uuid" : "n9gEE8ucQ1W01HeYox6A2w",
  "version" : {
    "number" : "6.5.4",
    "build_flavor" : "default",
    "build_type" : "rpm",
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

### 健康狀態

* `curl http://localhost:9200/_cat/health?v`
* `curl http://localhost:9200/_cat/indices?v`

健康狀態

- Green - everything is good (cluster is fully functional)
- Yellow - all data is available but some replicas are not yet allocated (cluster is fully functional) 資料還沒作好 HA
- Red - some data is not available for whatever reason (cluster is partially functional)

```sh
# Example
health status index    uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   customer p4An8JtFQ_aPbiMgOOoWJw   5   1          0            0      1.1kb          1.1kb

# pri       5       5 primary shards
# rep       1       1 replica(the defaults)
# docs.cont 0       0 documents
```
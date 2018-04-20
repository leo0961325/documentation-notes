# ELK

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
# [Elasticsearch Developer Tool](https://marketplace.visualstudio.com/items?itemName=crasnam.elasticdeveloper)

- 這東西根本是 ElasticSearch 版的 RestClient
- 2019/01/16
- 1.2.11

# Settings

```js
// 關閉 .esquery 上的 open endpoint documentation
elasticdeveloper.intelliSense.openEndpointDocumentation.enabled
```


# Useful

## XXX.esenv (環境檔)

設定 ES host (JSON data type), 作後續連線及操作

```esenv
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
ping node-ES01 environment | set node-ES01 as target
{
    "host": "http://localhost:9200",
    "name": "dev"
}
```

## XXX.esind ()



## XXX.esquery (ElasticSearch 執行檔)

```esquery
{
    "output": "",
    "params": {
        "query": "data2"
    }
}
```



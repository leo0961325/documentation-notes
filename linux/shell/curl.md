# curl 指令工具

- [curl command](https://gist.github.com/subfuzion/08c5d85437d5d4f00e58)
- 2019/01/16

> 語法: `curl -X<Verb> '<Protocol>://<Host>:<Port>/<Path>?<Query_String>' -d '<Body>'`

- Verb - 下列其一, GET, POST, PUT, HEAD, DELETE
- Path - API endpoint

```sh
### 使用純文字作 POST (下兩者相同)
curl -X POST -d "k1=v1&k2=v2" -H "Content-Type: application/x-www-form-urlencoded" http://localhost:9200/data
curl -X POST -d "k1=v1&k2=v2" http://localhost:9200/data
# POST : 使用純文字作 POST
# -H   : 預設的 Content-Type: application/x-www-form-urlencoded
# -d   : request body 為
#           k1=v1&k2=v2

### 使用檔案作 POST
curl -X POST -d "@data.txt" http://localhost:3000/data

### 使用 JSON 作 POST
curl -d '{"k1": "v1", "k2": "v2"}' -H "Content-Type: application/json" -X http://localhost:8000/data

```
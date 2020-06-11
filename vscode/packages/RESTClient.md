# [VSCode 套件 - REST Client](https://github.com/Huachao/vscode-restclient)
- 2018/07/05
- VSCode版本 1.24.1
- 套件版本 0.19.0


檔案的附檔名只能為下列兩者:
- .http
- .rest

請求方法:
- GET
- POST
- PUT
- DELETE
- PATCH : 依照 request body做修改, 不用在 URL 指定資源點PK
- HEAD
- CONNECT
- OPTIONS
- TRACE


# 強大功能
- `Ctrl+Alt+H` 可看近 50 次的請求
- `Ctrl+Alt+C` 依照 資源點 && 請求方式, 產生程式碼阿 @@!!!
- `Ctrl+Shift+O` 列出所有的資源請求
- `Ctrl+Alt+E` 使用 `Environment Variables`
- `Ctrl+Alt+L` 重 run 上次發的請求 (沒啥鳥用的感覺...)


# 寫法
- 每個資源的請求前, 一定要有 `###` (資源請求之間, 以 `###` 分隔)
- 第一行, `請求方法` + `資源點` + `協定/版本(可不寫)`
- 緊鄰第一行, 為 `request head`
- `request head` 以 `key : value` 的方式還放, 每個 `key : value` 放一行
- `request head` 與 `request body` 之間, 要空一行
- `request body` 可以是 JSON, XML, string, ...
- 文件內, 可以用 `//` 開頭 或者 `#` 開頭, 為整行作註解
- 文件內, **`不可以`** 在某些 `API` 區段的 `同行尾端` 寫註解

## 範例1 - 寫明 Request body (幾乎都這樣用)
```sh
### 取得全部 並指明 協定/版本
GET http://127.0.0.1:8000/api/machines/ HTTP/1.1

### 新增一筆 - Request Body 用 JSON
POST http://127.0.0.1:8000/api/machines/
content-type: application/json

{
    "code" : "emcgo3",
    "machine_name" : "第三台"
}

### 新增一筆 - Request Body 用 XML (要看後端吃不吃 `application/xml` 這格式)
POST http://127.0.0.1:8000/api/machines/ HTTP/1.1
Content-Type: application/xml

<request>
    <code>emcgo3</code>
    <machine_name>第三台</machine_name>
</request>
```


```sh
### 新增一筆 Request Body 使用 key=value 的方式的話, 得 「換行 + &」 隔開 ( & 放開頭 )
POST https://api.example.com/login HTTP/1.1
Content-Type: application/x-www-form-urlencoded

name=foo
&password=bar
```


## 範例2 - 給路徑 (比較少用)
```sh
###
POST http://127.0.0.1:8000/comments HTTP/1.1
Content-Type: application/xml
Authorization: token xxx

< C:\Users\Default\Desktop\demo.xml
# (這行是註解) 指定電腦上的絕對路徑

###
POST http://127.0.0.1:8000/comments HTTP/1.1
Content-Type: application/xml
Authorization: token xxx

< ./demo.xml
# (這行是註解) 指定相對於 專案 baseurl 的相對路徑
```

# 認證方式
- Basic Auth
    - 將 帳號密碼 以 `username:password` 的方式, 作 `base64`
    - 直接寫明 帳號, 密碼
- Digest Auth - 比 "Basic Auth" 安全一些 (文件是這麼說的 但安全在哪我不曉得... )
- SSL Client Certificates - (我讀不懂, pass)
- Azure Active Directory(Azure AD) - (我讀不懂, pass)

```sh
### 將轉換後的 base64 寫在底下...
GET https://httpbin.org/basic-auth/user/passwd HTTP/1.1
Authorization: Basic dXNlcjpwYXNzd2Q=

### 直接寫明 帳號 密碼
GET https://httpbin.org/basic-auth/user/passwd HTTP/1.1
Authorization: Basic user passwd

### 改用 Digest Auth
GET https://httpbin.org/digest-auth/auth/user/passwd
Authorization: Digest user passwd
```

# 變數
- System Variables `{{$variableName}}`
- Custom Variables `{{variableName}}`
    - Environment Variables     - 最後
    - File Variables            - 次優先
    - Request Variables         - 最優先

## Environment Variable 用法

- 在 `VSCode 設定檔` 定義
- `Ctrl+Alt+E` 可以選擇定義好的 `Environment Variable`
- `$shared` 會自動分享給其他沒被定義的的變數 (父類別的概念)

```json
"rest-client.environmentVariables": {
    "$shared": {
        "version": "v1"
    },
    "local": {
        "version": "v2",
        "host": "localhost",
        "token": "test token"
    },
    "production": {
        "host": "example.com",
        "token": "product token"
    }
}
```

不管是選擇哪種環境 (`local` or `production`), 都會有 `version` 這個 key

```sh
###
GET https://{{host}}/api/{{version}comments/1 HTTP/1.1
Authorization: {{token}}
```

## File Variable 用法

- 使用 `@key = value` 一次一行, 可在文件內任何地方定義變數, 不用理會由上而下

```sh
@host = api.example.com
@contentType = application/json
@name = hello

###
GET https://{{host}}/authors/{{name}} HTTP/1.1

###
PATCH https://{{host}}/authors/{{name}} HTTP/1.1
Content-Type: {{contentType}}

{
    "content": "foo bar"
}

```

## Request Variables 用法

- 有點變態的 API 玩法...
- 為 API 命名, 供其他 API 使用 ((接技的概念))
- 命名寫法的位置 : 在 `###` 與 `請求資源端點` 之間, 命名
- 命名的寫法 : `# @name xxx` 或 `// @name xxx`

```sh
@baseUrl = https://example.com/api

### 此API命名為 login
# @name login
POST {{baseUrl}}/api/login HTTP/1.1
Content-Type: application/x-www-form-urlencoded

name=foo&password=bar

### 此API命名為 createComment
# @name createComment
POST {{baseUrl}}/comments HTTP/1.1
Authorization: {{login.response.headers.X-AuthToken}}
Content-Type: application/json

{
    "content": "fake content"
}

// 使用 login 那組 API 的 response.headers.X-AuthToken 來驗證

### 此API命名為 getCreatedComment
# @name getCreatedComment
GET {{baseUrl}}/comments/{{createComment.response.body.$.id}} HTTP/1.1
Authorization: {{login.response.headers.X-AuthToken}}

// 使用 login 那組 API 的 response.headers.X-AuthToken 來驗證
// 搭配 createComment 那組 API 的 response.body 的 id

### 此API命名為 getReplies
# @name getReplies
GET {{baseUrl}}/comments/{{createComment.response.body.$.id}}/replies HTTP/1.1
Accept: application/xml

// 使用 createComment 那組 API 的 response.body 的 id 來作 get

### 此API命名為 getFirstReply
# @name getFirstReply
GET {{baseUrl}}/comments/{{createComment.response.body.$.id}}/replies/{{getReplies.response.body.//reply[1]/@id}}

// 使用 createComment 那組 API 的 response.body 的 id
// 搭配 getReplies 那組 API 的 .response.body 的 //reply[1]/@id  <---我看不懂了...
```

## System Variables

- 使用 `{{$variableName}}` 取得 `系統變數`
- `{{$randomInt 2 5}}` 為 隨機 2~5
- `{{$guid}}` RFC 4122 v4 UUID (不知道幹嘛...)
- `{{$timestamp [offset option]}}` : UTC timestamp, ex: `{{$timestamp -3 h}}` 3小時前
- `"{{$datetime 'YYYY-MM-DD HH:mm:ss'}}"` : 可產生目前時間, ex: "2020-04-23 13:58:32"


Option | Description
------ | --------------
y      | Year
Q      | Quarter
M      | Month
w      | Week
d      | Day
h      | Hour
m      | Minute
s      | Second
ms     | Millisecond


# 關於 時間 變數

- {{$datetime iso8601}} : `2019-12-05T03:17:20.638Z`
- {{$datetime rfc1123}} : `Thu Dec 05 2019 03:17:05 GMT+0000`
- {{$localDatetime iso8601}} : `2019-12-05T11:20:17.617+08:00`


```sh
###
POST https://api.example.com/comments HTTP/1.1
Content-Type: application/xml
Date: {{$datetime rfc1123}}

{
    "request_id": "{{$guid}}",
    "updated_at": "{{$timestamp}}",
    "created_at": "{{$timestamp -1 d}}",
    "review_count": "{{$randomInt 5, 200}}"
}
```



# 額外

```r
@baseURL=http://localhost:8000

### 法一: 查 Token ((application/json))
# @name login
POST {{baseURL}}/api/get_auth_token/
Content-Type: application/json

{
  "username": "tony",
  "password": "password123"
}
# 36ac46118a054c8fff5bfb62c46ce1c2a4ca12f2

### 法二: 查 Token ((application/x-www-form-urlencoded))
POST {{baseURL}}/api/get_auth_token/
Content-Type: application/x-www-form-urlencoded

username=tony&password=password123

### 法三: 接技 - login
# @name goByLogin
GET {{baseURL}}/api/users/1/
Authorization: Token {{login.response.body.token}}
# 類似會把 回傳值丟給 「@name login」, 然後用 「{{login.response.body.token}}」 取出
```

以上三種方法都可收到

```
HTTP/1.0 200 OK
Date: Thu, 23 Aug 2018 02:04:28 GMT
Server: WSGIServer/0.2 CPython/3.6.1
Content-Type: application/json
Allow: POST, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 52
Vary: Cookie

{
  "token": "y6af53p61ce1hf182c48fub2c46b62Qa4ca10g4c"
}
```



# login 取得 token 做後續操作

### - Request Variables 接技用法
```sh
### Login -------------------------
# @name login
POST http://127.0.0.1:5000/api
Content-Type: application/json

{
    "username": "tony",
    "password": "1234"
}
# 取得登入 token
# ---------------------------------
# 取得到的 response 為
{
    "data": {
        "token": "u~eXAiOiJK?V1QiLCYTYw*YzQ0NTgyNDIxNaMUP.lB3YPXwG2S%w"
    }
}
# ---------------------------------
### 作 token 驗證的後續請求
GET http://127.0.0.1:5000/api/demo
Content-Type: application/json
token: {{login.response.body.data.token}}

{
    "data": {
        "token" : "apgfiurwjngarnhgpuh94"
    }
}
# ---------------------------------
# 若 server 直接回傳 response body:
{
    "accessToken" : "apgfiurwjngarnhgpuh94"
}

則直接以 token: {{login.response.body.token}} 即可取得 token
```

### - Request Variables 接技用法(Array)

```sh
# @name demo1
GET {{apiEndPoint}}/api/get_array
Content-Type: application/json
# ---------------------------------
# 取得的 response 為:
HTTP/1.1 200 OK
Connection: close
Content-Length: 64
Content-Type: application/json

{
  "assets": [
    {
      "type": "moto",
      "value": 100
    },
    {
      "type": "bike",
      "value": 10
    }
  ]
}
# ---------------------------------
### 使用 demo1 的 response body 的 moto 來傳遞的話
GET {{apiEndPoint}}/api/get_array
Content-Type: application/json

{
    "data": {{demo1.response.body.assets[1].type}}
}
# ---------------------------------

```


### 上傳附件

```sh
@img1=1.gif
###
# @name fileID
POST {{apiEndPoint}}/api?m=file
token: {{token}}
Content-Type: multipart/form-data; boundary=--upd

--upd
Content-Disposition: form-data; name="file"; filename="{{img1}}"
Content-Type: application/octet-stream

< {{img1}}
--upd--
```
- 後端接口為 `file`
- 僅接收 `file` 參數


### 怎麼取

```sh
### response 長這樣 --------
# @name demo
{
  "code": 0,
  "data": [
    {
      "id": "b98f2ade72d011e997ce00d8610bac98",
      "created_at": "2019-05-10 10:53:58",
      "content": "777 經貿自經區",
      "remark": "777 經貿自經區"
    }
  ]
}

### 取剛剛的 id ---------------
GET {{apiEndPoint}}/api
Content-Type: application/json
token: {{token}}

{
    "id": "{{demo.response.body.data[0].id}}"
}
```

# GraphQL (還不會用)

- 2020/06/09

```bash
POST https://api.github.com/graphql
Content-Type: application/json
Authorization: Bearer v3q905ja9f
X-Request-Type: GraphQL  # GraphQL 查詢, 所送的 Request Header

query ($name: String!, $owner: String!) {
    repository(name: $name, owner: $owner) {
        name
    }
}
```

ServerSentEvent base on `HTTP`

EventSource 有 3 種狀態:

- CONNECTING: 0, 連線中
- OPEN: 1, 以建立連線
- CLOSED: 2, 已關閉連線 or 連線失敗

EventSource 實例 sse

- 屬性:
    - 
- 事件:
    - open
    - message
    - error
    - close
- 方法:

```js
let url = 'http://localhost:23456';
let sse = new EventSource(url);
// 

sse.onopen = function(evt) {
    //
}

sse.onmessage = function(evt) {
    // evt.data
}
```
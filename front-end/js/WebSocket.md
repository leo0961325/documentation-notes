
WebSocket base on `TCP`


WebSocket 實例 ws

- 屬性:
    - readyState:
        - CONNECTING: 0, 連線中
        - OPEN: 1, 連線成功
        - CLOSING: 2, 正在關閉連線
        - CLOSED: 3, 已關閉連線 or 連線失敗
    - bufferedAmount: (遇到再來學)
- 事件:
    - open
    - message
    - error
    - close
- 方法:
    - send()
    - close()


```js
let url = 'ws://localhost:45688';
let ws = new WebSocket(url);
// ws.send()
// ws.readyState
// ws.bufferedAmount
// ws.onerror

ws.onmessage = function(evt) { 
    // evt.code
    // evt.data
    // evt.readyState
}

```


## WebSocket 實作

- [NodeJS-Socket.IO](https://socket.io/get-started/chat/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)

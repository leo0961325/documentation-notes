# socket



## 範例1 - [Python] Simple Socket Server

### [[Python] Simple Socket Server](http://hhtucode.blogspot.tw/2013/03/python-simple-socket-server.html)
- 2018/04/24
- 原著使用 python2 撰寫

> 當client做個一傳一回的動作之後, 就中斷了, 因為 server 端並沒有後續的處理, server 端因為 while loop 的關係, 所以又重新開始回到 accept() 接收狀態, 所以這時候就需要做 thread

> 常見問題補充, 如果在實作的時候, 因為常常中斷又重新啟動server, 而發生 
`socket.error: [Errno 98] Address already in use` 可以參考這篇: https://stackoverflow.com/questions/337115/setting-time-wait-tcp  這是因為, TCP connection建立的時候, 會有一組 *tuple - (source IP, source port, destination IP, destination port)*
這組就算你的server shutdown了!!  *TCP connection都還是會在TIME_WAIT狀態, 因為怕還有其他live packets還沒傳送過來所以要嘛是改TIME_WAIT時間(不安全)*. `解法: 設定之後可以這個TCP connection可以再度重複使用 -> sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
這樣不管你強行中斷了多少次 server, 它都會再次接收原本的 TCP connection


###### server.py
```py
import socket

host = '127.0.0.1'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # ipv4, 連接導向
s.bind((host, port))
s.listen(5)             # 連線數
s.settimeout(3)         # 設定 timeout, 拋出 timeout例外
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 後面的 "socket.SO_REUSEADDR, 1" 為 reuse TCP 、 socket.SOL_SOCKET: 65536 、 socket.SO_REUSEADDR: 4

while True: # 作永久性聆聽
    c, addr = s.accept()
    data = c.recv(1024)     # 最多接收 1024bytes
    c.send(data)
    if data:
        print('Client send ' + repr(data))  # bytes傳輸
        c.send(b"Hello, I'm Server!")
    c.close()
```

###### client.py
```py
import socket

host = '127.0.0.1'
port = 12345
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'&(^$#$R*#HFg*S(_V*F')
    data = s.recv(1024)
    print(repr(data))  # bytes傳輸
```


### 範例2 - 用 socket建立連線, 抓取headers
- [Python 的網路測試應用範例程式](https://www.qa-knowhow.com/?p=1601)
- 2018/04/24
- 原著使用 python2 撰寫
- [解編碼](https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)


###### server.py
```py
import socket
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.com", 80))

http_get = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
data = ''

s.send(http_get)
data = s.recvfrom(1024)

print(data)
```

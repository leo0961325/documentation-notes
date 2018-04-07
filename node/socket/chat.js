var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

// socket.io 監聽連線
io.on('connection', function(socket) {  // 建立 socket(通信介面)
    socket.on('chat message', function(msg) {   // socket 監聽  'chat message'事件
        io.emit('chat message', msg);   // io驅動 'chat message' 事件, 廣撥出 msg
    });
});

http.listen(3000, function() {
    console.log('listening on *:3000');
});
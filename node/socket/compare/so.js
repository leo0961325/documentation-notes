var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', (req, res) => {
	res.sendFile(__dirname + '/so.html');
});

io.on('connection', socket => {
	for (var t = 0; t < 3; t++) {
		// Server端完成 connection後, 開始每秒推送訊息
		setTimeout(() => socket.emit('message', 'message from server'), 1000*t);
	}
});

http.listen(3002, () => console.log('listening on 3002'));

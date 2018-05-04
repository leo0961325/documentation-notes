var app = require('express')();
var ws = require('express-ws')(app);


app.get('/', (req, res) => {
	res.sendFile(__dirname + '/ws.html');
});

app.ws('/', (socket, req) => {
	for (var t = 0; t < 3; t++) {
		// Server端完成 connection後, 開始每秒推送訊息
		setTimeout(() => socket.send('message from server', ()=>{}), 1000*t);
	}
});

app.listen(3001, () => console.log('listening on 3001'));

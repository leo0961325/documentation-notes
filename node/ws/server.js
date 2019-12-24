var ws = require('nodejs-websocket');
var server = ws.createServer(function(conn) {
    var counter = {counter:1, string: ''}

    conn.sendText(JSON.stringify(counter))

    conn.on('text', function(message) {
        var ct = JSON.parse(message)
        ct.counter = parseInt(ct.counter) + 1;
        if (ct.counter < 100) {
            conn.sendText(JSON.stringify(ct));
        }
    });

    conn.on('close', function(code, reason) {
        console.log('Connection closed')
    })
}).listen(8001);
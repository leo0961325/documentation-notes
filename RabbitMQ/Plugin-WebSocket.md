
- [RabbitMQ_Web_STOMP](https://www.rabbitmq.com/web-stomp.html)
- [RabbitMQ_Web_MQTT](https://www.rabbitmq.com/web-mqtt.html)

## MQTT && STOMP Plugin

> **Web MQTT plugin** && **Web STOMP plugin** 分別讓 **MQTT** && **STOMP** 可以在 WebSocket 之上建立連線

而其中, ****RabbitMQ Web STOMP plugin**** 能與 ****RabbitMQ STOMP plugin**** 完全相容

啟用方式:

```bash
$# rabbitmq-plugins enable rabbitmq_web_mqtt
$# rabbitmq-plugins enable rabbitmq_web_stomp
```

- Web STOMP: `http://HOST:15674/ws`
- Web MQTT : `http://HOST:15675/ws`


## Web STOMP 

```html
<script src="stomp.js"></script>
<script>
    let url = 'ws://127.0.0.1:15674/ws';
    let ws = new WebSocket(url);

    let client = Stomp.over(ws);

    let on_conn = () => {
        console.log('Connection success!');
    }

    let on_error = (evt) => {
        console.log('Connection error!!!!');
    }

    client.connect('guest', 'guest', on_conn, on_error, '/');

</script>
```


### Web MQTT

```html
<script src="mqttws31.js"></script>

```
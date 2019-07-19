# RabbitMQ

- 2019/07/05
- [Rabbit MQ 官網](https://www.rabbitmq.com/)
- [AMQP, RabbitMQ and Celery - A Visual Guide For Dummies](https://www.abhishek-tiwari.com/amqp-rabbitmq-and-celery-a-visual-guide-for-dummies/) 簡明扼要
- [Part 3: The RabbitMQ Management Interface](https://www.cloudamqp.com/blog/2015-05-27-part3-rabbitmq-for-beginners_the-management-interface.html) 監控 web GUI
- [Part 4: RabbitMQ Exchanges, routing keys and bindings](https://www.cloudamqp.com/blog/2015-09-03-part4-rabbitmq-for-beginners-exchanges-routing-keys-bindings.html) 圖表流程清晰

# 觀念

RabbitMQ 是個 message-queueing software, 被稱為 *message broker* or *queue manager*

![RabbitMQ](/img/RabbitMQ.png)

Exchange Type 分為下列 4 種:

* Direct: A direct exchange delivers messages to queues based on a message routing key. In a direct exchange, the message is routed to the queues whose `binding key` exactly matches the routing key of the message. **If the queue is bound to the exchange with the `binding key` pdfprocess, a message published to the exchange with a routing key pdfprocess is routed to that queue.**
* Fanout: A fanout exchange routes messages to all of the queues that are bound to it.
* Topic: The topic exchange does a wildcard match between the routing key and the routing pattern specified in the binding.
* Headers: Headers exchanges use the message header attributes for routing.

![Different Exchange](https://www.cloudamqp.com/img/blog/exchanges-topic-fanout-direct.png)
###### Source: https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html

## 名詞解釋

* Producer: 發送 Message/Task 的一方
* Consumer: 處理 Message/Task 的一方
* Queue: 儲存 Message/Task 的地方
* Message: Producer 透過 RabbitMQ 送給 Consumer 的資訊
* Connection: 與 RabbitMQ Server(Broker) 所做的 TCP 連線
* Channel: 處於 Connection 之間的 虛擬 Connection. Producer 發送 Message 與 Consumer 提取 Message 的過程, 都是透過此 Channel 來進行.
* Exchange: 依據 `Exchange Type 準則`, 來分配 **從 Producer 發送的 Message** 應該要給那些 Queue(每個 Queue 都應該 bind 到至少一個 Exchange) (郵局的概念)
* Binding: Queue 與 Exchange 之間的連結
* Routing key: 讓 Exchange 知道它如何配送 Message 到那些 Queue(s) 的關鍵. (郵件地址的概念)
* AMQP(Advanced Message Queuing Protocol): RabbitMQ 用來做 messaging 的協定.
* Vhost, virtual host: A Virtual host provides a way to segregate applications using the same RabbitMQ instance. Different users can have different access privileges to different vhost and queues and exchanges can be created, so they only exist in one vhost.
* Users: 透過 http://<HOST>:15672 連到 RabbitMQ 管理介面時, 所需要登入的使用者帳戶. 一般來說, 特定用戶都有搭配特定權限(Read, Write, Configuration...等)


# 安裝

使用 Docker 來做示範:

```bash
### 來個 RabbitMQ 吧
$# docker run -d \
    -p 5672:5672 \
    -p 15672:15672 \
    -e RABBITMQ_NODENAME=mq1 \
    --name=mq \
    --hostname=tonyhost \
    rabbitmq:management
c7fdf1313520c9b30c68cb826122afe2397a0a1c6c8e22da6e0831ea6f092de4
# 然後就可以開始玩了
```

# 更細節閱讀

- [Production Checklist](https://www.rabbitmq.com/production-checklist.html)
- [Monitoring](https://www.rabbitmq.com/monitoring.html)
- [Consumer Acknowledgements and Publisher Confirms](https://www.rabbitmq.com/confirms.html)
- [AMQP 0-9-1 Model Explained](https://www.rabbitmq.com/tutorials/amqp-concepts.html) 裡面看 headers exchange

## 實作

程式端 與 `RabbitMQ` 溝通, 使用 `AMQP` 傳輸協定, 所以需要支援 AMQP Library

Python 可用下列套件來實作:
- py-amqplib
- txAMQP
- Pika

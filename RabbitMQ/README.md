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

下面兩者非常容易搞混, 且有點重要!

* Binding: A binding is a link between a queue and an exchange.
* Routing key: The routing key is a key that the exchange looks at to decide how to route the message to queues. The routing key is like an address for the message.

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

# Kibana

- [kibana docker](https://github.com/elastic/kibana-docker/tree/6.5)

- 2019/01/24

```sh
/etc/
    /kibana/
        /kibana.yml         # Kibana 設定主檔
/usr/
    /share/
        /kibana/            # ${KIBANA_HOME}
            /bin/               # 
                /kibana             # kibana 執行主檔
            /optimize           # 
            /plugins/           # Kibana 外掛套件位置
/var/
    /lib/
        /kibana             # Kibana 及其外掛套件寫入的資料位置
```


## 初始設定

```sh
### 安裝
$# rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
$# vim /etc/yum.repos.d/kibana.repo
[kibana-6.x]
name=Kibana repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md

$# yum install kibana
$# systemctl daemon-reload
$# systemctl enable kibana.service
$# systemctl start kibana.service
# 2019/01/24 曾因為啟動後, status 發現成功了, 幾秒後隨即跳失敗, 似乎是 RAM 不夠的問題
# RAM 加大後, 就可正常 running 了

### 環境變數 (如果使用 tar.gz 才需要設定; package 安裝時無須設定)
$# echo 'export KIBANA_HOME=/usr/share/kibana'   >> ~/.bashrc
$# echo 'export PATH=${KIBANA_HOME}/bin:${PATH}' >> ~/.bashrc
$# source ~/.bashrc
$# echo ${KIBANA_HOME}

### 設定主檔
$# vim /etc/kibana/kibana.yml	# 設定檔內, 可使用 ${ENV_VAR} 來接收環境變數
elasticsearch.url: "http://localhost:9200"  # elasticsearch 位置
logging.dest: /var/log/kibana/access.log    # 原本沒這個資料夾, 得自己建(還要chown kibana:kibana)
logging.timezone: Asia/Taipei       # logging timezone
server.defaultRoute: /app/kibana    # (default) 將來透過 「http://HOST:PORT/app/kibana」來存取kibana
server.host: localhost      # (default) This setting specifies the host of the back end server.
server.name: your-hostname  # (default) A human-readable display name that identifies this Kibana instance.
server.port: 5601           # (default) Kibana is served by a back end server. This setting specifies the port to use.

```


# Visualize

建立圖表時, 可以為欄位建立進階選項, ex: 將收盤量*100

```json
{"script": "doc['volume'].value * 10"}
```


## 設定檔


```sh
### Kibana 設定主檔
$# vim /etc/kibana/kibana.yml
```
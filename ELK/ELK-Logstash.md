# Logstash

- Since 2019/01

```sh
### 版本
$# /usr/share/logstash/bin/logstash --version
logstash 6.5.4
```


## 目錄

```sh
/etc/logstash/
            /conf.d                 # 設定副檔目錄
            /jvm.options            # 
            /log4j2.properties      # 
            /logstash-sample.conf   # 
            /logstash.yml           # 主要設定檔
            /pipelines.yml          # 
            /startup.options        # 
```




Logstash filter - 強大的字串切割功能 : grok

- [grok debug](https://grokdebug.herokuapp.com/)

```sh
### https://www.elastic.co/guide/en/logstash/6.5/config-examples.html
### Example: logstash.conf
# 此範例目的: 自己把 log 貼到 stdin, 然後來看看是否有把你要的 log pattern 拆解出來 (重點是 filter 那段)
# 然後再用 bin/logstash -f logstash.conf
/usr/share/logstash/bin/logstash -e '
input { stdin { } }
filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  date {
    match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
  }
}
output {
  stdout { codec => rubydebug }
}' --path.settings /etc/logstash
```

現階段的 Log 分析軟體有: splunk, graylog, LOGGLy, logentries, sumologic

```sh
### ↓ 一大堆的 input
### https://www.elastic.co/guide/en/logstash/current/plugins-inputs-stdin.html#plugins-inputs-stdin-codec
input {
    file { # 1
        path => "/path/to/file"
        add_field => { "input_time" => "%{@timestamp}" } # 為 incoming events 增加欄位, value 為 Hash, 此值預設: {}
        codec => "XXX"                  # 將 input 作 decode; ex: "json", 則是將 input json 作 decode. 此值預設: "plain"
        delimiter => "\n"               # 辨識換行
        exclude => ["*.gz", "*.bz2"]    # 不作 input
        start_position => "end"         # beginning -> old data  ; end -> live streaming data
        tags => ["tagName"]             # 此通常與 condition 混搭, ex: filter { if "tagName" in tags[] { ... }}
        type => "event type"            # different type of incoming streams, ex: "syslog", "apache"
        sincedb_path => "/path/to/file" # (不懂)
    }
    stdin { # 2
        add_field => ""     # default: {}
        codec => "line"     # default: line
        tags => [""]        # 
        type => ""          # 
        id => ""            # 若有多個 stdin inputs, 建議給此 unique ID

    }
    # 3. lumberjack : 
    # 4. redis : 
    # ...(超多)
}
filter {
    # csv : 
    # file : 
    # email : 
    # elasticsearch : 
    # ganglia : 
    # jira : 
    # kafka : 
    # lumberjack : 
    # redis : 
    # rabbitmq : 
    # stdout : 
    # mongodb : 
}
output {
    # csv : 
    # date : 
    # drop : 
    # geoip : 
    # grok : 
    # mutate : 
    # sleep : 
}
```

testLog
> [2019-01-11 22:13:88.638] ERROR, ClientIP:192.168.124.101,ServerIP:192.168.124.133,testmessage[測試訊息]#逃避雖然可恥但有用#新垣結衣我女友

grok 基本組成 : `%{屬性:自訂切割後屬性名稱}`.


## 檢查組態

```sh
### 檢查組態
$# /usr/share/logstash/bin/logstash -t logstash.conf

### 列出目前 logstash 可用的 plugins
$# /usr/share/logstash/bin/logstash-plugin list
```


## Running Logstash

```sh
### (Logstash還沒啟動前)
### 測試玩法1: 用 logstash 收集 stdin, 並將之導向 stdout
$# /usr/share/logstash/bin/logstash -e 'input {stdin{}} output {stdout{}}' --path.settings /etc/logstash
Sending Logstash logs to /var/log/logstash which is now configured via log4j2.properties
[2019-01-25T14:16:58,671][WARN ][logstash.config.source.multilocal] Ignoring the 'pipelines.yml' file because modules or command line options are specified
[2019-01-25T14:16:58,684][INFO ][logstash.runner          ] Starting Logstash {"logstash.version"=>"6.5.4"}
[2019-01-25T14:17:00,595][INFO ][logstash.pipeline        ] Starting pipeline {:pipeline_id=>"main", "pipeline.workers"=>2, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>50}
The stdin plugin is now waiting for input:
[2019-01-25T14:17:00,669][INFO ][logstash.pipeline        ] Pipeline started successfully {:pipeline_id=>"main", :thread=>"#<Thread:0x24ba7a43 sleep>"}
[2019-01-25T14:17:00,694][INFO ][logstash.agent           ] Pipelines running {:count=>1, :running_pipelines=>[:main], :non_running_pipelines=>[]}
[2019-01-25T14:17:00,820][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600}
Hello~~~TEST@@      # <- 輸入
{                   # <- 回傳
       "message" => "Hello~~~TEST@@",
    "@timestamp" => 2019-01-25T06:07:15.722Z,
          "host" => "server22",
      "@version" => "1"
}
# Ctrl+C 即可中斷
^C[2019-01-25T14:20:30,150][WARN ][logstash.runner          ] SIGINT received. Shutting down.
[2019-01-25T14:20:30,315][INFO ][logstash.pipeline        ] Pipeline has terminated {:pipeline_id=>"main", :thread=>"#<Thread:0x24ba7a43 run>"}

### 測試玩法2: 用 logstash 收集 stdin, 並將之導向 stdout codec => rubydebug
$# /usr/share/logstash/bin/logstash -e 'input {stdin{}} output {stdout{codec=>rubydebug}}' --path.settings /etc/logstash
Sending Logstash logs to /var/log/logstash which is now configured via log4j2.properties
[2019-01-25T14:33:57,315][WARN ][logstash.config.source.multilocal] Ignoring the 'pipelines.yml' file because modules or command line options are specified
[2019-01-25T14:33:57,328][INFO ][logstash.runner          ] Starting Logstash {"logstash.version"=>"6.5.4"}
[2019-01-25T14:33:59,441][INFO ][logstash.pipeline        ] Starting pipeline {:pipeline_id=>"main", "pipeline.workers"=>2, "pipeline.batch.size"=>125, "pipeline.batch.delay"=>50}
The stdin plugin is now waiting for input:
[2019-01-25T14:33:59,523][INFO ][logstash.pipeline        ] Pipeline started successfully {:pipeline_id=>"main", :thread=>"#<Thread:0x63cb75f7 sleep>"}
[2019-01-25T14:33:59,546][INFO ][logstash.agent           ] Pipelines running {:count=>1, :running_pipelines=>[:main], :non_running_pipelines=>[]}
[2019-01-25T14:33:59,675][INFO ][logstash.agent           ] Successfully started Logstash API endpoint {:port=>9600}
Hello~~~TEST@@      # <- 輸入
{                   # <- 回傳
      "@version" => "1",
    "@timestamp" => 2019-01-25T06:34:07.940Z,
          "host" => "server22",
       "message" => "Hello~~~TEST@@"
}

### 測試玩法3: 收集 httpd 資料, 導向 codec=> rubydebug
$# /usr/share/logstash/bin/logstash -e '
input {
    file {
        type => "apache"
        path => "/var/log/httpd/access_log"
    }
}
output { stdout { } }' --path.settings /etc/logstash

### 測試玩法4: 收集所有 input, 並導向 elasticsearch (ELK platform 最常見的用法)
$# /usr/share/logstash/bin/logstash -e '
input { 
    stdin { } 
} 
output { 
    elasticsearch { 
        hosts => ["http://localhost:9200"]
        index => sample1
    } 
}' --path.settings /etc/logstash

### 測試玩法5: 可使用外部檔案寫好的組態
$# /usr/share/logstash/bin/logstash -f /Path/To/Logstash.conf --path.settings /etc/logstash
```



```sh
# /etc/logstash/conf.d/example_stock_price.conf
input {
  file {
    path => "/root/data/GOOG.csv"
    start_position => "beginning"
    # start_position : beginning, end
    #  beginning : 歷史資料
    #  end       : 後續 Streaming
  }
}

filter {
  csv {
    columns => ["date_of_record","open","high","low","close","adj_close","volume"]
    separator => ","
  }
  date {
    match => ["date_of_record", "yyyy-MM-dd"]
    target => "@timestamp"
  }
  mutate {
    convert => ["open", "float"]
    convert => ["high", "float"]
    convert => ["low", "float"]
    convert => ["close", "float"]
    convert => ["adj_close", "float"]
    convert => ["volume", "float"]
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
  }
}
```


## Grok

- [grok pattern](https://github.com/logstash-plugins/logstash-patterns-core/tree/master/patterns)



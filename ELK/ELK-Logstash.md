# Logstash


## 目錄

```sh
/etc/logstash/
            /conf.d                 # 
            /jvm.options            # 
            /log4j2.properties      # 
            /logstash-sample.conf   # 
            /logstash.yml           # 
            /pipelines.yml          # 
            /startup.options        # 
```



Logstash filter - 強大的字串切割功能 : grok

- [grok debug](https://grokdebug.herokuapp.com/)

現階段的 Log 分析軟體有: splunk, graylog, LOGGLy, logentries, sumologic

```sh
input {

}
filter {
    grok {
        match => {
            "message" => "\[(?<date>.+?)\] %{LOGLEVEL:level},ClientIP:%{IPV4:client_ip},ServerIP:%{IPV4:server_ip},%{GREEDYDATA:message}"
        }
    }
}
output {

}
```

testLog
> [2019-01-11 22:13:88.638] ERROR, ClientIP:192.168.124.101,ServerIP:192.168.124.133,testmessage[測試訊息]#逃避雖然可恥但有用#新垣結衣我女友

grok 基本組成 : `%{屬性:自訂切割後屬性名稱}`.


## 檢查組態

```sh
### 檢查組態
$# /usr/share/logstash/bin/logstash -t logstash.conf
```

# Running Logstash

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
}' --path.settings /etc/logstash # 但是不知道為什麼會出錯@@

### 測試玩法5: 可使用外部檔案寫好的組態
$# /usr/share/logstash/bin/logstash -f /Path/To/Logstash.conf
```



```sh
# /etc/logstash/conf.d/example_stock_price.conf
input {
  file {
    path => "/root/data/GOOG.csv"
    start_position => "beginning"
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
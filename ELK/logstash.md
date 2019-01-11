
Logstash filter - 強大的字串切割功能 : grok

- [grok debug](https://grokdebug.herokuapp.com/)

```sh
filter {
    grok {
        match => {
            "message" => "\[(?<date>.+?)\] %{LOGLEVEL:level},ClientIP:%{IPV4:client_ip},ServerIP:%{IPV4:server_ip},%{GREEDYDATA:message}"
        }
    }
}
```

testLog
> [2019-01-11 22:13:88.638] ERROR, ClientIP:192.168.124.101,ServerIP:192.168.124.133,testmessage[測試訊息]#逃避雖然可恥但有用#新垣結衣我女友

grok 基本組成 : `%{屬性:自訂切割後屬性名稱}`.


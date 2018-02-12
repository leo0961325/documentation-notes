# Hadoop筆記
## 目前還非常雜亂... 改天改

Hive 內, 使用
ADD JAR xxx.jar
來使用使用者字定義的jar user define function

ADD FILE xxx.csv
來分配檔案到各個運算節點



---
$ hadoop fs -put <localPathFile> <hdfsPathFile>

$ hadoop fs -get <hdfsPathFile>

---

```sh
# 使用SparkSQL
# 1.用IdeaProjects包完tar檔,放在/home/tony/IdeaProjects/spark_sql/out/artifacts/spark_sql

# 2.啟動spark
$ /opt/spark/sbin/start-all.sh

# 3.使用spark-submit啟動執行指令
$ spark-submit --master spark://quickstart.cloudera:7077 ~/Desktop/spark_sql_101/data/people.json
```

---

使用貼上多行程式碼模式於互動式模式

```sh
scala> :paste
xxx
xxx
xxx
# Ctrl+d結束, 開始執行貼上的指令
```
---

Spark SQL使用Hive
```sh
$ spark-shell --master spark://quickstart.cloudera:7077 --jars <filePath1.jar>, <filePath2.jar> --files <filePath>
```
將來可使用Hive定義好的腳本(放在jar內)

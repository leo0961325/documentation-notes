# Hadoop eco-system

- 2019/01/25


## 常用指令彙整

```sh

## ${HADOOP_HOME}/sbin/start-all.sh    # (Deprecated) 使用下 2 者代替
$# ${HADOOP_HOME}/sbin/start-dfs.sh    # 啟用 NameNode, DataNode, SecondaryNameNode
$# ${HADOOP_HOME}/sbin/start-yarn.sh   # 啟用 yarn, NodeManager, ResourceManager


## ${HADOOP_HOME}/sbin/start-all.sh    # (Deprecated) 使用下 2 者代替
$# ${HADOOP_HOME}/sbin/stop-yarn.sh    # 關閉 yarn, ResourceManager
$# ${HADOOP_HOME}/sbin/stop-dfs.sh     # 關閉 NameNode, DataNode, SecondaryNameNode

# hbase
$# ${HBASE_HOME}/bin/start-hbase.sh    # 啟用 HMaster
$# ${HBASE_HOME}/bin/stop-hbase.sh     # 關密 hbase

$# jps
```
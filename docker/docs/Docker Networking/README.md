


## Docker Network 語法彙整

```sh
# 建立 Network
$ docker network create <Network Name> # 使用預設的 bridge driver
# 或
$ docker network create -d <Network Driver> <Network Name>  # 指定 driver種類

# 移除 Network
$ docker network rm <Network Name>

# 附加 Network to running Container
$ docker network connect <Network Name> <Container Name>

# 拔掉 Network
$ docker network disconnect <Network Name> <Container ID>

# 列出所有 Network
$ docker network ls

# 查看 Network
$ docker network inspect <Network Name> 
# 或
$ docker inspect <Network Name>

```
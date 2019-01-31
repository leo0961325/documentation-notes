
```sh
### 由 Dockerfile 建立 image, 名為 flaskhello
docker build -t flaskhello .

### 使用 flaskhello(image) 建立 flaskhello(container), port 5000:5000
docker run -d -p 5000:5000 --name flaskhello flaskhello

### start/stop container
docker stop flaskhello
docker start flaskhello

### go into container
docker exec -it flaskhello /bin/bash

### 直接執行
docker run -it --name flaskhello2 hi /bin/bash

# ------------------------------------------

### 直接由 compose 來執行 container
docker-compose down
docker-compose up
```







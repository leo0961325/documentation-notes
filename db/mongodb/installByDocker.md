


```bash
### 2020/02/06
docker pull mongo:4.2

docker run -d -p 27017:27017 -v ~/docker_data/mongo4.2:/db/data --name mongo42 mongo:4.2
```
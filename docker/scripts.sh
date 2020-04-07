
# docker-compose - One Line Command - 查看 compose 內的環境變數
docker-compose run ${COMPOSE_NAME} env

# docker - One Line Command
docker exec ${CONTAINER_NAME} ls /var

# 查看 docker host
docker system info


# 啟動 docker swarm
docker swarm init

# postgresql

```bash
docker pull postgres

docker run -d -p 54321:5432 -v /var/data/postgres:/var/data/postgres -v /var/data/xlog_archive:/var/data/xlog_archive -v /var/data/backup:/var/data/backup -e POSTGRES_PASSWORD=postgres --name=postgresql postgres
```
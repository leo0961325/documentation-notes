# ELK

- 2019/07/03
- [docker-elk](https://github.com/deviantony/docker-elk#host-setup)


```bash
### 載專案
git clone https://github.com/deviantony/docker-elk.git

### 解 SELinux (非 root) (不是很好的方式)
chcon -R system_u:object_r:admin_home_t:s0 docker-elk/

cd docker-elk

docker-compose up   # 要先安裝好 docker compose 「sudo yum install -y docker-compose」
```
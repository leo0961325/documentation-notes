# Docker Machine
- 此篇 for CentOS7
- 2018/01/02

### Prerequest:
- 安裝好 Docker
- 安裝好 Virtual Box

```sh
# 下載並安裝 Docker-Machine
$ curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine && chmod +x /tmp/docker-machine && sudo cp /tmp/docker-machine /usr/local/bin/docker-machine

$ docker-machine version
docker-machine version 0.13.0, build 9ba6da9
```
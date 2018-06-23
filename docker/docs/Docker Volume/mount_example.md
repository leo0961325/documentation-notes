
# mount 範例

## example 1
- 2018/06/21

```dockerfile
FROM scratch
MAINTAINER binghongli@cirrusdi.com
ADD c68-docker.tar.xz /
RUN mkdir /forMount
```

```sh
$ ls
c68-docker.tar.xz  dockerfile  step3_note  wait_for_mount
# c68-docker.tar.xz 解壓縮之後是 Linux 「/」 底下的東西, ex: bin/, etc/, opt/, ...等

$ ls wait_for_mount
test

$ cat wait_for_mount/test
aa

$ docker build -t iiiedu/step3 step3/
# 以 step3/ 裏頭的 dockerfile 建立名為 iiiedu/step3 的 Docker Image

$ docker run -it --name step3_container -v /home/$USER/docker_tutorial/step3/wait_for_mount/:/forMount iiiedu/step3 /bin/bash
# 以 iiiedu/step3 這個 Image
# 建立名為 step3_container 的 Container
# 並以 /bin/bash 執行, -it 進行 REPL
# 並把 「/home/$USER/docker_tutorial/step3/wait_for_mount/」內的檔案映射到 Container內的「/forMount」, 其中一端修改, 另一端可以馬上看到
```

## example 2
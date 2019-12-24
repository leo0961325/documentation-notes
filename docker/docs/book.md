

```bash
$# docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry --name privatedocker registry


$# docker pull ubuntu:14.04

### docker tag IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
$# docker tag ubuntu:14.04 192.168.2.157:5000/demo
$# docker images
REPOSITORY                TAG                 IMAGE ID            CREATED                  SIZE
192.168.2.157:5000/demo   latest              6e4f1fe62ff1        Less than a second ago   197MB
ubuntu                    14.04               6e4f1fe62ff1        Less than a second ago   197MB

$# docker push 192.168.2.157:5000/demo
```
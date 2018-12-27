# 問題...

- 2018/12/03
- v18.03

```powershell
> docker images
error during connect: Get http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.37/images/json: open //./pipe/docker_engine: The system cannot find the file specified. In the default daemon configuration on Windows, the docker client must be run elevated to connect. This error may also indicate that the docker daemon is not running.
# 但是我服務明明有起來阿!!!
```

不知道為什麼, 一直以來都用得好好的, 但是這天電腦就無法使用@@

- [可能的解法](https://github.com/docker/toolbox/issues/636)

```powershell
# 文中提到的解法, 看起來可能可行
> docker-machine env --shell cmd default 
@FOR /f "tokens=*" %i IN ('docker-machine env --shell cmd default') DO @%i
```


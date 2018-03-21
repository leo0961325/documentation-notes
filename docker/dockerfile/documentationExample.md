# Dockerfile範例

[Manage Application data - Images and layers](https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#images-and-layers)
```dockerfile
FROM ubuntu:15.04           # 從 ubuntu:15.04 image 建立虛擬層
COPY . /app                 # 從 dockerfile當時的資料夾, Copy資料到 Container內的 /app/
RUN make /app               # 使用 make來建立 application
CMD python /app/app.py      # Container內執行的指令
```
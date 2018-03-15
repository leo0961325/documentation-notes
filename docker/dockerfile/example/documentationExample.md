# Dockerfile範例

[Manage Application data - Images and layers](https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#images-and-layers)
```dockerfile
FROM ubuntu:15.04           # creating a layer from the ubuntu:15.04 image
COPY . /app                 # adds some files from your Docker client’s current directory
RUN make /app               # builds your application using the make command
CMD python /app/app.py      # what command to run within the container
```
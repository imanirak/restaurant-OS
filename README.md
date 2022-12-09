# Restaurant Order & Inventory Management

### Setup Guide

```
docker build -t restaurant .
```

### confirm docker image was created
```
docker images
```
### should return
```
REPOSITORY                        TAG           IMAGE ID       CREATED          SIZE
restaurant                        latest        dc98e16ac956   2 minutes ago    557MB
restaurant_web                    latest        0ebb59f81e86   7 minutes ago    525MB
```

### view containers
```
docker ps
```

### build local environment with docker compose
```
docker compose up
```

### run a command in a running container
<p>restaurant-web-1 is what the name of the docker container is called
if you come across an error run "docker ps" to find the name of your container. </p>
```
docker exec -it restaurant-web-1 /bin/bash
```
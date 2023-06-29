# usersite
build image
```
make docker-image TARGET=usersite
```

run docker image
```
docker run -d -p 8080:9001 usersite:0.0.1
```
url:
http://127.0.0.1:8080/handlers/

# nginx
build image
```
make docker-image TARGET=nginx-usersite
```

run docker image
```
docker run -d -p 9000:9000 nginx:0.0.1
```
url:
http://127.0.0.1:9000/handlers/

but start two container seperately will not work and we need to create a docker network. In this case we could create a docker-compose file which help to setup network between them
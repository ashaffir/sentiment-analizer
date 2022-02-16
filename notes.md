# Docker Compose Reference
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

# Docker tutorial

> https://www.youtube.com/watch?v=gAkwW2tuIqE&ab_channel=Fireship

## Docker Playground

> https://labs.play-with-docker.com/

## Commands
> https://docs.docker.com/engine/reference/run/

## Docker Docs
> https://docs.docker.com/language/python/

<!-- Build -->

docker build -t ashaffir/stam1:1.0

<!-- Show images -->

docker images

<!-- Run image -->

docker run ashaffir/stam1:1.0

<!-- Run in detouched mode including port forwarding -->

docker run -d -p 5000:8000 ashaffir/stam1:1.0

<!------------ Local : Docker -->

<!-- Running dockers -->

docker ps --all

<!-- Stop/Restart docker -->

docker stop <DOCKER-NAME>
docker restart <DOCKER-NAME>

<!-- Remove Container --> 
docker rm <CONTAINER ID> 

<!-- Remove image --> 
docker image rm <IMAGE ID>

<!-- Tag images -->

docker tag ashaffir/stam1:1.0:latest ashaffir/stam1:1.0:v1.0.0

<!-- Remove tag -->

docker rmi ashaffir/stam1:1.0:v1.0.0

<!-- Push to docker cloud repo -->

docker push ashaffir/stam1:1.0

<!-- Creating Volume (Shared files area) -->

docker volume create shared-stuff

<!-- Checking volumes -->

docker volume ls

<!-- Removing volume -->

docker volume rm shared-stuff

<!-- Start container with a volume -->

docker run -d 8a83e613f075 -v shared-stuff:/stuff

<!-- Removing ALL dockers/containers -->
docker system prune -a

<!-- Docker Compose for more than one process (used with a docker-compose.yml file)-->

docker compose up
docker compose down

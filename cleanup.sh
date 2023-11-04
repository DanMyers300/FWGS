#!/bin/bash

# Stop and remove all running containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Remove all Docker images
docker rmi $(docker images -q)

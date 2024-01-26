#!/bin/bash

# Stop and remove all running containers
sudo docker stop $(docker ps -a -q)
sudo docker rm $(docker ps -a -q)

# Remove all Docker images
sudo docker rmi $(docker images -q)

# Prune system
sudo docker system prune -a
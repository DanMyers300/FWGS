#!/bin/bash

sudo ./docker_cleanup.sh
git fetch && git pull origin main

# Build and run docker containers
sudo docker compose up --build -d

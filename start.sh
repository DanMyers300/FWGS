#!/bin/bash

sudo ./docker_cleanup.sh
git fetch && git pull origin main
sudo docker compose up

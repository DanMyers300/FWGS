#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y curl
sudo apt-get install -y nodejs npm
source ~/.config/envman/PATH.env
curl https://webi.sh/caddy | sh
npm ci
PUBLIC_API_BASE_URL='https://localhost/api' npm run build
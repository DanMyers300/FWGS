#!/bin/bash

apt-get update -y
apt-get upgrade -y
apt-get install -y curl
apt-get install -y nodejs npm
source ~/.config/envman/PATH.env
curl https://webi.sh/caddy | sh
npm ci
PUBLIC_API_BASE_URL='https://localhost/api' npm run build
#!/bin/bash

apt-get update -y
apt-get upgrade -y
apt-get install -y curl
apt-get install -y nodejs
apt-get install -y npm
source ~/.config/envman/PATH.env
curl https://webi.sh/caddy | sh
npm ci
cp -RPp example.env .env
PUBLIC_API_BASE_URL='https://localhost/api' npm run build
caddy run --envfile .env --config ./Caddyfile.localhost
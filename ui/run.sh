#!/bin/bash

apt-get update -y
apt-get upgrade -y
apt-get install -y curl
apt-get install -y nodejs
apt-get install -y npm
source ~/.config/envman/PATH.env
apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
apt update
apt install caddy
npm ci
cp -RPp example.env .env
npm run build
caddy start
caddy run --envfile .env --config ./Caddyfile.localhost
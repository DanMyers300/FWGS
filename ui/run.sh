#!/bin/bash
apt-get update -y
apt-get upgrade -y
apt-get install -y curl
curl https://webi.sh/node@lts | sh
source ~/.config/envman/PATH.env
curl https://webi.sh/caddy | sh
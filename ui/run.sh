#!/bin/bash

apt-get update -y
apt-get upgrade -y
apt-get install -y curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
nvm install --lts
source ~/.config/envman/PATH.env
curl https://webi.sh/caddy | sh
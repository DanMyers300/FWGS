# syntax=docker/dockerfile:1

FROM debian:12-slim
WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y curl
RUN curl https://webi.sh/node@lts | sh
RUN source ~/.config/envman/PATH.env
RUN curl https://webi.sh/caddy | sh

ARG OLLAMA_API_BASE_URL=''
RUN echo $OLLAMA_API_BASE_URL

ENV ENV prod

ENV PUBLIC_API_BASE_URL $OLLAMA_API_BASE_URL
RUN echo $PUBLIC_API_BASE_URL

COPY package.json package-lock.json ./ 
RUN npm ci

COPY . .
RUN PUBLIC_API_BASE_URL='https://localhost/api' npm run build

CMD [ "caddy", "run", "--envfile", ".env", "--config", "./Caddyfile.localhost"]

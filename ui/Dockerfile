# syntax=docker/dockerfile:1

FROM debian:12-slim
WORKDIR /app

ARG OLLAMA_API_BASE_URL=''
RUN echo $OLLAMA_API_BASE_URL

ENV ENV prod

ENV PUBLIC_API_BASE_URL $OLLAMA_API_BASE_URL
RUN echo $PUBLIC_API_BASE_URL

COPY . .
RUN ./run.sh
COPYV package.json package-lock.json ./ 
RUN npm ci
RUN PUBLIC_API_BASE_URL='https://localhost/api' npm run build

CMD [ "caddy", "run", "--envfile", ".env", "--config", "./Caddyfile.localhost"]

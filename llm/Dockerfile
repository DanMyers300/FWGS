FROM nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc

WORKDIR /usr/app

COPY . .

RUN apt-get -y update; apt-get -y install curl
RUN curl -L https://ollama.ai/download/ollama-linux-amd64 -o /usr/bin/ollama
RUN chmod +x /usr/bin/ollama

EXPOSE 11434
ENV OLLAMA_HOST 0.0.0.0
ENTRYPOINT ["/bin/ollama"]
CMD ["serve"]

# Build stage
FROM python:3.12-slim as build

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc

WORKDIR /usr/app

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN /usr/app/venv/bin/pip install -r requirements.txt

COPY . .

# Final stage
FROM python:3.12-slim

WORKDIR /usr/app

COPY --from=build /usr/app .

RUN apt-get -y update; apt-get -y install curl
RUN curl -L https://ollama.ai/download/ollama-linux-amd64 -o /usr/bin/ollama
RUN chmod +x /usr/bin/ollama

ENV PATH="/usr/app/venv/bin:$PATH"

CMD ["python", "app.py"]

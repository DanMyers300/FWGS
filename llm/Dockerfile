# Build stage
FROM python:3.11-slim@sha256:8fcf215ec209b0cba4048197d3a78544faa69561b03a35528899fd9b93fe2990 as build

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc

WORKDIR /usr/app

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY ./requirements.txt .
RUN /usr/app/venv/bin/pip install -r requirements.txt

COPY . .

# Final stage
FROM python:3.11-slim@sha256:8fcf215ec209b0cba4048197d3a78544faa69561b03a35528899fd9b93fe2990

WORKDIR /usr/app

COPY --from=build /usr/app .

ENV PATH="/usr/app/venv/bin:$PATH"

RUN apt-get -y update; apt-get -y install curl

RUN curl -L https://ollama.ai/download/ollama-linux-amd64 -o /usr/bin/ollama
RUN chmod +x /usr/bin/ollama

EXPOSE 11434
ENV OLLAMA_HOST 0.0.0.0
ENTRYPOINT ["/bin/ollama"]
CMD ["serve"]

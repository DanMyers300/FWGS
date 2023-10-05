# Build stage
FROM python:3.11-slim@sha256:8fcf215ec209b0cba4048197d3a78544faa69561b03a35528899fd9b93fe2990 as build

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc

WORKDIR /usr/app

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN /usr/app/venv/bin/pip install -r requirements.txt

COPY . .

# Final stage
FROM python:3.11-slim@sha256:8fcf215ec209b0cba4048197d3a78544faa69561b03a35528899fd9b93fe2990

WORKDIR /usr/app

COPY --from=build /usr/app .

ENV PATH="/usr/app/venv/bin:$PATH"

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

FROM python:3.11-slim as build

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc

WORKDIR /usr/app

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN /usr/app/venv/bin/pip install -r requirements.txt

COPY . /usr/app/

FROM python:3.11-slim

WORKDIR /usr/app/venv

COPY --from=build /usr/app/venv ./venv

WORKDIR /usr/app

EXPOSE 5000

ENV PATH="/usr/app/venv/bin:$PATH"

CMD ["python", "app.py"]

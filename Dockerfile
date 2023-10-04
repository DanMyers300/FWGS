FROM python:3.11-slim
WORKDIR /usr/app
COPY requirements.txt ./
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
COPY . .
CMD ["flask", "--app", "ui", "run"]


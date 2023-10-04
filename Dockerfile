FROM python:3.11-slim
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
COPY . .
CMD ["flask", "--app", "ui", "run"]


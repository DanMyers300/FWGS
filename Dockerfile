FROM debian:latest
COPY . /FWGS
CMD [ "flask", "--app", "ui", "run" ]

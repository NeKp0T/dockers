FROM python:3.5

VOLUME ["/server"]
WORKDIR /server

CMD ["python3", "server.py"]

EXPOSE 8000
FROM python:3.5

VOLUME ["/server"]
ADD server /server
WORKDIR /server
EXPOSE 8000
EXPOSE 8001

CMD ["python3", "./server.py", "8000"]
# CMD ["python", "-m", "http.server", "8000"]
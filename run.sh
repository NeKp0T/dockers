#!/bin/bash

docker build -t task2 .
# docker run -v "$(pwd)/server/contents":/server/contents -p 8000:8000 task2
docker run -v "$(pwd)/server/contents":/server/contents -p 127.0.0.4:8000:8000/tcp -p 127.0.0.4:8001:8001/tcp task2


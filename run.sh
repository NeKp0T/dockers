#!/bin/bash

docker build -t task1 .
docker run -v "$(pwd)/mount":/mnt task1 /exec/script.sh

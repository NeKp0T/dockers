#!/bin/bash

echo started
while [ -x /mnt/hello.sh ] 
do
  /mnt/hello.sh 
  sleep 3
done
echo ended

#!/bin/bash
sudo docker stop md5calculator_chall
sudo docker rm md5calculator_chall
./build.sh
docker run -d \
  --name md5calculator_chall \
  --user 1127:1127 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,size=64m \
  --pids-limit 20 \
  --memory=128m \
  --cpus=1.0 \
  -p 9002:9002 \
  md5calculator

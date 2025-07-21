#!/bin/bash
sudo docker stop kcrc_chall
sudo docker rm kcrc_chall
./build.sh
docker run -d \
  --name kcrc_chall \
  --user 1086:1086 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,size=64m \
  --pids-limit 100 \
  --memory=128m \
  --cpus=1.0 \
  -p 9901:9901 \
  kcrc

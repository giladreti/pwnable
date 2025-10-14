#!/bin/bash
sudo docker stop dos4fun_chall
sudo docker rm dos4fun_chall
./build.sh
docker run -d \
  --name dos4fun_chall \
  --user 1121:1121 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --tmpfs /tmp:rw,size=64m \
  --pids-limit 100 \
  --memory=128m \
  --cpus=1.0 \
  -p 9903:9903 \
  dos4fun

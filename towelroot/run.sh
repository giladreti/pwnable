#!/bin/bash
sudo docker stop towelroot_chall
sudo docker rm towelroot_chall
./build.sh
docker run -d \
  --name towelroot_chall \
  --user 1138:1138 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,size=64m \
  --pids-limit 100 \
  --memory=128m \
  --cpus=1.0 \
  -p 9902:9902 \
  towelroot

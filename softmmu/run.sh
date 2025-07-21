#!/bin/bash
sudo docker stop softmmu_chall
sudo docker rm softmmu_chall
docker run -d \
  --name softmmu_chall \
  --user 1136:1136 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,size=64m \
  --pids-limit 100 \
  --memory=128m \
  --cpus=1.0 \
  -p 9900:9900 \
  softmmu

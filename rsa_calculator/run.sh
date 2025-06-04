#!/bin/bash
sudo docker stop rsa_calculator_chall
sudo docker rm rsa_calculator_chall
./build.sh
docker run -d \
  --name rsa_calculator_chall \
  --user 1128:1128 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,size=64m \
  --pids-limit 20 \
  --memory=128m \
  --cpus=1.0 \
  -p 9012:9012 \
  rsa_calculator

#!/bin/bash
docker build -t sizcaller_user .
docker rm -f sizcaller
docker run --privileged -d --pids-limit=100 -p 9047:9047 --name sizcaller sizcaller_user

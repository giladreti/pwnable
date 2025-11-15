docker build -t chatbot_image .
docker rm -f chatbot
docker run -d -p 9044:9044 --name chatbot --security-opt seccomp=unconfined --privileged chatbot_image

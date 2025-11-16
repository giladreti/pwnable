FROM ubuntu:18.04

ENV USER sizcaller
ENV FLAG flag

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/kr.archive.ubuntu.com/g" /etc/apt/sources.list
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y libc6:i386

#Adduser
RUN useradd -b /home/sizcaller sizcaller
RUN useradd -b /home/sizcaller_pwn sizcaller_pwn

#Copy Binary
ADD loader.sh /loader.sh
ADD $USER /$USER
ADD $USER.c /$USER.c

#Set Flag
ADD flag /home/$USER/$FLAG

#Set Priviledge
RUN chown -R root:sizcaller_pwn /home/$USER
RUN chmod 551 /home
RUN chmod 440 /home/$USER/$FLAG

#COPY start script
ADD ./super.pl /

WORKDIR /home/$USER
CMD ["perl", "/super.pl"]

EXPOSE 9047



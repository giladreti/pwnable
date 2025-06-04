FROM ubuntu:16.04

ENV USER tiny_hard

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/kr.archive.ubuntu.com/g" /etc/apt/sources.list
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y libc6:i386
RUN apt-get install gcc -y
RUN apt-get install -y build-essential
RUN dpkg --add-architecture i386
RUN apt-get install -y gcc-multilib libc6-dev-i386
RUN apt-get install -y gdb

#Adduser
RUN useradd -b /home/tiny_hard tiny_hard
RUN useradd -b /home/tiny_hard_pwn tiny_hard_pwn

#Copy Binary
ADD tiny_hard /tiny_hard
ADD loader.sh /loader.sh
ADD super.pl /super.pl
ADD flag_is_in_here /home/tiny_hard_pwn/flag_is_in_here

#Set Priviledge
RUN mkdir -p /home/tiny_hard
RUN mkdir -p /home/tiny_hard_pwn
RUN chown -R root:tiny_hard /home/tiny_hard
RUN chown -R root:tiny_hard_pwn /home/tiny_hard_pwn
RUN chmod 555 /home
RUN chmod 755 /loader.sh
RUN chmod 755 /super.pl
RUN chmod -R 550 /home/tiny_hard_pwn

WORKDIR /home/$USER
CMD ["perl", "/super.pl"]




FROM ubuntu:16.04

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y gcc-multilib libc6:i386 libssl1.0.0:i386 lib32stdc++6 lib32z1 gdb file net-tools

RUN apt-get install -y perl

RUN useradd -u 1127 -m md5calculator_pwn

COPY md5calculator /home/md5calculator_pwn/md5calculator
COPY super.pl /home/md5calculator_pwn/super.pl
COPY flag /home/md5calculator_pwn/flag

RUN chown root:md5calculator_pwn /home/md5calculator_pwn/md5calculator /home/md5calculator_pwn/flag /home/md5calculator_pwn/super.pl
RUN chmod 550 /home/md5calculator_pwn/md5calculator
RUN chmod 440 /home/md5calculator_pwn/flag
RUN chmod 550 /home/md5calculator_pwn/super.pl

USER md5calculator_pwn
WORKDIR /home
CMD ["perl", "/home/md5calculator_pwn/super.pl"]

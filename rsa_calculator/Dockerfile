FROM ubuntu:16.04

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y gcc-multilib libc6:i386 libssl1.0.0:i386 lib32stdc++6 lib32z1 gdb file net-tools

RUN apt-get install -y perl

RUN useradd -u 1128 -m rsa_calculator_pwn

COPY rsa_calculator /home/rsa_calculator_pwn/rsa_calculator
COPY super.pl /home/rsa_calculator_pwn/super.pl
COPY flag /home/rsa_calculator_pwn/flag

RUN chown root:rsa_calculator_pwn /home/rsa_calculator_pwn/rsa_calculator /home/rsa_calculator_pwn/flag /home/rsa_calculator_pwn/super.pl
RUN chmod 550 /home/rsa_calculator_pwn/rsa_calculator
RUN chmod 440 /home/rsa_calculator_pwn/flag
RUN chmod 550 /home/rsa_calculator_pwn/super.pl

USER rsa_calculator_pwn
WORKDIR /home
CMD ["perl", "/home/rsa_calculator_pwn/super.pl"]

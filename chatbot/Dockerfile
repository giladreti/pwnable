FROM ubuntu:16.04

ENV USER chatbot
ENV FLAG flag_802743cb7dfca891af0ed89056fa3c3d
ENV TERM xterm

RUN apt-get update && apt-get install -y libncurses-dev libseccomp-dev socat gdb

RUN useradd -b /home/$USER $USER

ADD chatbot /home/$USER/$USER
ADD libc-2.23.so /chatbot-libc.so
ADD flag /home/$USER/$FLAG
ADD super.pl /super.pl

RUN chown -R root:$USER /home/$USER
RUN chmod 750 /home/$USER
RUN chmod 750 /home/$USER/$USER
RUN chmod 440 /home/$USER/$FLAG

WORKDIR /home/$USER

CMD ["perl", "/super.pl"]

EXPOSE 9044

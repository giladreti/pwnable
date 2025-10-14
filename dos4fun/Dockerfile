FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y dosemu && \
    apt-get clean

ENV DEBIAN_FRONTEND=noninteractive
ENV HOME=/home/dos4fun

RUN useradd -u 1121 -m dos4fun

COPY dos4fun.exe  /home/dos4fun/
COPY execme       /home/dos4fun/
COPY flag         /home/dos4fun/
COPY keys         /home/dos4fun/
COPY super.pl     /home/dos4fun/

RUN mkdir -p /media/CDROM

RUN chmod 777 /home/dos4fun/execme /home/dos4fun/super.pl && \
    chmod 777 /home/dos4fun/dos4fun.exe /home/dos4fun/flag && \
    chmod 777 /home/dos4fun/keys /media/CDROM

RUN echo '$_layout = "us"' > /home/dos4fun/.dosemurc && \
    echo '$_term_char_set = "latin1"' >> /home/dos4fun/.dosemurc && \
    echo '$_lines = (80)' >> /home/dos4fun/.dosemurc && \
    echo '$_columns = (25)' >> /home/dos4fun/.dosemurc


WORKDIR /home/dos4fun
USER dos4fun
CMD ["perl", "/home/dos4fun/super.pl"]


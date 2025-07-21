FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y qemu-system-i386 && \
    apt-get clean

RUN useradd -u 1086 -m kcrc

COPY bzImage /home/kcrc/bzImage
COPY ld /home/kcrc/ld
COPY super.pl /home/kcrc/super.pl
COPY ramdisk.img /home/kcrc/ramdisk.img

RUN chmod 555 /home/kcrc/ld
RUN chmod 555 /home/kcrc/super.pl
RUN chmod 444 /home/kcrc/bzImage
RUN chmod 444 /home/kcrc/ramdisk.img

USER kcrc
WORKDIR /home/kcrc
CMD ["perl", "/home/kcrc/super.pl"]

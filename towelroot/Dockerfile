FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y qemu-system-arm && \
    apt-get clean

RUN useradd -u 1138 -m towelroot

COPY zImage /home/towelroot/zImage
COPY ld /home/towelroot/ld
COPY super.pl /home/towelroot/super.pl
COPY ramdisk.img /home/towelroot/ramdisk.img

RUN chmod 555 /home/towelroot/ld
RUN chmod 555 /home/towelroot/super.pl
RUN chmod 444 /home/towelroot/zImage
RUN chmod 444 /home/towelroot/ramdisk.img

USER towelroot
WORKDIR /home/towelroot
CMD ["perl", "/home/towelroot/super.pl"]

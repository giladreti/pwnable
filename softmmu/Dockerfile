FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y qemu-system-i386 && \
    apt-get clean

RUN useradd -u 1136 -m softmmu

COPY bzImage /home/softmmu/bzImage
COPY ld /home/softmmu/ld
COPY super.pl /home/softmmu/super.pl
COPY ramdisk.img /home/softmmu/ramdisk.img

RUN chmod 555 /home/softmmu/ld
RUN chmod 555 /home/softmmu/super.pl
RUN chmod 444 /home/softmmu/bzImage
RUN chmod 444 /home/softmmu/ramdisk.img

USER softmmu
WORKDIR /home/softmmu
CMD ["perl", "/home/softmmu/super.pl"]

#!/bin/sh
qemu-system-i386 -kernel bzImage -initrd ramdisk.img -append "root=/dev/ram rw console=ttyS0 rdinit=/bin/ash" -nographic


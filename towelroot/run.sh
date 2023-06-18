#!/bin/sh
qemu-system-arm -M vexpress-a9 -m 110M -kernel zImage -initrd ramdisk.img -append 'root=/dev/ram rw console=ttyAMA0 rdinit=/sbin/init' -nographic -monitor /dev/null
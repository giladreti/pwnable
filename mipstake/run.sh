#!/usr/bin/env sh
qemu-system-mips -M malta -kernel vmlinux-3.2.0-4-4kc-malta \
-hda debian_wheezy_mips_standard.qcow2 -append "root=/dev/sda1 \
console=ttyS0" -device e1000,netdev=net0 -netdev user,id=net0,hostfwd=tcp::5555-:22,hostfwd=tcp::9033-:9033,hostfwd=tcp::1234-:1234 -nographic
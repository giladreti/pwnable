#include <stdio.h>

int main(int argc, char* argv[], char* envp[]){
	system("/usr/bin/qemu-system-i386 -m 64 -kernel /home/softmmu/bzImage -initrd /home/softmmu/ramdisk.img -append 'root=/dev/ram rw console=ttyS0 rdinit=/bin/ash' -nographic -monitor /dev/null");
	return 0;
}


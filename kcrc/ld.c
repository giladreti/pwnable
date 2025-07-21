#include <stdio.h>

int main(int argc, char* argv[], char* envp[]){
	system("qemu-system-i386 -smp 2 -kernel /home/kcrc/bzImage -initrd /home/kcrc/ramdisk.img -append \"root=/dev/ram rw console=ttyS0 rdinit=/bin/ash\" -nographic -monitor /dev/null");
	return 0;
}


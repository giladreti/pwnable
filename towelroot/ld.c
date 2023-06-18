#include <stdio.h>

int main(int argc, char* argv[], char* envp[]){
	char* args[] = {"/usr/bin/qemu-system-arm", "-M", "vexpress-a9", "-m", "110M", "-kernel", "/home/towelroot/zImage", "-initrd", "/home/towelroot/ramdisk.img", "-append", "'root=/dev/ram rw console=ttyAMA0 rdinit=/sbin/init'", "-nographic", "-monitor", "/dev/null", 0};
	execve(args[0], args, envp);
	printf("failed to execve! tell admin!\n");
	return 0;
}


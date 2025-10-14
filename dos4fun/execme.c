#include <stdio.h>
int main(int argc, char* argv[], char* envp[]){
	char* args[] = {"/usr/bin/dosemu", "/home/dos4fun/dos4fun.exe", 0};
	execve(args[0], args, envp);
	printf("failed!\n");
	return 0;
}

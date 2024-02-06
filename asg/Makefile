all:
	gcc -o asg asg.c -lseccomp
	setcap cap_sys_chroot+ep ./asg

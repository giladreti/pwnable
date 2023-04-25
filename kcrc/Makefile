exploit:
	gcc -m32 exploit.c -static -o exploit

exploit2:
	rz-gg -a x86 -b 32 -F -o exploit2 exploit2.c 
	echo echo (cat exploit2 | gzip | base64 -w 0) "|" base64 -d "|" gzip -d | pbcopy
	./clipboard.sh
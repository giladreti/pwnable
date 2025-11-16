#!/bin/sh
secret_dir=`mktemp -d --tmpdir=/tmp`
mount -n -o size=50m -t tmpfs tmpfs $secret_dir
cp /sizcaller `echo $secret_dir`
cp /sizcaller.c `echo $secret_dir`
chown -R sizcaller_pwn:sizcaller_pwn `echo $secret_dir`
chmod 111 /tmp
chmod 777 `echo $secret_dir`
chmod 6755 `echo $secret_dir`/sizcaller
cd `echo $secret_dir`
timeout --preserve-status -k 5s 500s su sizcaller -c /bin/sh


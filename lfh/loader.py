#!/usr/bin/python2
import os, sys, time
import subprocess
from threading import Timer
from pwn import *

TIME = 60

class MyTimer():
    timer=None
    def __init__(self):
        self.timer = Timer(TIME, self.dispatch, args=[])
        self.timer.start()
    def dispatch(self):
        print 'time out. bye!'
        os._exit(0)

def pwn(bookname, mode):
    print 'get your shell'
    p = process(['/home/lfh_pwn/lfh', bookname, mode])
    p.interactive()

def realpath( path ):
    return os.path.realpath(path)

if __name__ == '__main__':
    print 'your book file path please : '
    bookname = realpath(raw_input())
    print bookname
    
    print 'your mode please : '
    mode = raw_input()
    if mode != '1' and mode != '0' :
        print "mode is only 0 or 1"
        os._exit(0)

    print 'thanks! let me parse your book file'
    MyTimer()
    result = pwn( bookname, mode )
    print 'something wrong'
    os._exit(0)


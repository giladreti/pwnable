- `eax` is random `<= 0x300` and not ptrace, execve, open, fork, vfork
- `randpage` is RWX at `0x10000`, random data
- `ebx` `ecx` `edx` `esi` `edi` are random
    - if `mod 2 == 0`, point to random even pointer in `randpage`
    - else unchanged

- we have a weak shell on target! we can customize run env!
-we can `ulimit -S -n 0x11000` and `dup2` a files to `0x10000-0x11000` so that there is 50% that it will be any reg!
    - maybe `fchmod` to SUID? there seem to be no checks at all for the validity of `mode`!
        - but we need a file with custom content and owned by `sizcaller_pwn`... maybe make him create it? and hope for perms... (or umask?)
    - we can `read` into the random area, but what after? the program will exit...
    - `uselib`? probably the first arg will be a long unpredictable string...
    - `ptrace` from tinyhard is filtered...


- what about making heap close to `input`? maybe with large stack?
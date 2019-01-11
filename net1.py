from pwn import *
io = remote('192.168.56.101',2998)
data = io.recvn(4)
value = unpack(data)
io.send(str(value))
log.info(io.recvall())


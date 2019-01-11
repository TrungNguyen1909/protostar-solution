from pwn import *
import struct
io = remote('192.168.56.101',2997)
value = io.unpack()
value += io.unpack()
value += io.unpack()
value += io.unpack()
io.send(pack((value & 0xffffffff)))
log.info(io.recvall())


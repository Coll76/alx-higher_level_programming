#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'Your email is': email})
result = data.encode('utf-8')
req = urllib.request.Request(url, data=result, method='POST')

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print(body)

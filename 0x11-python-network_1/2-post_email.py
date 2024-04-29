#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 2:
    print("Invalid arguments")
    exit(98)
url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'Your email is': email})
result = data.encode('utf-8')
req = urllib.request.Request(url, data=result, method='POST')

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print(body)

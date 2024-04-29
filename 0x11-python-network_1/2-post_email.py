#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""

import sys
import urllib.request
import urllib.parse

email = sys.argv[2]
data = urllib.parse.urlencode({'Your email is': email})
data = data.encode('UTF-8')
post = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(post) as request:
    get = request.read()
    print(get)

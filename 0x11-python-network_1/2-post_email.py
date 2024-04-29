#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.
HTTPError exceptions and print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""

import sys
from urllib.request import HTTPRedirectHandler, build_opener, install_opener
import urllib.parse

"""
takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
"""

def Redirecthandler(HTTPRedirectHandler):
    """
    takes in a URL, sends a request to
    the URL and displays the body of the response (decoded in utf-8)
    """
    if len(sys.argv) != 2:
        print("Invalid arguments")
        exit(98)

    email = sys.argv[2]
    data = urllib.parse.urlencode({'Your email is': email})
    data = data.encode('UTF-8')
    post = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(post) as request:
        get = request.read()
        print(get)

    if __name__ == "__main__":
        Redirecthandler()

#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -i -L --max-redirs 5 "$1" | grep -i -o '^Allow: .*$'| awk '{print $2}'

#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -i -s "$1"

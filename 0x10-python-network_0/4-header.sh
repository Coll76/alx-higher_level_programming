#!/bin/bash
#  Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s -L --max-redirs 5 -H "X-School-User-Id: 98" -X GET "$1"

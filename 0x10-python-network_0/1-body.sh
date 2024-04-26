#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response

# Display only body of a 200 status code response
# You have to use curl

if [ $# != 1 ]; then
	echo "Invalid number of arguments"
	exit 1
fi
url=$1
request=$(curl -s -w "%{http_code}" "$url")
if [ "$request" == "200" ]; then
	$(curl -s "$url")
fi

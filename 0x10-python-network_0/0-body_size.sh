#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# The size must be displayed in bytes
# You have to use curl
# Please test your script in the sandbox provided, using the web server running on port 5000
if [ $# != 1 ]; then
	echo "Invalid arguments"
	exit 98
else
	url=$1
	size=$(curl -s -w "%{size_download}" "$url")
	echo "$size"
fi
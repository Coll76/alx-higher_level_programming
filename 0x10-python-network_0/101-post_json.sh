#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -X POST -d "$1" -H "Content-Type: application/json" "$2"

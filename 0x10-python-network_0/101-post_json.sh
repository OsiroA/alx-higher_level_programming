#!/bin/bash
# This sends a JSON post requeets to a URL and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "$(cat $2)" $1

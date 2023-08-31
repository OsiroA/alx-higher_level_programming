#!/bin/bash
# This script takes in a URL, sends a request to that URL and displays the
# size of the body response
# url = $1 && curl -sS "$url"
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2

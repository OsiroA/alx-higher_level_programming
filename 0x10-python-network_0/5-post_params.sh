#!/bin/bash
# This takes in a URL, sends in a POST request and displays response body
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"

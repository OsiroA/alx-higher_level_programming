#!/bin/bash
# This makes a request to an address that caused the server tk respkmd with a custom
curl -s -X PUT "http://0.0.0.0:5000/catch_me" | grep "You got me!"

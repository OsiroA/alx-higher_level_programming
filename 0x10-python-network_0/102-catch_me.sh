#!/bin/bash
# This makes a request to an address that caused the server tk respkmd with a custom message
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:You got me!"

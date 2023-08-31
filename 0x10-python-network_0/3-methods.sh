#!/bin/bash
# This script tales in a URL and displays all HTTP methods the sever will take
curl -sI "$1" | grep "Allow:" | cut -f2- -d " "

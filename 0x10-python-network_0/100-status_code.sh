#!/bin/bash
# This script finds t
curl -s -o /dev/null -w %{http_code} $1

#!/bin/bash
# bash script to take url as an arg, send GET request and display body response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
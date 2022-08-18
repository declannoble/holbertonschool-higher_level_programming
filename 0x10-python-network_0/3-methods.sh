#!/bin/bash
# script to take in url as an arg and display http methods
curl -sI "$1"| grep 'Allow:' | awk '{print $2, $3, $4}'

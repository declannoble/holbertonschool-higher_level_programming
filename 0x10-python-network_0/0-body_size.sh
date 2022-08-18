#!/bin/bash                                                                                                                  
# script to take in url, send a request and display body size of response                                                    
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
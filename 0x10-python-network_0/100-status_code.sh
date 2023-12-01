#!/bin/bash
#display responce
curl -s -o /tmp/out.txt -w "%{http_code}" "$1" 

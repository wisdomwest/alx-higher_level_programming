#!/bin/bash
#get size of body
curl -s "$1" | wc -c

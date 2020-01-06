#!/bin/bash
# script to get the size of the header
curl -si -X OPTIONS "$1" | awk -F ": " '/Allow:/{print $2}'

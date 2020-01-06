#!/bin/bash
# script to get the size of the header
curl -w '%{size_download}\n' "$1" -so NULL

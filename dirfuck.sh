#!/bin/bash
#Usage: ./dirfuck http://website.com wordpress_directories.txt
#RobertShala

website=$1
directory=$2
path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

> output.txt

while read line; do

  curl -o /dev/null --silent --head --write-out '[+] %{http_code}' "$website$line"
  wget $website$line -a output.txt
  echo " $website$line"

done < $path/$directory

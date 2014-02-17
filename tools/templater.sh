#!/bin/bash

while read line; do
  $(cat $1 | grep -m 1 -o '%%\(.*\)%%' | grep -o '[^%]*') > part.js
  cat $1 | sed -e 's/$(cat $1 | grep -m 1 -o '%%\(.*\)%%')/$(cat part.js)/' > compiled.js
  rm part.js
done < $1

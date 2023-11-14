#!/bin/bash

shopt -s globstar

for zipfile in dir/**/*.zip; do
    unzip "$zipfile" -d "${zipfile%/*}"
done

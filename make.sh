#!/bin/bash
rm -r site/output/*
rm *.html
rm -r photography
pelican site/content/ -o site/output/ -s site/pelicanconf.py -t site/themes/pure-single/
cp -r site/output/* .


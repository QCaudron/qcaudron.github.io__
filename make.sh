#!/bin/bash
pelican site/content/ -o site/output/ -s site/pelicanconf.py -t site/themes/pure-single/
cp site/output/*.html .


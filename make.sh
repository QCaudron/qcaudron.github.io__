#!/bin/bash
pelican site/content/ -o site/output/ -s site/pelicanconf.py -t site/themes/pure-single/
cp site/output/index.html site/output/research.html site/output/projects.html site/output/publications.html site/output/photography.html .


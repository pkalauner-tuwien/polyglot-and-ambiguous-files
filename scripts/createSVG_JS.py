#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to create a SVG-JS polyglot.
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200314
## Version: 1.0
##################################################

import sys

if len(sys.argv) == 3:
    print("No SVG File given, using default file.")
    svg_path =  "files/default.svg"
    offset = -1
elif len(sys.argv) == 4:
    svg_path = sys.argv[1]
    offset = 0
else:
    sys.exit("Usage: python3 createSVG_JS.py [SVG File] <Javascript File> <Output file>")

try:
    with open(svg_path, 'r') as svg, open(sys.argv[2 + offset], 'r') as js, open(sys.argv[3 + offset], 'w') as out:
        # Check filename extension of out file
        if out.name[out.name.rfind('.'):] != '.svg':
            print("Warning: Filename extension of output file should probably be '.svg'.")
        
        js_content = js.read()
        # Add script tag if not already present in JS file
        if "<script>" not in js_content:
            js_content = "<script>\n" + js_content + "</script>\n"

        out.write(svg.read().replace("</svg>", js_content + "</svg>"))
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

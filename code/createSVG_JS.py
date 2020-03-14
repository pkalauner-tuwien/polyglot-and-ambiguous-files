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
    svg_file =  "<?xml version=\"1.0\" standalone=\"no\"?>\n" + \
                "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n" + \
                "<svg version=\"1.1\" baseProfile=\"full\" xmlns=\"http://www.w3.org/2000/svg\">\n" + \
                "<rect width=\"100\" height=\"100\" style=\"fill:rgb(0,255,0);stroke-width:2;stroke:rgb(0,0,0)\" />\n" + \
                "</svg>\n"
    offset = -1
elif len(sys.argv) == 4:
    try:
        with open(sys.argv[1], 'r') as svg:
            svg_file = svg.read() 
        offset = 0
    except FileNotFoundError:
        sys.exit("Error: SVG File could not be opened.")
else:
    sys.exit("Usage: python3 createSVG_JS.py [SVG File] <Javascript File> <Output file>")

try:
    with open(sys.argv[2 + offset], 'r') as js, open(sys.argv[3 + offset], 'w') as out:
        js_content = js.read()
        # Add script tag if not already present in JS file
        if "<script>" not in js_content:
            js_content = "<script>\n" + js_content + "</script>\n"

        out.write(svg_file.replace("</svg>", js_content + "</svg>"))
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

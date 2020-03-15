#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to create a JS-JAVA Polyglot.
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200315 
## Version: 1.0
##################################################

import sys
import os

if len(sys.argv) != 4:
    sys.exit("Usage: python3 createJS_JAVA.py <Javascript File> <Java File> <Output file>")

try:
    with open(sys.argv[1]) as js, open(sys.argv[2], 'r') as java, open(sys.argv[3], 'w') as out:
        java_name = os.path.basename(java.name)
        out_name = os.path.basename(out.name)
        out_suffix = out_name[out_name.rfind('.'):]
        # Check if filenames match (public class name has to be the same as the filename)
        if java_name[:java_name.rfind('.')] != out_name[:out_name.find('.')]:
            print("Warning: Names of Java- and output file should probably match.")
        # Check filename extension of out file
        if out_suffix != '.html' and out_suffix != '.java':
            print("Warning: Filename extension of output file should probably be '.html' or '.java'.")

        js_content = js.read()
        # Add script tag if not already present in JS file
        if "<script>" not in js_content:
            js_content = "<script>\n" + js_content + "</script>\n"

        out.write("/* <html><body>\n" + js_content + "</body></html><!-- */\n")
        out.write(java.read())
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

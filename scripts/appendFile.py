#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to append one file to
## another and write the result to the specified
## output which results in a simple polyglot file.
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200314
## Version: 1.0
##################################################

import sys

if len(sys.argv) != 4:
    sys.exit("Usage: python3 appendFile.py <File 1> <File 2> <Output file>")

try:
    with open(sys.argv[1], 'rb') as in1, open(sys.argv[2], 'rb') as in2, open(sys.argv[3], 'wb') as out:
        out.write(in1.read())
        out.write(in2.read())
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

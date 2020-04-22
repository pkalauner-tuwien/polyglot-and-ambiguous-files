#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################
## This script allows to fix the offsets of a ZIP
## file. E.g. after appending it to another file.
#####################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200422
## Version: 1.0
#####################################################

import sys
from zip_common import fix_zip_offsets

if len(sys.argv) != 2:
    sys.exit("Usage: python3 fixZIPOffsets.py <ZIP File>")

try:
    fix_zip_offsets(sys.argv[1])    
except FileNotFoundError:
    sys.exit("Error: File could not be opened.")

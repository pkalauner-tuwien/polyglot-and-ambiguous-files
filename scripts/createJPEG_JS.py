#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to create a JPEG-JS Polyglot.
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200426
## Version: 1.0
##################################################

import sys
import binascii
from common import to_hex_bytes

if len(sys.argv) != 4:
    sys.exit("Usage: python3 createJPEG_JS.py <JPEG File> <Javascript File> <Output file>")

try:
    with open(sys.argv[1], 'rb') as jpeg, open(sys.argv[2], 'rb') as js, open(sys.argv[3], 'wb') as out:
        out_suffix = out.name[out.name.rfind('.'):]
        # Check filename extension of out file
        if out_suffix != '.jpeg' and out_suffix != '.jpg' and out_suffix != '.js':
            print("Warning: Filename extension of output file should probably be '.jpeg', '.jpg' or '.js'.")
        
        jpeg_data = jpeg.read()
        js_data = js.read()

        # Write start of image and APP0 marker
        out.write(jpeg_data[:4])
        # Open Javascript comment and length of APP0 Segment (0x2f2a)
        out.write(b"/*")
        # Write Data until APP0 segment (incl.)
        out.write(jpeg_data[6:20])
        # Pad APP0 segment so its length reaches 0x2f2a bytes
        out.write(b"\x00" * (0x2f2a - 16))

        # Comment Header
        out.write(b"\xff\xfe")
        
        # Close Javascript comment and use string
        js_data = b"*/=0;" + js_data
        # Open comment again
        js_data += b"/*"
        # Pad comment length with 0 byte if neccessary
        if len(js_data) <= 0xff:
            out.write(b"\x00")
        
        # Write comment length
        out.write(to_hex_bytes(len(js_data), big_endian=True))
        # Write Javascript-Code
        out.write(js_data)
        # Write JPEG data until end of image (EOI) marker (excl.)
        out.write(jpeg_data[20:-2])
        # Close Javascript comment
        out.write(b"*/")
        # Write EOI marker
        out.write(jpeg_data[-2:])

except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################
## This script allows to create a JPEG-ZIP Polyglot.
#####################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200427
## Version: 1.0
#####################################################

import sys
import binascii
from common import to_hex_bytes
from zip_common import fix_zip_offsets

if len(sys.argv) != 4:
    sys.exit("Usage: python3 createJPEG_ZIP.py <JPEG File> <ZIP File> <Output file>")

try:
    with open(sys.argv[1], 'rb') as jpeg, open(sys.argv[2], 'rb') as zip, open(sys.argv[3], 'wb') as out:
        out_suffix = out.name[out.name.rfind('.'):]
        # Check filename extension of out file
        if out_suffix != '.jpeg' and out_suffix != '.jpg' and out_suffix != '.zip':
            print("Warning: Filename extension of output file should probably be '.jpeg', '.jpg' or '.zip'.")
        
        jpeg_data = jpeg.read()
        zip_data = zip.read()

        # Write JPEG data until image data (excl.)
        out.write(jpeg_data[:20])

        # Comment Header
        out.write(b"\xff\xfe")
        
        # Pad comment length with 0 byte if neccessary
        if len(zip_data) <= 0xff:
            out.write(b"\x00")
        
        # Write comment length
        out.write(to_hex_bytes(len(zip_data), big_endian=True))
        # Write ZIP data
        out.write(zip_data)
        # Write remaining JPEG data
        out.write(jpeg_data[20:])

    # Fix zip offsets
    fix_zip_offsets(sys.argv[3])

except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

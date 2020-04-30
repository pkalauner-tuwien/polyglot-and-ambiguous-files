#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################
## This script allows to create a JPEG-PDF Polyglot.
#####################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200428
## Version: 1.0
#####################################################

import sys
import binascii
from common import to_hex_bytes

if len(sys.argv) != 4:
    sys.exit("Usage: python3 createJPEG_PDF.py <JPEG File> <PDF File> <Output file>")

try:
    with open(sys.argv[1], 'rb') as jpeg, open(sys.argv[2], 'rb') as pdf, open(sys.argv[3], 'wb') as out:
        out_suffix = out.name[out.name.rfind('.'):]
        # Check filename extension of out file
        if out_suffix != '.jpeg' and out_suffix != '.jpg' and out_suffix != '.pdf':
            print("Warning: Filename extension of output file should probably be '.jpeg', '.jpg' or '.pdf'.")
        
        jpeg_data = jpeg.read()
        pdf_lines = pdf.readlines()

        # Write JPEG data until image data (excl.)
        out.write(jpeg_data[:20])

        # PDF header
        pdf_inside_comment = pdf_lines[0]

        # Add object with stream
        pdf_inside_comment += b"999 0 obj\n"
        pdf_inside_comment += b"<<>>\n"
        pdf_inside_comment += b"stream\n"

        # Comment Header
        out.write(b"\xff\xfe")
        
        # Pad comment length with 0 byte if neccessary
        if len(pdf_inside_comment) <= 0xff:
            out.write(b"\x00")
        
        # Write comment length
        out.write(to_hex_bytes(len(pdf_inside_comment), big_endian=True))
        # Write PDF header and 999 object
        out.write(pdf_inside_comment)
        # Write remaining JPEG data
        out.write(jpeg_data[20:])

        # End stream and object
        out.write(b"endstream\n")
        out.write(b"endobj\n")

        # Write complete PDF
        for cur in pdf_lines:
            out.write(cur)

except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################
## This script allows to create a PDF-ZIP Polyglot.
## The ZIP file will be nested inside an additional
## PDF object just before the trailer declaration.
#####################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200422
## Version: 1.0
#####################################################

import sys
import zip_common

if len(sys.argv) != 4:
    sys.exit("Usage: python3 createPDF_HTML.py <PDF File> <ZIP File> <Output file>")

try:
    with open(sys.argv[1], 'rb') as pdf, open(sys.argv[2], 'rb') as zip, open(sys.argv[3], 'wb') as out:
        out_suffix = out.name[out.name.rfind('.'):]
        # Check filename extension of out file
        if out_suffix != '.pdf' and out_suffix != '.zip':
            print("Warning: Filename extension of output file should probably be '.pdf' or '.zip'.")

        pdf_content = pdf.read()

        # Get position of trailer object and write PDF document until this offset
        trailer_pos = pdf_content.index(b"trailer")
        out.write(pdf_content[:trailer_pos])

        # Add object with stream
        out.write(b"999 0 obj\n")
        out.write(b"<<>>\n")
        out.write(b"stream\n")

        # Write ZIP contents
        out.write(zip.read())

        # Close stream and object
        out.write(b"endstream\n")
        out.write(b"endobj\n")

        # Write remaining PDF document
        out.write(pdf_content[trailer_pos:])

    # Fix zip offsets
    zip_common.fix_zip_offsets(sys.argv[3])
        
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

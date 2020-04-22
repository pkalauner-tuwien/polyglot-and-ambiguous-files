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
import binascii


FILE_CD = binascii.unhexlify("504b0102")
FILE_HEADER = binascii.unhexlify("504b0304")
END_OF_CD = binascii.unhexlify("504b0506")

def find_nth_substring(text, pattern, n):
    return text.replace(pattern, b'?' * len(pattern), n-1).find(pattern)

def to_hex_bytes(number):
    number_str = format(number, 'x')
    if len(number_str) % 2 != 0:
        number_str = '0' + number_str
    return binascii.unhexlify(number_str)[::-1]

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
    with open(sys.argv[3], 'r+b') as f:
        content = f.read()

        count = 1
        lfh_pos = find_nth_substring(content, FILE_HEADER, count)
        cd_pos = find_nth_substring(content, FILE_CD, count)

        # Central directory offset
        f.seek(find_nth_substring(content, END_OF_CD, 1) + 16)
        f.write(to_hex_bytes(cd_pos))

        while lfh_pos >= 0 and cd_pos >= 0:
            # Local file header offset
            f.seek(cd_pos + 42)
            f.write(to_hex_bytes(lfh_pos))

            count += 1
            lfh_pos = find_nth_substring(content, FILE_HEADER, count)
            cd_pos = find_nth_substring(content, FILE_CD, count)
        
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

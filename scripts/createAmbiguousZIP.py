#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to create an ambiguous ZIP
## the way G. Coldwind presented it.
## https://gynvael.coldwind.pl/?id=539
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200325
## Version: 1.0
##################################################

import sys
import os
import binascii
import mmap

def find_second_last(text, pattern):
    return text.rfind(pattern, 0, text.rfind(pattern))

def to_hex_bytes(number):
    return binascii.unhexlify(format(number, 'x'))


PLACEHOLDER_ZIP = "files/placeholder.zip"
STRUCTURE_BREAKER = b"--- STRUCTURE BREAKER ---"

FILE_CD = binascii.unhexlify("504b0102")
FILE_HEADER = binascii.unhexlify("504b0304")
END_OF_CD = binascii.unhexlify("504b0506")

if len(sys.argv) != 6:
    print("Usage: python3 createAmbiguousPDF.py <ZIP 1> <ZIP 2> <ZIP 3> <ZIP 4> <Output file>")
    sys.exit("Use '-' to use placeholder zip.")

# TODO dont use zip files as parameters, use single files and zip them afterwards to maintain compatibility

zip1_path = sys.argv[1]
zip2_path = sys.argv[2]
zip3_path = sys.argv[3]
zip4_path = sys.argv[4]
out_path = sys.argv[5]

# Check if - is used, if so set path to placeholder zip
if zip1_path == '-':
    zip1_path = PLACEHOLDER_ZIP

if zip2_path == '-':
    zip2_path = PLACEHOLDER_ZIP

if zip3_path == '-':
    zip3_path = PLACEHOLDER_ZIP

if zip4_path == '-':
    zip4_path = PLACEHOLDER_ZIP

try:
    # Merge zip files
    with open(zip1_path, 'rb') as zip1, open(zip2_path, 'rb') as zip2, open(zip3_path, 'rb') as zip3, open(zip3_path, 'rb') as zip3, open(zip4_path, 'rb') as zip4, open(out_path, 'wb') as out:
        # Check filename extension of out file
        if out.name[out.name.rfind('.'):] != '.zip':
            print("Warning: Filename extension of output file should probably be '.zip'.")

        out.write(zip1.read())
        out.write(STRUCTURE_BREAKER)
        out.write(zip2.read())
        out.write(zip3.read())
        out.write(zip4.read())
    
    file_size = os.path.getsize(out_path)
    # Modify created zip file
    with open(out_path, "r+b") as f: #, mmap.mmap(f.fileno(), 0) as mm:
        content = f.read()
        # Calculate comment size
        comment_size = file_size - content.rfind(FILE_HEADER)
        # Go to comment size field in central directory of zip 3
        f.seek(find_second_last(content, END_OF_CD) + 20)
        f.write(to_hex_bytes(comment_size))
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

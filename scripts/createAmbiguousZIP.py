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
import zipfile
import tempfile
from zip_common import FILE_CD, FILE_HEADER, END_OF_CD, find_nth_substring, find_second_last, to_hex_bytes

PLACEHOLDER_ZIP = os.path.join(sys.path[0], "files/placeholder.zip")
STRUCTURE_BREAKER = b"--- STRUCTURE BREAKER ---"

if len(sys.argv) != 6:
    print("Usage: python3 createAmbiguousPDF.py <File 1> <File 2> <File 3> <File 4> <Output file>")
    sys.exit("Files must not be ZIP files. Use '-' to use placeholder file.")

# Create ZIPs out of specified files
tmpdir = tempfile.gettempdir()
zip_paths = []
for i in range(4):
    if (sys.argv[i+1] == '-'):
        zip_paths.append(PLACEHOLDER_ZIP)
    else:
        zip_paths.append(os.path.join(tmpdir, "zip{}.zip".format(i+1)))
        zf = zipfile.ZipFile(zip_paths[i], "w", zipfile.ZIP_STORED)
        zf.write(sys.argv[i+1], arcname=os.path.basename(sys.argv[i+1]))
        zf.close()

try:
    # Merge zip files
    with open(zip_paths[0], 'rb') as zip1, open(zip_paths[1], 'rb') as zip2, open(zip_paths[2], 'rb') as zip3, open(zip_paths[3], 'rb') as zip4, open(sys.argv[5], 'wb') as out:
        # Check filename extension of out file
        if out.name[out.name.rfind('.'):] != '.zip':
            print("Warning: Filename extension of output file should probably be '.zip'.")

        out.write(zip1.read())
        out.write(STRUCTURE_BREAKER)
        out.write(zip2.read())
        out.write(zip3.read())
        out.write(zip4.read())
    
    # Remove temporarily created ZIP files
    for f in zip_paths:
        if f != PLACEHOLDER_ZIP:
            os.remove(f)

    try:
        # Modify created zip file
        with open(sys.argv[5], "r+b") as f:
            # Read file and remove contents
            old_content = f.read()
            f.seek(0)
            f.truncate()

            # Make ZIP 1 and 2 loose
            # Write contents without central directory and end of central directory from ZIP 1 and 2
            content = old_content[:old_content.index(FILE_CD)]
            content += old_content[old_content.index(STRUCTURE_BREAKER):find_nth_substring(old_content, FILE_CD, 2)]
            content += old_content[find_nth_substring(old_content, FILE_HEADER, 3):]
            f.write(content)

            # Correct offsets of ZIP 3 and 4
            for i in range(2):
                local_header_offset = find_nth_substring(content, FILE_HEADER, i+3)
                start_of_cd_offset = find_nth_substring(content, FILE_CD, i+1)
                # Local file header offset
                f.seek(start_of_cd_offset + 42)
                f.write(to_hex_bytes(local_header_offset))
                # Central directory offset
                f.seek(find_nth_substring(content, END_OF_CD, i+1) + 16)
                f.write(to_hex_bytes(start_of_cd_offset))

            # Nest ZIP 4 into comment of ZIP 3
            # Calculate comment size
            # len(content) = file size
            comment_size = len(content) - content.rindex(FILE_HEADER)
            # Set comment size field in central directory of ZIP 3
            f.seek(find_second_last(content, END_OF_CD) + 20)
            f.write(to_hex_bytes(comment_size))
       
    except ValueError:
        sys.exit("Error: Invalid input files")
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

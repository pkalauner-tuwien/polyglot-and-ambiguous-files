#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to create an ambigious PDF.
## It can contain 2 or 3 different images.
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200321
## Version: 1.0
##################################################

import sys
import binascii

if len(sys.argv) == 4:
    offset = -1
elif len(sys.argv) == 5:
    offset = 0
else:
    sys.exit("Usage: python3 createAmbiguousPDF.py <Image 1> <Image 2> [Image 3] <Output file>")

try:
    with open(sys.argv[1], 'rb') as img1, open(sys.argv[2], 'rb') as img2, open(sys.argv[4 + offset], 'w') as out, open("files/three_images_template.pdf") as template:
        # Check filename extension of out file
        if out.name[out.name.rfind('.'):] != '.pdf':
            print("Warning: Filename extension of output file should probably be '.pdf'.")

        img2_content = img2.read()
        if offset == 0:
            with open(sys.argv[3], 'rb') as img3:
                img3_content = img3.read()
        else:
            img3_content = img2_content

        template_content = template.read()
        template_content = template_content.replace("% [IMAGE1]", binascii.hexlify(img1.read()).decode())
        template_content = template_content.replace("% [IMAGE2]", binascii.hexlify(img2_content).decode())
        template_content = template_content.replace("% [IMAGE3]", binascii.hexlify(img3_content).decode())

        out.write(template_content)
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

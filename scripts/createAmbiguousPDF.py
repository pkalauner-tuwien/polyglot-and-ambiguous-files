#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to create an ambiguous PDF.
## It can contain 2 or 3 different images.
## Two different methods of creating ambiguous PDFs
## are used, depending on the amount of images.
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200321
## Version: 1.0
##################################################

import sys
import os
import binascii
from PIL import Image

if len(sys.argv) == 4:
    offset = -1
    template_path = os.path.join(sys.path[0], "files/two_images_template.pdf")
elif len(sys.argv) == 5:
    offset = 0
    template_path = os.path.join(sys.path[0], "files/three_images_template.pdf")
else:
    sys.exit("Usage: python3 createAmbiguousPDF.py <Image 1> <Image 2> [Image 3] <Output file>")

try:
    with open(sys.argv[1], 'rb') as img1, open(sys.argv[2], 'rb') as img2, open(sys.argv[4 + offset], 'w') as out, open(template_path, 'r') as template:
        # Check filename extension of out file
        if out.name[out.name.rfind('.'):] != '.pdf':
            print("Warning: Filename extension of output file should probably be '.pdf'.")


        template_content = template.read()

        template_content = template_content.replace("% [IMAGE1]", binascii.hexlify(img1.read()).decode())
        img1.seek(0)
        width, height = Image.open(img1).size
        template_content = template_content.replace("[IMAGE1_WIDTH]", str(width))
        template_content = template_content.replace("[IMAGE1_HEIGHT]", str(height))

        template_content = template_content.replace("% [IMAGE2]", binascii.hexlify(img2.read()).decode())
        img2.seek(0)
        width, height = Image.open(img2).size
        template_content = template_content.replace("[IMAGE2_WIDTH]", str(width))
        template_content = template_content.replace("[IMAGE2_HEIGHT]", str(height))

        if offset == 0:
            with open(sys.argv[3], 'rb') as img3:
                template_content = template_content.replace("% [IMAGE3]", binascii.hexlify(img3.read()).decode())
                img3.seek(0)
                width, height = Image.open(img3).size
                template_content = template_content.replace("[IMAGE3_WIDTH]", str(width))
                template_content = template_content.replace("[IMAGE3_HEIGHT]", str(height))

        out.write(template_content)
except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

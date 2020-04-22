#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
## This script allows to create an ambiguous GIF.
##################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200419
## Version: 1.0
##################################################

import sys
import binascii
import imageio

if len(sys.argv) != 4:
    sys.exit("Usage: python3 createAmbiguousGIF.py <Image 1> <Image 2> <Output file>")

# Graphic Control Extension Identifier
GCE = binascii.unhexlify("21f9")

try:
    with open(sys.argv[1], 'rb') as img1, open(sys.argv[2], 'rb') as img2, open(sys.argv[3], 'w+b') as out:
        # Check filename extension of out file
        if out.name[out.name.rfind('.'):] != '.gif':
            print("Warning: Filename extension of output file should probably be '.gif'.")

        # Read specified images
        image1 = imageio.imread(img1)
        image2 = imageio.imread(img2)
        images = []
        
        # Append first image 1000 times and finally second image
        for i in range(1000):
            images.append(image1)
        images.append(image2)
        
        # Write all images to one GIF
        imageio.mimwrite(out, images, format='GIF')

        # Remove Graphic Control Extension blocks
        out.seek(0)
        content = out.read()
        out.seek(0)
        out.truncate()

        gce_pos = content.find(GCE)
        while gce_pos >= 0:
            new_content = content[:gce_pos]
            new_content += content[gce_pos+8:]
            content = new_content
            gce_pos = content.find(GCE)
            
        out.write(content)

except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

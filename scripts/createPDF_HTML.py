#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################
## This script allows to create a PDF-HTML Polyglot.
#####################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200418
## Version: 1.0
#####################################################

import sys
import os

if len(sys.argv) != 4:
    sys.exit("Usage: python3 createPDF_HTML.py <PDF File> <HTML File> <Output file>")

try:
    with open(sys.argv[1], 'rb') as pdf, open(sys.argv[2], 'rb') as html, open(sys.argv[3], 'wb') as out:
        out_suffix = out.name[out.name.rfind('.'):]
        # Check filename extension of out file
        if out_suffix != '.pdf' and out_suffix != '.html':
            print("Warning: Filename extension of output file should probably be '.pdf' or '.html'.")

        pdf_lines = pdf.readlines()

        out.write(b"<!--" + pdf_lines[0])
        out.write(b"999 0 obj\n")
        out.write(b"<<>>\n")
        out.write(b"stream\n")
        out.write(b"-->\n")
        out.write(html.read())
        out.write(b"<!--\n")
        out.write(b"endstream\n")
        out.write(b"endobj\n")
        for cur in pdf_lines[1:]:
            out.write(cur)

except FileNotFoundError:
    sys.exit("Error: One or more files could not be opened.")

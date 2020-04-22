#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################
## This file contains some variables and helper
## functions for the easier handling of ZIP files.
#####################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200422
## Version: 1.0
#####################################################

import binascii
from common import find_nth_substring, find_second_last, to_hex_bytes

FILE_CD = binascii.unhexlify("504b0102")
FILE_HEADER = binascii.unhexlify("504b0304")
END_OF_CD = binascii.unhexlify("504b0506")

def fix_zip_offsets(filepath):
    with open(filepath, 'r+b') as f:
        content = f.read()

        count = 1
        lfh_pos = find_nth_substring(content, FILE_HEADER, count)
        cd_pos = find_nth_substring(content, FILE_CD, count)

        # Fix central directory offset
        f.seek(find_nth_substring(content, END_OF_CD, 1) + 16)
        f.write(to_hex_bytes(cd_pos))

        while lfh_pos >= 0 and cd_pos >= 0:
            # Fix local file header offset
            f.seek(cd_pos + 42)
            f.write(to_hex_bytes(lfh_pos))

            count += 1
            lfh_pos = find_nth_substring(content, FILE_HEADER, count)
            cd_pos = find_nth_substring(content, FILE_CD, count)

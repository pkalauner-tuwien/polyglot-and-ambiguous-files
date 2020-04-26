#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#####################################################
## This file contains some helper functions for
## handling files in general.
#####################################################
## Author:  Paul Kalauner
## Email:   paul.kalauner@student.tuwien.ac.at
## Date:    20200422
## Version: 1.0
#####################################################

import binascii

def find_nth_substring(text, pattern, n):
    return text.replace(pattern, b'?' * len(pattern), n-1).find(pattern)

def find_second_last(text, pattern):
    return text.rindex(pattern, 0, text.rindex(pattern))

def to_hex_bytes(number, big_endian = False):
    number_str = format(number, 'x')
    if len(number_str) % 2 != 0:
        number_str = '0' + number_str
    return binascii.unhexlify(number_str)[::1 if big_endian else -1]

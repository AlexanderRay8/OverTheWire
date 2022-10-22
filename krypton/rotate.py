#!/usr/bin/env python3

# This is a tool to rotate characters in python
# It maintains the case of the characters
# It will print all rotations if no amount is specified

import argparse

parser = argparse.ArgumentParser(description=
"""
This is a tool to rotate characters in Python.
It maintains the case of the characters.
It will print all rotations if no amount is specified.
""")

parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('-r', '--rots', metavar='rots', type=int, nargs='*')
args = parser.parse_args()

enc_text = ' '.join(args.file.readlines()).strip()

def rotate_text(enc_text:str, rot_amount:int) -> str:
    rot_text = ''
    for c in enc_text:
        if c.isspace():
            rot_text += ' '
            continue
        casing_diff = ord('a') if c.islower() else ord('A')
        rot_text += chr(((ord(c) + rot_amount - casing_diff) % 26) + casing_diff)
    return rot_text

if args.rots is None: # We default to all
    args.rots = range(27)

for i in args.rots:
    print(rotate_text(enc_text, i))
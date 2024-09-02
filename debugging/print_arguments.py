#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    sys.argv.extend(['1', '2', '3'])

for i in range(len(sys.argv)):
    print(sys.argv[i])

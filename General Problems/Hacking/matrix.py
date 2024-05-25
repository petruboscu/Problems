#!/usr/bin/python3
import sys

if len(sys.argv) == 2:
    print(f"Knock, Knock, {sys.argv[1]}")
else:
    sys.stderr.write(f"Usage, {sys.argv[0]} <name>\n")

#!/usr/bin/env python3
import sys
if len(sys.argv) != 3:
    print("none")
    sys.exit(1)
print(sys.argv[2].split().count(sys.argv[1]))
    
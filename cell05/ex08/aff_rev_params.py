#!/usr/bin/env python3
import sys 
if len(sys.argv) <= 2:
    print("none")
    sys.exit(1)

for i in sys.argv[-1:0:-1]:
    print(i)
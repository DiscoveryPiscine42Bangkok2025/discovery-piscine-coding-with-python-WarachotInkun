#!/usr/bin/env python3
import sys 
if len(sys.argv) ==1:
    print("none")
    sys.exit(1)


for i in sys.argv[1:]:
    if "ism" not in i.lower():
        print(i+"ism")
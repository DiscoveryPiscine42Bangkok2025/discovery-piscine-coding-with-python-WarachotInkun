#!/usr/bin/env python3
import sys
i,j = 0,0
if len(sys.argv) > 1:
    print("none")
    exit()
while i <= 10:
    j = 0
    print(f"Table de {i}: " ,end="")
    while j <= 10:
        print(f"{i * j}", end=" ")
        j += 1
    print()
    i += 1
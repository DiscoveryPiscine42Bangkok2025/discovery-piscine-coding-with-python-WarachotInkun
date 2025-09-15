#!/usr/bin/env python3
f = input("Enter thr first number: \n")
s = input("Enter the second number: \n")
r = int(f) * int(s)
print(f"{f} x {s} = {r}")

if r<0:
    print("The result is negative.")
elif r==0:
    print("The result is zero.")
else:
    print("The result is positive.")
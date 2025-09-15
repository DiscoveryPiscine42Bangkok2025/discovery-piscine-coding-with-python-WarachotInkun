#!/usr/bin/env python3
n = int(input("Enter the number less than 25\n"))
print('\n'.join(f"Inside the loop ,My variable is {i}" for i in range(n, 26))if n <= 25 else "Error") 

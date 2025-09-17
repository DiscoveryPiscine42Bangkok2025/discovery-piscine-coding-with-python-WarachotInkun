#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]

arrN = [i+2 for i in arr ] 
arrNN  = [i for i in arrN if i  >5]


for i in arrNN:
    if arrNN.count(i) > 1:
        arrNN.remove(i)


print(set(arrNN))

#!/usr/bin/env python
'''Counter NO. from 1 to 300'''
for i in range(1,301):
    aStr = str(i)
    if i % 10 == 0:
        print(aStr)
    else:
        print(aStr, end = "\t")

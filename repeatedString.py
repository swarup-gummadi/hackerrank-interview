#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
    '''
    count=0
    for char in s:
        if(char=='a'):
            count=count+1
    l=len(s)
    count=count*(n//l)
    if(n%l!=0):
        for i in s[n%l+1]:
            if(char=='a'):
                count=count+1
    else:
    return count

    '''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

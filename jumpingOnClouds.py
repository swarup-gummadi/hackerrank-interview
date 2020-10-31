#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    i=0
    if len(c)>2:
        while i in range(len(c)-2):
            if(c[i+2]==0):
                i=i+2
                count=count+1
            else:
                i=i+1
                count=count+1
        if(i==(len(c)-2)):
            if(c[i+1]==0):
                count=count+1
    else:
        count=1
        
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

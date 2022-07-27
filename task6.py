import sys

def get_min_max(ints):
    maxNum=-sys.maxsize-1
    minNum=sys.maxsize
    for val in ints:
        if(maxNum<val):
            maxNum = val
        if(minNum > val):
            minNum = val
    return (minNum, maxNum)            

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
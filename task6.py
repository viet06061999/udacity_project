import sys

def get_min_max(ints):
    if ints is None or len(ints) == 0:
        return (-1, -1)
    elif len(ints) == 1:
         return (ints[0], ints[0])    
    maxNum=ints[0]
    minNum=ints[0]
    for val in ints:
        if(maxNum<val):
            maxNum = val
        if(minNum > val):
            minNum = val
    return (minNum, maxNum)            

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((-1, -1) == get_min_max(None)) else "Fail")
print ("Pass" if ((-1, -1) == get_min_max([])) else "Fail")
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")



print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1000000)]  # a list containing 0 - 999999
random.shuffle(l)

print ("Pass" if ((0, 999999) == get_min_max(l)) else "Fail")
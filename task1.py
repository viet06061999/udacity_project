def Square(n, i, j):
    mid = (i + j) // 2
    mul = mid*mid
    mul1 = (mid-1) * (mid-1)
    mul2 = (mid+1)*(mid+1)
    if ((mul == n) or (n < mul2 and n>mul1 and n > mul)):
        return mid;
 
    elif (mul < n):
        return Square(n, mid, j)
    else:
        return Square(n, i, mid)
def sqrt(number):
    if number < 0:
        return -1
    if number == 0:
        return 0
    if number ==1:
        return 1        
    i = 1
    return Square(number, 0, number) 
  
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (3 == sqrt(15)) else "Fail")
print ("Pass" if  (5 == sqrt(26)) else "Fail")
print ("Pass" if  (5 == sqrt(35)) else "Fail")
print ("Pass" if  (9 == sqrt(99)) else "Fail")

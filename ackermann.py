import math

m=3
n=4

def ackermann(m,n):
    if m == 0:
        result = (n+1)
        #print("Returning: %d" % result)
        return result
    elif m > 0 and n == 0:
        result = ackermann(m-1,1)
        #print("Returning: %d" % result)
        return result
    elif m > 0 and n > 0:
        result = ackermann(m-1, ackermann(m,n-1))
        #print("Returning: %d" % result)
        return result
    else:
        print("Not defined for these entries")

print(ackermann(m,n))
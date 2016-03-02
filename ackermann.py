"""
implementation of the ackermann function,
see http://en.wikipedia.org/wiki/Ackermann_function
"""

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

print(ackermann(3,4))
print(ackermann(4,7))
print(ackermann(8,9))

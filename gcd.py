"""
calculate the greatest common divisor
"""

def gcd(a,b):
	""" 
	find the gcd following
	gcd(a,b) = gcd(b,a%b)
	base case  gcd(a,0) = a
	"""
	
	if (b == 0):
		return a
	else:
		return gcd(b,a%b)

print(gcd(13,26))
print(gcd(35,10))
print(gcd(107,34))
print(gcd(100,20))
print(gcd(56,1234))

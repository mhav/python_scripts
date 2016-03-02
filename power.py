import math

a = 2
b = 3

def is_power(a,b):
	if a == 1:
		return True
	if (a%b == 0) and is_power(a/b,b):
		return True
	else:
		return False

print(is_power(a,b))
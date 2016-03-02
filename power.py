"""
checks if a is a power of b
"""
def is_power(a,b):
	if a == 1:
		return True
	if (a%b == 0) and is_power(a/b,b):
		return True
	else:
		return False

print(is_power(2,3))
print(is_power(8,2))
print(is_power(18,3))
print(is_power(10,5))

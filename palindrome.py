
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) <= 1:
		return True
	elif first(word) != last(word):
		return False
	elif first(word) == last(word):
		return is_palindrome(middle(word))

print(is_palindrome("sassas"))
print(is_palindrome("noon"))
print(is_palindrome("Marcus"))
print(is_palindrome("maoam"))
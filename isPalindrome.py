#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

def isPalindrome(x):
	if x <0:
		return False
	else:
		if x == int(str(x)[::-1]):
			return True
		else:
			return False
#Given a 32-bit signed integer, reverse digits of an integer. Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

def reverse(x):
	if x >= 2**31-1 or x <= -2**31:
		return 0
	else:
		if x >= 0:
			result = int(str(x)[::-1])
		else:
			result = (-1) * int(str(x)[1:][::-1])
		
		if result >= 2**31-1 or x <= -2**31:
			return 0
		else:
			return result


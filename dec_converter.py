class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items ==[]

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()


def divideBy2(decNumber):
	"""to convert a decimal number to binary"""
	remstack = Stack()

	while decNumber >0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber // 2

	binString = ""
	while not remstack.isEmpty():
		binString += str(remstack.pop())

	return binString


def divideBy2(decNumber):
	"""use list methods, more complexity"""
	res = ""
	while decNumber >0:
		rem = decNumber %2
		res += str(rem)
		decNumber = decNumber // 2

	res = res[::-1]
	return res


def baseConverter(decNumber, base):
	digits = '0123456789ABCDEFG' #base 2,8,16 so no larger than 16 digits

	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base

	newString = ""
	while not remstack.isEmpty():
		newString = newString + digits[remstack.pop()]

	return newString




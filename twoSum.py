
def twoSum(lst, target): # O(n^2)
	for i in range(lst):
		for j in range(i+1, len(lst)):
			if lst[i] + lst[j] == target:
				return [i, j]

	return []


def twoSum(lst, target): # O(n) using hash table to get index
	seen = {}
	for index, num in enumerate(lst):
		remaining = target - num
		if remaining in seen:
			return [index, seen[remaining]]
		else:
			seen[num] = index

	return []

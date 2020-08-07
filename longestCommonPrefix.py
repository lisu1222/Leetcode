#Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".


def longestCommonPrefix(strs):
	if not strs: return ""
	if len(strs) == 1: return strs[0]

	strs.sort()
	result = ""
	for x,j in zip(strs[0], strs[-1]):
		if x == j: 
			result += x
		else:
			break
			
	return result


'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''
def searchInsert(nums, target):
	for i, v in enumerate(nums):
		if v == target:
			return i
		else:
			nums.append(target)
			nums.sort()
			return nums.index(target)

def searchInsert(nums, target): #better
	nums.append(target)
	nums[:] = sorted(list(set(nums)))
	return nums.index(target)


def searchInseart(nums, target): #binary search
	if nums == []:
		return 0
	lo = 0
	hi = len(nums) - 1
	if target > nums[hi]:
		return hi+1
	while lo < hi:
		mid = (lo + hi)//2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			lo += 1
		else:
			hi += 1

	return lo
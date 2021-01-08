
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    	# Using a helper function
    	return self.helper(nums, 0, len(nums)-1)

    # Finding peak values in array can be done using binary search.
    def helper(self, nums, left, right):
    	if (left == right):
    		return left

    	mid = (left + right)//2

    	if nums[mid] > nums[mid+1]:
    		return self.helper(nums, left, mid)
    	else:
    		return self.helper(nums, mid+1, right)


"""
Out of Box Binary Search 
def binary(self, nums, target, left, right):
	if (left == right):
		return None

	mid = (left + right)//2

	if (nums[mid] == target):
		return nums[mid]

	elif nums[mid] > target:
		return self.binary(nums, target, left, mid)

	else:
		return self.binary(nums, target, mid+1, right)
"""
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that 
they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element 
twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

# time: O(n) space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Using two pointers to traverse the array 
        left = 0
        right = len(numbers) - 1
        
        # move pointers inwards sums from both sides dont match. 
        # only possible for sorted arrays. 
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            else:
                left += 1
            
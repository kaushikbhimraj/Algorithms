"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice 
and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does 
not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # Since all elements are less than the length of the array. 
        # Only the numbers between 1 and N(lenght of array) exists in the array. 
        # When you come across the element simply change the sign of the number to its opposite. 
        # Leftovers are missing numbers. 
        for i in range(len(nums)):
            
            # Treating the value at position as index of the array. 
            index = abs(nums[i]) - 1
            
            # if the value is not already negative, then convert it -ve. 
            if nums[index] > 0:
                nums[index] *= -1
        
        # Declare new array for output. 
        result = []
        
        # Iterate through updated values 
        # Note we are looking the index in this array now not at the value at the index. 
        # Check for only the +vs and append the position + 1 of that value into output array. 
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
                
        return result
            
            
            
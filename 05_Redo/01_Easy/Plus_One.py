"""
Given a non-empty array of digits representing a non-negative integer, increment one to 
the integer.

The digits are stored such that the most significant digit is at the head of the list, and 
each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    
    # Two main cases:
    # Case 1: when last number is 9 -> handle the carry
    # Case 2: otherwise add one and return.
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] == 9:
            # Iterate through entire array to handle carry.     
            i = len(digits) - 1
            carry = 1
            
            while i >= 0:
                digit = digits[i] + carry
                carry = digit // 10
                digits[i] = digit % 10
                i -= 1
            
            # Handling overflow. 
            return [carry] + digits if carry else digits
        
        else:
            digits[-1] += 1
            return digits
                
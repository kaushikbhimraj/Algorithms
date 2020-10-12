"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer. The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit. 

You may assume the integer does not contain any leading zero, except the number 0 itself.

input:  [1,2,3]
output: [1,2,4]
123 + 1 = 124

input:  [4,3,2,1]
output: [4,3,2,2]
4321 + 1 = 4322


TESTCASES:
[1,2,9]
[4,9,9,9]
[0]
[2,3,5,8,7,9,0,2,2,1,4,3,2]
[9]
"""

class prob_66:
	def plusOne(self, digits: List[int]) -> List[int]:
        carry       = 0
        length      = len(digits) - 1
        digits[-1] += 1
        
        while length >= 0:
            unit 		   = digits[length] + carry
            carry          = unit//10
            digits[length] = unit%10
            
            length -= 1
        
        # Overflow handling
        if carry:
            return [carry] + digits
        return digits


# Notes: These kinds of addition problems, you will have to worry about two problems. 
# Carry 
# Carry overflow. 
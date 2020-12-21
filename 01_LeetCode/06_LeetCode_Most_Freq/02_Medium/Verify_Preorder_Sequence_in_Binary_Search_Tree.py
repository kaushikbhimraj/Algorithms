"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence
of a binary search tree.
You may assume each number in the sequence is unique.
Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3

Example 1:
Input: [5,2,6,1,3]
Output: false

Example 2:
Input: [5,2,1,3,6]
Output: true
"""

# Time:  O(n)
# Space: O(n)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # Put values into sack as long as the values are smaller tahn the previous. 
        stack = []
        lastRemoved = 0
        
        # FOR every val in preorder,
        # Rule 1: if lastRemoved > val -> return False
        # Rule 2: as long as stack exists and val > stack[0]
        #           -> pop off the first value 
        #           -> update lastRemoved with latest pop off
        
        # Each iteration add value to stack. 
        for val in preorder:
            if lastRemoved > val:
                return False
            while stack and val > stack[0]:
                lastRemoved = stack.pop(0)
            stack = [val] + stack
        return True
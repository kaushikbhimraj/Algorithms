"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued 
number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]

Time: O(n)
Space: O(n)
where n is # of digits in num. 
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        # Step 1: Create an array with all the digits in the integer. 
        numList = list(map(int, str(num)))
        
        # Step 2: Store the locations of each digit in a dictionary. 
        locations = {x:i for i,x in enumerate(numList)}
        
        # Iterate through each element in array. 
        for i,x in enumerate(numList):
            
            # Each digit in an integer can range from 0 to 9. 
            # So we look if there is a digit from 9 to 0 that exists, 
            # in the integer that can be swapped with the digit in the current location. 
            # If so, we found the max. 
            # Why? Because we are going the reverse order. 
            for d in range(9, x, -1):
                if d in locations and locations[d] > i:
                    # Swap the two digits and return new string 
                    numList[i], numList[locations[d]] = numList[locations[d]], numList[i]
                    return "".join(map(str, numList))
            
        # If there was no mathing found. 
        # In other word the current is optimal. 
        return num
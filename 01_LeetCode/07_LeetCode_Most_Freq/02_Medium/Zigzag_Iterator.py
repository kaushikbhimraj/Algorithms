"""
Given two 1d vectors, implement an iterator to return their elements alternately.
Example:
Input:
v1 = [1,2]
v2 = [3,4,5,6] 

Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of 
elements returned by next should be: [1,3,2,4,5,6].

Follow up:
What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If 
"Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""

# Trick
# 	1. Use a boolean switch to toggle between the arrays. 
# 	2. Based on switch, check if the array is not null and then pop and return the first value. 
# 	3. For hasNext(), check if atleast one array is not null to return true.

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.switch = True

    def next(self) -> int:
        if self.switch:
        	self.switch: = False
        	return self.v1.pop(0) if self.v1 else self.v2.pop(0)
        else:
        	self.switch = True
        	return self.v2.pop(0) if self.v2 else self.v1.pop(0)

    def hasNext(self) -> bool:
    	return True if self.v1 or self.v2 else False
   
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
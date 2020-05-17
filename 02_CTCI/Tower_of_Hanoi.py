import unittest

"""
RECURSION AND DYANMIC PROGRAMMING
Name: Tower of Hanoi
Q No: 8.6
Desc: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of 
      different sizes which can slide onto any tower. The puzzle starts with disks sorted 
      in ascending order of size from top to bottom (i.r, each disk sits on top of an even larger 
      one). You have the following constraints:

		- Only one disk can be moved at a time
		- A disk is slid off the top of the one tower onto another tower. 
		- A disk cannot be placed on top of smaller disk. 

	  Write a program to move the disks from the first tower to the last using Stacks. 

S   T   D

1
2    
3   -   -


2
3   -   1


3   2   1


    1
3   2   -


    1
-   2   3

"""

class TowerofHanoi:
	def __init__(self):
		self.steps = []

	def play(self, stack:int):
		return self.play_helper(stack, "src", "tmp", "des")

	def play_helper(self, stack, src, tmp, dst):
		if stack < 1:
			return
		self.play_helper(stack-1, src, dst, tmp)
		print(src, "->", dst)
		self.play_helper(stack-1, tmp, src, dst)



# Driver Code 
TowerofHanoi().play(3)
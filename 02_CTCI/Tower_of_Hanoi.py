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

"""

class TowersOfHanoi:
	def playGame(self, NumOfDisks, srcTower, dstTower, tmpTower):
		if NumOfDisks < 1:
			return

		# Follows depth first approach here. 
		# This script is constructed on a base case of two disks. 
		# Uses recursion to move the n-1 disks on top of the nth disk 
		# Then moves the nth disk to destination tower
		# Moves n-1 disks back on top of the nth disk 
		self.playGame(NumOfDisks-1, srcTower, tmpTower, dstTower)
		print(srcTower, "->", dstTower)
		self.playGame(NumOfDisks-1, tmpTower, srcTower, dstTower)


# Driver Code 
TowersOfHanoi().playGame(3, 1, 2, 3)
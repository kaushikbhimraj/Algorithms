"""
High school students are voting for their class president and you're tasked with counting the votes. 
Each presidential candidates is represented by a unique integer and the candidate that should win 
the election is the candidate that has received more than half the votes. Given a list of integers,
return the candidate that should become the class president. 

Note: You may assume there is always a candidate that has received more than half the votes. 

Ex: Given the following votes…

votes = [1, 1, 2, 2, 1], return 1.
Ex: Given the following votes…

votes = [1, 3, 2, 3, 1, 2, 3, 3, 3], return 3.
"""
from collections import defaultdict

class Solution:
	def classPresident(self, votes):
		n = len(votes)
		mem = defaultdict(int)
		
		for vote in votes:
			if (vote in mem):
				mem[vote] += 1

		count, candidate = 0, 0
		for key in mem.keys():
			if (mem[key] > (n + 1)//2):
				return key
			if count < mem[key]:
				count = mem[key]
				candidate = key
		return key
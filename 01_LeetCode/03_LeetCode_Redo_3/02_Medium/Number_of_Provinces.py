"""
There are n cities. Some of them are connected, while some are not. If city a is 
connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities 
outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith 
city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		m = len(isConnected)
		visited = [0] * m
		count = 0
		for i in range(m):
			if visited[i] == 0:
				self.dfs(isConnected, visited, i)
				count += 1
		return count

	# Basic DFS. 
	# 
	def dfs(self, isConnected, visited, i):
		for j in range(len(isConnected[0])):
			if (isConnected[i][j] == 1 and visited[j] == 0):
				visited[j] = 1
				self.dfs(isConnected, visited, j)

# ---------------------------------------------------------------------------
	def findCircleNum2(self, isConnected: List[List[int]]) -> int:
		# Use a nested function
		# Create a set to track all the rows that you have visited.
		# because recursion will go through all the values in that row for you. 
		visited = set()
		res = 0

		# Nested function to perform DFS
		# This function will iterate through the entire row each col at a time. 
		def dfs(node):
			for pos, val in enumerate(isConnected[node]):
				if val and pos not in visited:
					visited.add(pos)
					dfs(pos)

		# PROGRAM START. 
		# Iterate through each row. If the row has been visited. 
		for i in range(len(isConnected)):
			if i not in visited:
				dfs(i)
				res += 1
		return res
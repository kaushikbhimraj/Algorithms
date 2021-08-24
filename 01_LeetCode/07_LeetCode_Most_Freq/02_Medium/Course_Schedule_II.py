"""
There are a total of n courses you have to take labelled from o to n - 1

Some courses may have prerequisites, for example, if prerequisites[i] = [a,b] this means
you must take the course b before the course a.

Give the total number of courses numCourses and a list of the prerequisite pairs, return 
the ordering of courses you should take to finish all courses. 

If there are many valid answers, return any of them. If it is impossible to finish
all courses, return an empty array. 

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    	# Create an adjacency list
    	# Create a visited list to check for DAG
    	adj = [[] for _ in range(numCourses)]
    	self.visited = [0] * numCourses
    	self.stack = []

    	for x,y in prerequisites:
    		adj[x].append(y)

    	for i in range(numCourses):
    		if not self.dfs(i, adj):
    			return []
    	return self.stack

    def dfs(self, node, graph):
    	if self.visited[node] == -1:
    		return False

    	if self.visited[node] == 1:
    		return True

    	self.visited[node] = -1
    	for u in graph[node]:
    		if not self.dfs(u, graph):
    			return False

    	self.visited[node] = 1
    	self.stack.append(node)
    	return True
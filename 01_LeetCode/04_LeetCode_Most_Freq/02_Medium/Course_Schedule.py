class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list and list to hold all the visited nodes. 
        adj = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for x,y in prerequisites:
        	adj[x].append(y)

        # Iterate through each course:
        # Check if recursion returns a cycle
        for i in range(numCourses):
        	if not self.dfs():
        		return False
        return True

    def dfs(self, course, visited, adj):

    	# If the course is still being visited and we come back to it, 
    	# we have a cycle here. 
    	if visited[course] == -1:
    		return False

    	if visited[course] == 1:
    	 	return True

    	visited[course] = -1
    	for w in adj[course]:
    		if not self.dfs(w, visited, adj):
    			return False

    	# Since we have completed visited all the dependencies of the course, 
    	# we set it to a 1 since it is fully explored. 
    	visited[course] = 1
    	return True


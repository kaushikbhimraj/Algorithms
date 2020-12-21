"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair 
of nodes), write a function to find the number of connected components in an undirected 
graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Creating a magic function to do the DFS
        def dfs(n, adj, visiT):
            if visit[n]:
                return 
            visit[n] = 1
            for u in adj[n]:
                dfs(u, adj, visit)
        
        # In order to count the number of components in the graph
        # Create an adjacency list. 
        # Keep track of nodes visited.
        visit = [0]*n
        adj = [[] for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        # Evertime we run into a 0 in the visited list we start DFS. 
        count = 0
        for i in range(n):
            if not visit[i]:
                dfs(i, adj, visit)
                count += 1
        return count
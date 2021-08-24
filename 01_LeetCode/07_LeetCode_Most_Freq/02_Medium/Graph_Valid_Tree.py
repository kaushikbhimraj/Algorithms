"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each 
edge is a pair of nodes), write a function to check whether these edges 
make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since 
all edges are undirected, [0,1] is the same as [1,0] and thus will not 
appear together in edges.

"""

# Time:  O(N + E)
# Space: O(N + E)
# Where N = # of nodes and E = # of edges
class Solution:
    # 1. Graph is completely.
    # 2. Graph does not have any cycles. 
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Create adjacency list
        # Maintain a set to record all nodes you have seen. 
        adj = [[] for _ in range(n)]
        seen = set()
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        # Helper DFS function. 
        def dfs(node, parent):
            if node in seen:
                return
            
            # Check if parent's grandchild is already in the seen bucket. 
            # If so then you have cycle!
            seen.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                
                # Check at every step if there is a False. 
                result = dfs(neighbor, node)
                if not result:
                    return False
            # Made it through -> Success!
            return True
        
        # Trigger Point
        return dfs(0, -1) and len(seen) == n
    
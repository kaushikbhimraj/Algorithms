"""
Given an undirected graph, check whether the graph contains a cycle or not. 
Your function should return true if the given graph contains at least one 
cycle, else return false.
"""

# Graph vertex.
class Node:
	def __init__(self, val):
		self.val = val
		self.adj = []

# Graph object.
class Graph:
	def __init__(self):
		self.vertics = {}

	def addNode(self, val):
		node = Node(val)
		if node.val not in self.vertics.keys():
			self.vertics[node.val] = node
			return True
		else:
			return False

	# Non directional
	def addEdge(self, a, b):
		if a.val not in self.vertics.keys() or b.val not in self.vertics.keys():
			return False
		else:
			a.adj.append(b)
			b.adj.append(a)
			return True

# DFS Cycle detection. 
class Cycle:
	def __init__(self):
		self.isCycle = False

	# Using helper function to run the DFS. 
	def checkDAG(self, graph):
		marked = {v:False for v in graph.vertics.keys()}
		for vertex in graph.vertics.keys():
			if graph.vertics[vertex] not in marked:
				self.dfs(graph, Node(-1), graph.vertics[vertex], marked)
		return self.isCycle

	def dfs(self, graph, parent, vertex, marked):
		marked[vertex.val] = True
		for w in graph.vertics[vertex.val].adj:
			if not marked[w.val]:
				self.dfs(graph, vertex, w, marked)
			elif (w.val == parent.val):
				self.isCycle = True

# Unit Test
G = Graph()
G.addNode(0)
G.addNode(1)
G.addNode(2)
G.addNode(3)

G.addEdge(G.vertics[0],G.vertics[1])
G.addEdge(G.vertics[0],G.vertics[2])
G.addEdge(G.vertics[1],G.vertics[2])
G.addEdge(G.vertics[2],G.vertics[3])

C = Cycle()
print(C.checkDAG(G))

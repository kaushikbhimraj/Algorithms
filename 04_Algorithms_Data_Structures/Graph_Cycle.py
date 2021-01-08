"""
Given an undirected graph, check whether the graph contains a cycle or not. 
Your function should return true if the given graph contains at least one 
cycle, else return false.
"""

# Node in graph. 
class Vertex:
	def __init__(self, val):
		self.val = val
		self.adj = []

# Basic graph object.
class Graph:
	def __init__(self, val):
		self.vertics = {}

	def addNode(self, val):
		if val not in self.vertics.keys():
			self.vertics[val] = Vertex(val)
			return True
		else:
			return False

	def addEdge(self, g1, g2):
		if g1.val not in self.vertics.keys() or g2.val not in self.vertics.keys():
			return False
		g1.adj.append(g2)
		g2.adj.append(g1)
		return True

# Union-Find
class disJointSet:
	def __init__(self):
		self.parent = {}

	def makeSet(self, vertics):
		self.parent = {vertex:vertex for vertex in vertics}

	def find(self, x):
		if self.parent[x] == x:
			return x
		self.find(self.parent[x])

	def union(self, a, b):
		self.parent[a] = b

# Union-Find Cycle Detection
def findCycle(graph, n):
	ds = disJointSet()
	ds.makeSet(graph.vertics.keys())
	for vertex in graph.vertics.keys():
		for neighbor in graph.vertics[vertex].adj:
			x = ds.find(vertex.val)
			y = ds.find(neighbor.val)
			if x != y:
				ds.union(x, y)
			else:
				return True
	return False

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

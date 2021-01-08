<<<<<<< HEAD
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
=======
"""
Given an undirected graph, check whether the graph contains a cycle or not. 
Your function should return true if the given graph contains at least one 
cycle, else return false.
"""

# Time:  O(V + E)
# Space: O(V + E)

# Standard graph node
class Node:
	def __init__(self, val):
		self.val = val
		self.adj = []

# Standard Graph (UNDIRECTED)
class Graph:
	def __init__(self):
		self.vertics = {}

	def addNode(self, val):
		if val not in self.vertics:
			self.vertics[val] = Node(val)
			return True
		else:
			return False

	def addEdge(self, a, b):
		if a.val not in self.vertics or b.val not in self.vertics:
			return False

		a.adj.append(b)
		b.adj.append(a)
		return True

# Dis-joint creates a set for each vertex in graph and 
# uses find method to link values to a set. 
class disJointSet:
	def __init__(self):
		self.parent = {}

	def makeSet(self, g):
		self.parent = {x:x for x in g.vertics}

	def find(self, x):
		if (self.parent[x] == x):
			return self.parent[x]
		else:
			return self.find(self.parent[x])

	def union(self, a, b):
		self.parent[x] = y

# Using union-find, detect cycles in graph.
def findCycle(graph, n):
	ds = disJointSet()
	ds.makeSet(graph)
	for vertex in graph.vertics.values():
		for neighbor in vertex.adj:
			x = ds.find(vertex.val)
			y = ds.find(neighbor.val)
			if (x != y):
				ds.union(x,y)
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
>>>>>>> df8c580498458a3c6af83157ac7722b393371909

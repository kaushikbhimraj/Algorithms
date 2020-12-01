"""
Given an undirected graph, check whether the graph contains a cycle or not. 
Your function should return true if the given graph contains at least one 
cycle, else return false.
"""
# Standard graph node (undirected)
class Node:
	def __init__(self, val):
		self.val = val
		self.adj = []

# Standard Graph
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
			self.find(self.parent[x])

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

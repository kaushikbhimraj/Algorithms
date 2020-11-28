"""
Given an undirected graph, check whether the graph contains a cycle or not. 
Your function should return true if the given graph contains at least one 
cycle, else return false.
"""

class Node:
	def __init__(self, val):
		self.val = val
		self.adj = []


class Graph:
	def __init__(self):
		self.vertics = {}
	
	def addVertex(self, val):
		if val not in self.vertics.keys():
			self.vertices[val] = Node(val)
			return True
		else:
			return False

	def addEdge(self, g1, g2):
		if g1.val not in self.vertics.keys() or g2.val not in self.vertics.keys():
			return False
		g1.adj.append(g2)
		g2.adj.append(g1)
		return True


# DFS Cycle Detection.
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

# Union-Find 
class disjointSet:
	def __init__(self):
		self.parent = {}

	def makeSet(self, N):
		self.parent = {i:i for i in range(N+1)}

	def find(self, val):
		if self.parent[val] ==  val:
			return val
		else:
			self.find(self.parent[va])

	def union(self, x, y):
		self.parent[x] = y

# Union-Find Cycle Detection.
def findCycle(self, g, N):
	ds = disjointSet()
	ds.makeSet(N)
	for u in g.vertics:
		for v in u.adj:
			x = ds.find(u.val)
			y = ds.find(v.val)
			if x == y:
				return True
			else:
				ds.union(x, y)
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

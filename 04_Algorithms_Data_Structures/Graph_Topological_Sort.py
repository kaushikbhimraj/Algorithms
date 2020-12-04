# Standard graph node
class Node:
	def __init__(self, val):
		self.val = val
		self.adj = []

# Standard Graph (DIRECTED)
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
		#b.adj.append(a)
		return True

# Topological Sort. 
class TopologicalSort:

	# Either make the stack and visited global parameters or 
	# return them accordingly across the recursive stack. 
	def topSort(self, g):
		stack = []
		visited = set()

		for vertex in g.vertics.values():
			if vertex.val in visited:
				continue
			else:
				self.dfs(vertex, stack, visited)

		start = 0
		end = len(stack) - 1
		while start < end:
			stack[start], stack[end] = stack[end], stack[start]
			start += 1
			end -= 1

		return stack

	def dfs(self, vertex, stack, visited):
		visited.add(vertex.val)
		for child in vertex.adj:
			if child.val in visited:
				continue
			else:
				self.dfs(child, stack, visited)
		stack.append(vertex.val)

# Unit Test
G = Graph()
G.addNode("A")
G.addNode("B")
G.addNode("C")
G.addNode("D")
G.addNode("E")
G.addNode("F")
G.addNode("G")

G.addEdge(G.vertics["A"],G.vertics["C"])
G.addEdge(G.vertics["B"],G.vertics["C"])
G.addEdge(G.vertics["B"],G.vertics["D"])
G.addEdge(G.vertics["C"],G.vertics["E"])
G.addEdge(G.vertics["E"],G.vertics["F"])
G.addEdge(G.vertics["D"],G.vertics["F"])
G.addEdge(G.vertics["F"],G.vertics["G"])

t = TopologicalSort()
print(t.topSort(G))
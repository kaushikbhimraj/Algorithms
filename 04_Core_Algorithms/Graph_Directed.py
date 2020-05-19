"""
Directed Graph using dictionary. 
"""

# GRAPH NODE
class Node:
	def __init__(self, title, name):
		self.title     = title
		self.name      = name
		self.visited   = False
		self.neighbors = []


# DIRECTED 
class Graph:
	def __init__(self):
		self.cache = {}

	def insertVertex(self, title, name):
		if title not in self.cache.keys():
			self.cache[title] = Node(title, name)
			return True
		return False

	def insertEdge(self, parent, child):
		try:
			self.cache[parent]
			try:
				self.cache[child]
				self.cache[parent].neighbors.append(child)
			except KeyError:
				return "Node2 is not in graph"
		except KeyError:
			return "Node1 is not in graph"
		return "Success"




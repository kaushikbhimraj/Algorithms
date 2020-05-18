

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



grph = Graph()

# Adding vertics. 
vertices = [("CEO", "Paul Smith"), ("COO", "Tony James"), ("CFO", "Linda Jones"), ("VP of Marketing", "Dan O'Brien"), ("VP of Engineering", "Jeff Jackson"), ("VP of IT", "Mark Romney"), ("VP Sales", "Scott Burns"), ("Director of Operations", "Elaine Cho"), ("Director of Production", "Bob Zieger"), ("Director of Controller", "Julio Sanchez"), ("Search Marketing Manager", "Jerry Chu"), ("Email Marketing Manager", "Rich Lord"), ("Web Master", "Emese Gris"), ("Programmer I", "Greg Largin"), ("Programmer II", "John Lu"), ("Programmer III", "Mary Cooper"), ("System Admin", "Christine Bellamy"), ("Account Executive I", "Justin Malley"), ("Account Executive II", "Sarah Petravitz"), ("Account Executive III", "Arthur Walker")]

for val in vertices:
	grph.insertVertex(val[0], val[1])

# Creating edges
edges = [("CEO", "COO"), ("CEO", "CFO"), ("CEO", "VP of Marketing"), ("CEO", "VP of Engineering"), ("CEO", "VP of IT"), ("CEO", "VP Sales"), ("COO", "Director of Operations"), ("COO", "Director of Production"), ("CFO", "Controller"), ("VP of Marketing", "Search Marketing Manager"), ("VP of Marketing", "Email Marketing Manager"), ("VP of Marketing", "Web Master"), ("VP of Engineering", "Programmer I"), ("VP of Engineering", "Programmer II"), ("VP of Engineering", "Programmer III"), ("VP of IT", "System Admin"), ("VP Sales", "Account Executive I"), ("VP Sales", "Account Executive II"), ("VP Sales", "Account Executive III")]
for val in edges:
	grph.insertEdge(val[0], val[1])

x = grph.cache["VP Sales"]
print(x.title)
print(x.name)
print(x.neighbors)
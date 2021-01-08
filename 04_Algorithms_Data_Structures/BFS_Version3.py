"""
Use Breadth First Search to find a Vertex in a graph structure. 
"""

from Graph_Directed import Graph

# Loading object
grph = Graph()


# Adding vertics. 
vertices = [("CEO", "Paul Smith"), ("COO", "Tony James"), ("CFO", "Linda Jones"), ("VP of Marketing", "Dan O'Brien"), ("VP of Engineering", "Jeff Jackson"), ("VP of IT", "Mark Romney"), ("VP Sales", "Scott Burns"), ("Director of Operations", "Elaine Cho"), ("Director of Production", "Bob Zieger"), ("Director of Controller", "Julio Sanchez"), ("Search Marketing Manager", "Jerry Chu"), ("Email Marketing Manager", "Rich Lord"), ("Web Master", "Emese Gris"), ("Programmer I", "Greg Largin"), ("Programmer II", "John Lu"), ("Programmer III", "Mary Cooper"), ("System Admin", "Christine Bellamy"), ("Account Executive I", "Justin Malley"), ("Account Executive II", "Sarah Petravitz"), ("Account Executive III", "Arthur Walker")]


for val in vertices:
	grph.insertVertex(val[0], val[1])


# Creating edges.
edges = [("CEO", "COO"), ("CEO", "CFO"), ("CEO", "VP of Marketing"), ("CEO", "VP of Engineering"), ("CEO", "VP of IT"), ("CEO", "VP Sales"), ("COO", "Director of Operations"), ("COO", "Director of Production"), ("CFO", "Controller"), ("VP of Marketing", "Search Marketing Manager"), ("VP of Marketing", "Email Marketing Manager"), ("VP of Marketing", "Web Master"), ("VP of Engineering", "Programmer I"), ("VP of Engineering", "Programmer II"), ("VP of Engineering", "Programmer III"), ("VP of IT", "System Admin"), ("VP Sales", "Account Executive I"), ("VP Sales", "Account Executive II"), ("VP Sales", "Account Executive III")]
for val in edges:
	grph.insertEdge(val[0], val[1])



# Breadth First Search Logic
class search():
	def __init__(self):
		self.queue = []


	def bst(self, graph, targetNodeName):
		self.queue.append(graph)
		return self.helper(targetNodeName)


	def helper(self, targetNodeName):
		if not self.queue:
			return

		currNode = grph.cache[self.queue.pop(0)]
		if currNode.title == targetNodeName:
			self.queue = []
			return currNode
		self.queue += currNode.neighbors
		return self.helper(targetNodeName)


# Search
x = search().bst(grph.cache["CEO"].title, "VP of Engineering")
if x:
	print("\n")
	print("PERSON INFORMATION")
	print("\n")
	print("Person:    ", x.name)
	print("Job Title: ", x.title)
	print("Manages    :", x.neighbors)
	print("\n")
else:
	print(404)

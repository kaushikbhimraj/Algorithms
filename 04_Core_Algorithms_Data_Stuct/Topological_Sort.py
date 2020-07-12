"""
INPUT
jobs = [1, 2, 3, 4]
deps = [[1,2],[1,3],[3,1],[4,2],[4,3]]

OUTPUT
[1,4,3,2] or [4,1,3,2]

Definitions:
	Ordering of the directed graph so all the vertices only go forward. 

Data structures	
	- set/dictionary : use to record the value after the node has been visited. 
	- stack: use to record all the nodes in the topological order. 

Steps:
	- Add all values to the graph. 
	- Traverse all nodes in the graph. 
	- When you visit a vertex in the graph, save it to a set. 
	- Traverse through all its children in a DFS fashion. 
	- Add the current node to a stack when it no longer has any children. 
	- Continue doing until there are no nodes left to traverse. 

"""
from Directional_Graph import graph

class TSort():

	# declaring the data structures. 
	# visited: keeps track of all the visited node.
	# tstack:  records the topological order of the vertex. 
	def __init__(self):
		self.visited = set()
		self.tstack = []

	# iterate through all elements from jobs array. 
	def topology(self, jobs, deps):

		# Converting all values in jobs into a graph. 
		x = graph()
		for i in range(len(jobs)):
			x.insert(jobs[i])

		# Adding dependencies as edges to graph. 
		for vals in deps:
			x.edges(vals[0], vals[1])


		# Iterating through each vertex and conducting a topological sort. 
		for key in x.nodes.keys():
			
			# Check and see if the element is in the visisted dict. 
			if key in self.visited:
				continue

			# Use the helper function to recursively traverse the graph until we find a 
			# vertex with no children. 
			self.topology_helper(x.nodes[key])

		return self.tstack

	# Helper function to find the node without neighbors. (recursive)
	def topology_helper(self, graphVertex):

		# First add the vertex to the visited list. 
		self.visited.add(graphVertex.value)

		# Loop through all the child nodes in a DFS way. 
		for i in range(len(graphVertex.neighbors)):
			childNode = graphVertex.neighbors[i]

			# Avoid repeatitions. 
			if childNode.value in self.visited:
				continue
			
			# Traversing to the deepest node. 
			self.topology_helper(childNode)

		# Insert into stack.
		self.tstack = [graphVertex.value] + self.tstack
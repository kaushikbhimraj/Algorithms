"""
You're given a list of arbitrary jobs that need to be complete; these jobs are represented 
by distinct integers. You're also give a list of dependencies. A dependency is represented
as pair of jobs where the first job is a prerequisite of the second one. In other words, 
the second job depends on the first one; it can only be completed once the first job is 
completed. 

Write a function that takes in a list of jobs and a list of dependecies and returns a list 
containing a valid order in which the given jobs can be completed. If no such other exists, 
the function should return an empty array.

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


ADDITIONAL:
	Current code does not account for cycles. Very important that this be included. 

"""
def topologicalSort(jobs, deps):
	return TSort().topology(jobs, deps)

class TSort():
	def __init__(self):
		# data structures to hold values when sorting.
		self.visited = set()
		self.t_sort = []

	def topology(self, jobs, deps):
		# Convert jobs into vertex.
		x = graph()
		for job in jobs:
			x.insertVertex(job)
		# Convert deps as edges. 
		for dep in deps:
			x.insertEdge(dep[0], dep[1])
		
		# Traverse all nodes in the graph. 
		for vertex in x.nodes.keys():
			if vertex in self.visited:
				continue
			self.topologicalHelper(x.nodes[vertex])
		
		# Sorted vertics are returned. 
		return self.t_sort
			
	def topologicalHelper(self, graphVertex):
		self.visited.add(graphVertex.value)

		# Visit each neighbor and check in visited. 
		for neighbor in graphVertex.neighbors:
			if neighbor.value in self.visited:
				continue

			# Traverse through all its children in a DFS fashion. 
			self.topologicalHelper(neighbor)
		
		# Add the current node to a stack when it no longer has any children. 
		self.t_sort = [graphVertex.value] + self.t_sort
	
	
# Create a graph.
class vertex:
	def __init__(self, value):
		self.value = value
		self.neighbors = []
		
class graph:
	def __init__(self):
		self.nodes = {}
	
	def insertVertex(self, value):
		if value not in self.nodes:
			self.nodes[value] = vertex(value)
		
	def insertEdge(self, startNode, endNode):
		if startNode in self.nodes and endNode in self.nodes:
			startNode, endNode = self.nodes[startNode], self.nodes[endNode]
			
			if endNode not in startNode.neighbors:
				startNode.neighbors.append(endNode)
		


nodes = [1, 2, 3, 4]
links = [[1,2],[1,3],[3,1],[4,2],[4,3]]

print(topologicalSort(nodes, links))
"""
Date: 	03.15.2020
Desc: 	Graphs are very important as data structures to search and traverse for values. 

Time Complexity:
		O(V+E)
Space Complexity:
		O(V+E)
Notes:
	There are two types of graphs - directed and undirected graphs.
	Graphs can be weighted. These weights can be represent a lot of different things. 
	Most important graph is a tree. (undirected graph)

Adjacency List
	Each node will keep track of all its neighbors.
	This is efficient when there are many nodes. But bad when there are many edges. 

Edge List
	List of edges (two nodes and the weight between the nodes)
	Edge look up can be slow and might run into memory problems in large graphs. 

Bridges:
	These are edges, when removed will give rise to new graphs. 

Articulation Points:
	These are nodes on an edge that is a bridge. 

Algorithms:
	DFS 
	BFS
	Dijkstra's
	Bellman-Ford
	Floyd-Warshall
	A*
	Minimum Spanning Trees
	Held-Karp
	Max-Flow

Applications:
	Shortest path problems (BFS, Dijkstra's, Bellman-Ford, Floyd-Warshall, A*, etc)
	Connectivity (Union find, DFS, BFS)
	Negative cycles (Bellman-Ford and Floyd-Warshall) {Negaitive numbers are traps}
	Travelling Salesman Problem (Held-Karp)
	Minimum Spanning Trees (Least sum of weights without loops)
	Max Flow 

"""

"""
Date: 	03.15.2020
Desc: 	Graphs are very important as data structures to search and traverse for values. 

Time Complexity:
		O(V+E)
Space Complexity:
		O(V+E)
Notes:
	There are two types of graphs - directed and undirected graphs.
	Graphs can be weighted. These weights can be represent a lot of different things. 
	Most important graph is a tree. (undirected graph)

Adjacency List
	Each node will keep track of all its neighbors.
	This is efficient when there are many nodes. But bad when there are many edges. 

Edge List
	List of edges (two nodes and the weight between the nodes)
	Edge look up can be slow and might run into memory problems in large graphs. 

Bridges:
	These are edges, when removed will give rise to new graphs. 

Articulation Points:
	These are nodes on an edge that is a bridge. 

Algorithms:
	DFS 
	BFS
	Dijkstra's
	Bellman-Ford
	Floyd-Warshall
	A*
	Minimum Spanning Trees
	Held-Karp
	Max-Flow

Applications:
	Shortest path problems (BFS, Dijkstra's, Bellman-Ford, Floyd-Warshall, A*, etc)
	Connectivity (Union find, DFS, BFS)
	Negative cycles (Bellman-Ford and Floyd-Warshall) {Negaitive numbers are traps}
	Travelling Salesman Problem (Held-Karp)
	Minimum Spanning Trees (Least sum of weights without loops)
	Max Flow 

"""

class Node:
	def __init__(self, value):
		self.val = value
		self.visit = False
		self.neighbor = []

	def insert(self, neigh):
		if neigh not in self.neighbor:
			self.neighbor.append(neigh)
			return True
		else:
			return False

class Graph:

	# All nodes in the graph are maintained in the repo. 
	def __init__(self):
		self.repository = {}

	def add_vert(self, value:str) -> str:
		try:
			self.repository[value]
			return "Exists"
		except KeyError:
			self.repository[value] = Node(value)
			return "Added"

	def add_edge(self, value1:str, value2:str) -> str:
		# Check if value1 is in repo. 
		try:
			node1 = self.repository[value1]
		except KeyError:
			return value1 + " does not exist."
		
		try:
			node2 = self.repository[value2]
		except KeyError:
			return value2 + " does not exist."

		node1.insert(value2)
		node2.insert(value1)
		return "Added"

	def repo(self):
		keys   = self.repository.keys() 
		for val in keys:
			print(val + ": " + self.repository[val].val)



x = ["Kaushik", "Abhishek", "Sylvia", "Michael", "John", "David", "Kelsey", "Monica", "Chandler", "Kaushik"]

Object = Graph()

for i in range(len(x)):
	print(Object.add_vert(x[i]))
print("\n")

Object.add_edge("Kaushik", "Abhishek")
Object.add_edge("Kaushik", "Sylvia")
Object.add_edge("Kaushik", "Michael")
Object.add_edge("Michael", "John")
Object.add_edge("Michael", "David")

print(Object.repository["Kaushik"].neighbor)
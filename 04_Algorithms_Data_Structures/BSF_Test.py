"""
Algorithm: Breath First Algorithm
Notes:     This BFS does not have the self.distance.
            @ Grokkings:
            Breadth first algorihtm answers two questions
                - Is there apth from node A to node B?
                - What is the shortest path from node A to node B?

            What about the shortest path?
            Dijkstra's algorithm aka Greedy algorithm gives us this answer.

Runtime:
            Time complexity:  V + E (vertices + edges)
            Space complexity: V + E (vertices + edges)
"""

# Basic vertex implementation
class Vertex:
    def __init__(self, val):
        self.name = val
        self.distance = 9999
        self.neighbors = []
    
    # Neighbors list holds node objects
    def add_neighbors(self, neighbor):
        if self.neighbors[neighbor]:
            return self.neighbors[neighbor]
        neighbors.append(neighbor)

class Graph:
    allNodes = {}
    def addVertex(self, x):
        if isinstance(Vertex, x):
            try:
                self.allNodes[x.name]
                print("Vertex already exists.")
            except KeyError:
                self.allNodes[x.name] = x
    
    # If the vertex is not in graph, add it to graph and then add the edge to it. 
    def addEdges(self, x, y)->bool:
        if isinstance(Vertex, x) and isinstance(Vertex, y):
            try:
                self.allNodes[x]
                x.add_neighbors(y)
            except KeyError:
                print(x.name + " does not exist in graph.")
                print(" Adding " + x.name + " to graph and adding edge.")
                addVertex(x)
                x.add_neighbors(y)
            try:
                self.allNodes[y]
                y.add_neighbors(x)
            except KeyError:
                print(y.name + " does not exist in graph.")
                print(" Adding " + y.name + " to graph and adding edge.")
                addVertex(y)
                y.add_neighbors(x)
            return True
        else:
            return False
        
    def BFS(self, start, target) -> object:
        count = 1
        visited = {}
        
        # Check graph for start node.
        try:
            obj1 = allNodes[start]

            # Check graph for target node.
            try:
                obj2 = allNodes[target]
                queue = []

                # Add node to visited dictionary.
                visited[obj1.name] = obj1.name
                if obj1.name == obj2.name:
                    return True
                queue.append(obj1.neighbors)

                # Iterate through all neighbors, check if node was visited.
                # pop off the queue after visiting it.  
                while queue:
                    first = queue.pop()
                    try:
                        visited[first.name]
                        pass
                    except KeyError:
                        visited[first.name] = first.name
                        if first.name == obj2.name:
                            first.distance = count
                            return True
                        queue.append(first.neighbors)
                return False
            except KeyError:
                return False
        except KeyError:
            print(start + " does not exist in graph.")
    
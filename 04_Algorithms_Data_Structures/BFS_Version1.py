"""
Graph search - 
        - Exploring a graph (given source node and target node, find a way to reach the target node)
        - Had vertics and edges
                edges - {} --> unordered pair egdes --> undirected graphs (workds in one direction
"""

class Node:
    def __init__(self, value):
        self.name = value
        self.visit = False
        self.distance = 9999
        self.neighbors = []
    
    def add_neighbor(self,neighbor) -> bool:
        if neighbor in self.neighbors:
            return False
        self.neighbors.append(neighbor)
        return True
        
class Graph:
    allNodes = {}
    
    def add_Vertex(self,obj) -> bool:
        if isinstance(Node, obj):
            try:
                allNodes[obj.name]
                return False
            except KeyError:
                allNodes[obj.name] = obj
                return True
    
    def add_edge(self, obj1, obj2) -> bool:
        if isinstance(Node, obj1) and isinstance(Node, obj2):
            
            try:
                allNodes[obj1.name]
                obj1.add_neighbor(obj2)
            except KeyError:
                allNodes[obj1.name] = obj1
                obj1.add_neighbor(obj2)
            
            try:
                allNodes[obj2.name]
                obj2.add_neighbor(obj1)
            except KeyError:
                allNodes[obj2.name] = obj2
                obj2.add_neighbor(obj1)
            
            return True
        return False
    

    # The distance from the start to target is only recorded in the target node. 
    # Function will first check if the node has not been visited. 
    def BFS(self, start, target) -> int:
        queue = []
        count = 1
        if isinstance(Node, start) and isinstance(Node, target):
            if not start.visit:
                if start.name == target.nmae:
                    start.distance = count
                    start.visit = True
                    return count
                queue.append(start.neighbors)
                count += 1

                while queue:
                    first = queue.pop()
                    if not first.visit:
                        if first.name == target.name:
                            first.distance = count
                            start.visit = True
                            return count
                        queue.append(first.neighbors)
                        first.visit = True
                        count += 1
                    
# In place of object.visit in the Node object, a dictionary can be created to store the node name when it is visisted.
# To avoid the loop to iterate continously, this will be a better way to do things. 
# Will still stick to the same time and space complexity. 


            
